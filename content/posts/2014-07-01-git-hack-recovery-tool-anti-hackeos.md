---
title: Git Hack Recovery
author: Alevsk
type: post
date: 2014-07-01T08:51:44+00:00
url: /2014/07/git-hack-recovery-tool-anti-hackeos/
categories:
  - Ethical Hacking
  - Linux
  - Mac
  - Personal
  - Programming
  - Tutorials-ios
tags:
  - campus party
  - Linux
  - Programming
  - software libre
  - Solutions
  - Technology
  - Tutorials

---
En esta ocasión quiero compartir con ustedes una pequeña herramienta que desarrolle (y lo sigo haciendo) y que presente en #CPMX5 como parte de las charlas dadas por miembros de la [Comunidad Underground de México](https://www.underground.org.mx/), la herramienta se llama **Git Hack Recovery** y a grandes rasgos permite que en el caso de que tu sitio web haya sido comprometido por un atacante, los archivos regresen al último estado de confianza de manera automática, ahora explico un poco más.

[![1487876_10203003583025374_7182323267010208382_o](/images/1487876_10203003583025374_7182323267010208382_o.jpg)](http://www.alevsk.com/2014/07/git-hack-recovery-tool-anti-hackeos/1487876_10203003583025374_7182323267010208382_o/)

## Montando el entorno

Para empezar tenemos dos opciones, montar nuestro propio servidor con git o utilizar el servicio de algún tercero que permita crear repositorios privados, para este ejemplo [Bitbucket](bitbucket.org) es una buena opción puesto que nos permite crear repositorios ilimitados. ([https://bitbucket.org/repo/create](https://bitbucket.org/repo/create))

[![bitbucket](/images/bitbucket.jpg)](http://www.alevsk.com/2014/07/git-hack-recovery-tool-anti-hackeos/bitbucket/)

Después debemos de crear 2 cuentas y agregarlas al repositorio, un administrador del con permisos de lectura y escritura y “esclavo" que solo será capaz de leer los archivos del repositorio pero no subir ni modificar nada. (para agregar usuarios al repositorio debes ir a **settings** > **access management**)

[![bitbucket2](/images/bitbucket2.jpg)](http://www.alevsk.com/2014/07/git-hack-recovery-tool-anti-hackeos/bitbucket2/)

Después para mayor comodidad vamos a utilizar pki authentication por lo que debemos crear nuestras respectivas ssh keys en cada maquina (el servidor de producción y la máquina de desarrollo / administración), tutorial: [https://help.github.com/articles/generating-ssh-keys](https://help.github.com/articles/generating-ssh-keys)  
Recapitulando debemos de tener:

  * Repositorio privado
  * Una cuenta con acceso de escritura y lectura al repositorio
  * Una cuenta con acceso de solo lectura al repositorio

Ahora con las tres cosas que tenemos debemos montar una infraestructura como la siguiente:

[![git-hack-recovery](/images/git-hack-recovery.jpg)](http://www.alevsk.com/2014/07/git-hack-recovery-tool-anti-hackeos/git-hack-recovery/)
<div class="demobox" style="margin-top: 10px; height:auto;overflow:auto;">
<em><strong>Tip:</strong> En el caso de que nuestro sitio web utilice urls amigables como wordpress, es recomendable que en nuestro servidor de desarrollo utilicemos [virtual-host](http://www.alevsk.com/2011/04/configuracion-de-host-virtuales-en-mac/) y agreguemos una entrada con el dominio del sitio web que apunte a <strong>127.0.0.1</strong> en nuestro archivo <strong>hosts</strong>, esto porque algunas veces CMS como <strong>wordpress</strong> causan problemas con las urls.</em>
</div>

## Explicación de los Scripts

Esta primera versión de la herramienta está conformada por 5 scripts que se supone deben de correr en segundo background en el servidor de producción, los he separado en dos grupos para que sean más fácil de explicar.

**Scripts de administración**  
Deben de correr en nuestro “trusted system"

  * **auto_commit.sh:** Como su nombre lo indica, hace un **commit**, es util a la hora de que terminamos de agregar algo en **localhost** y queremos que los cambios sean agregados al repositorio
  * **db\_checksum\_backup.sh:** En el caso de que nuestro desarrollo utilice bases de datos con este **script** podemos crear un **backup** de las tablas y almacenar el checksum de las mismas en un archivo para que posteriormente sean revisadas

**Scripts de producción**  
Deben de correr en nuestro servidor de producción

  * **auto_update.sh:** Como su nombre lo indica, el trabajo de este script es revisar si hay nuevos cambios en el servidor Git, si los hay los descargara con el fin de mantener el sitio de producción actualizado
  * **deface_recovery.sh:** Este script se encarga de detectar cambios en los archivos locales, en el caso de que se elimine, modifique o cree un archivo, el script devolverá todo a como estaba originalmente
  * **db\_checksum\_validator.sh:** En el caso de que un atacante haya comprometido nuestra base de datos (agregado, eliminado o modificado información de la misma), este script detectara que hubo una modificación de las tablas utilizando el **checksum** y las restaurara utilizando la copia que tiene del **servidor Git**

<div class="demobox" style="margin-top: 10px; height:auto;overflow:auto;">
<em><strong>Tip:</strong> Es recomendable que los script de producción corran mediante <strong>cronjobs </strong>mientras que los de administración sean bajo demanda</em>
</div>

## Integrar los scripts con un proyecto

Primeramente, en nuestra laptop o la máquina de donde subiremos los cambios (normalmente **localhost**) clonaremos el repositorio usando la cuenta de administrador, y agregaremos los archivos de nuestro sitio web, blog de wordpress, joomla, desarrollo a la medida o lo que sea, después para integrar **Git Hack Recovery** es tan fácil como descargar los archivos del siguiente enlace [Git Hack Recovery](https://github.com/Alevsk/Git-Hack-Recovery) y colocarlos junto con los archivos del sitio web que queremos proteger, el archivo .gitignore ya contiene las entradas para que los scripts de administración sean ignorados al momento de hacer los commits. Una vez tenemos los archivos listos en la maquina “trusted" podemos correr los scripts de administración (en este orden)

```bash
$ ./db\_checksum\_backup.sh host-name db-name db-user db-pass  
$ ./auto_commit.sh remote-name branch-name "your-commit-message"
```

En este punto tanto nuestro sistema “trusted" como nuestro servidor Git estarán sincronizados con los mismos archivos, ahora en el servidor de producción vamos a clonar el repositorio de **Git** utilizando la cuenta “esclavo", esto nos asegura que en caso de que alguien vulnere el servidor de producción (que es el que normalmente está expuesto a Internet), solo seguirá teniendo acceso de lectura al repositorio en el servidor **Git**. En el servidor de producción es donde debemos de correr los 3 scripts que nos faltan como taras cron, para hacerlo podemos abrir el archivo de configuración de cronjobs usando el comando:

```bash
# crontab -e
```

Y agregar las siguientes entradas

```bash
\*/1 \* \* \* * cd /path/production-repository/; /bin/bash deface\_recovery.sh –arguments > /path/deface\_recovery.txt  
\*/1 \* \* \* * cd /path/production-repository/; /bin/bash auto\_update.sh –arguments > /path/auto\_update.txt  
\*/1 \* \* \* * cd /path/production-repository/; /bin/bash db\_checksum\_validator.sh –arguments > /path/db\_checksum\_validator.txt
```

Estos scripts se estarán ejecutando cada minuto y guardaran un log en el path que le indiquemos. Listo, esto ha sido un pequeño tutorial de cómo integrar la herramienta, es la versión 1.0 pero cumple con su cometido, estaré trabajando para agregarle funcionalidades extras así como soporte para manejar más motores de bases de datos. <del datetime="2014-07-03T00:16:09+00:00">Próximamente estaré subido algunos vídeos de donde se aprecie el funcionamiento de la misma</del>. 

## Git Hack Recovery en acción



Descargar [Git Hack Recovery](https://github.com/Alevsk/Git-Hack-Recovery)

salu2
---
title: 'Configurar servidor web en ubuntu 10.04 e instalar CakePHP [2]'
author: Alevsk
type: post
date: 2010-12-12T08:14:25+00:00
url: /2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-2/
categories:
  - Linux
  - Personal
  - Sin categoría
  - Tips
  - Tutorials
tags:
  - backtrack
  - Linux Debugging
  - debian
  - Storage
  - distros
  - grep
  - grub
  - Linux
  - Personal
  - shell
  - slackware
  - software libre
  - Solutions
  - Tutorials
  - ubuntu

---
![](/images/uploadfirst.jpg)

Si estas leyendo este post es por que probablemente lograste instalar apache satisfactoriamente siguiendo el post anterior. El orden de los tutoriales es el siguiente:

<div class="demobox" style="height:auto;">
<ul>
<li>
[Instalación de Apache](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-1)
</li>
<li>
[Instalación de soporte para paginas en PHP](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-2)
</li>
<li>
[Instalación de gestor de base de datos MYSQL y el phpmyadmin](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-3)
</li>
<li>
[Instalación de CakePHP en Linux](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-4)
</li>
</ul>
</div>

### Instalando **PHP**

No planeo explicar lo que es el lenguaje de programación PHP solo quiero decir que hoy en día es muy utilizado a lo largo y ancho de toda la red y es necesario que nuestro servidor web tenga soporte para esta tecnología y así poder crear códigos mas elaborados. Ya que tenemos el servidor apache corriendo al 100% ahora instalamos el php con el siguiente comando

```Transact-SQL
alevsk@aosnet:~$ sudo apt-get install php5-cgi php5-cli php5-common libapache2-mod-php5
```

Con este comando instalaran **PHP** (opcional: el gestor de instalación les sugerirá que instalen otros paquetes también, no están de mas, yo los instale también :)).

Ahora para hacer la prueba y ver si **PHP** se instalo correctamente creen un archivo que contenga

```Text only
<'?php phpinfo(); ?'>
```

Y lo guardan en la carpeta a la que apunta su servidor web  
_**los < y > sin las ' (wordpress no me los imprime si los dejo asi tal cual por seguridad :p), pueden crear el archivo rápidamente con el siguiente comando**_ 

```Transact-SQL
alevsk@aosnet:~$ echo "<'?php phpinfo(); ?'>" >> /home/nomreusuario/www/info.php
```

y ahora visiten el archivo desde su navegador preferido 🙂 y si todo salio bien les deberá aparecer algo así en su pantalla.

![](/images/phpinfo.png) 

Ya casi acabamos, el siguiente paso es:

<div class="demobox" style="height:auto;">
  El siguiente paso es [Instalación de gestor de base de datos MYSQL y el phpmyadmin](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-3)
</div>
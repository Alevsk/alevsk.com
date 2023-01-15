---
title: 'Configurar servidor web en ubuntu 10.04 e instalar CakePHP [3]'
author: Alevsk
type: post
date: 2010-12-12T08:15:51+00:00
url: /2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-3/
categories:
  - Linux
  - Personal
  - Programming
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
  - Programming
  - shell
  - slackware
  - software libre
  - Solutions
  - Tutorials
  - ubuntu

---
![](/images/data_base.jpg)

En este punto ya deberíamos de tener nuestro servidor web corriendo bajo **Apache** y con soporte para paginas webs hechas con **PHP** habilitado :), pero aun nos falta otro servicio muy importante, la gestión de bases de datos, el mas común es instalar **MYSQL**, también en este tutorial aprenderemos a instalar un manejador grafico llamado **phpmyadmin**.

También les recuerdo el orden de los tutoriales por si les han quedado dudas y quieren regresar:

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

### Instalando **MYSQL**

Como en los 2 tutoriales anteriores aremos uso de la shell de Linux para mayor rapidez, lo primero sera instalar mysql con el siguiente comando:

```Transact-SQL
alevsk@aosnet:~$ sudo apt-get install mysql-server mysql-client php5-mysql
```

Después de descargar los paquetes, durante la instalación nos pedirá que creemos una contraseña para el **root** de **mysql**, escribe una que no se te olvide :p que la necesitaras mas adelante.

### Instalando **PhpMyAdmin**

Después de haber instalado **MYSQL** es opcional instalar un manejador gráfico, en este caso nos enfocaremos en **phpmyadmin**, los mas puristas como yo jeje :p nos sentiremos bien usando la consola, pero para los usuarios mas nuevos les recomiendo instalar esta interfaz **web**, ya que desde **phpmyadmin** pueden crear, modificar, eliminar … hacer y deshacer cosas en las bases de datos.

Escriban el siguiente comando y comenzara la descarga y la instalación:

```Transact-SQL
alevsk@aosnet:~$ sudo apt-get install phpmyadmin
```

Durante la instalación les sera pedida la contraseña del **root** de **mysql** que definieron anteriormente, escriban-la para que continué.

Al terminar la instalación **PhpMyAdmin** se abra instalado en **/etc/phpmyadmin**, ahora tenemos que crear un enlace simbólico para poder acceder desde el directorio al cual apunta nuestro servidor web, si recordamos la aplicacion no esta en el mismo directorio ;).

Los enlaces simbólicos son como los accesos directos de **Windows** … mm creo que ese seria un ejemplo algo claro xD, creamos el enlace simbolico con el siguiente comando:

```Transact-SQL
alevsk@aosnet:~$ ln -s /etc/phpmyadmin /home/nombreusuario/www/phpmyadmin
```

Después de eso ya seremos capaces de acceder a **PhpMyAdmin**, tenemos que visitar la siguiente dirección desde nuestro navegador **http://localhost/phpmyadmin** como se muestra en la siguiente imagen

![](/images/url_phpmyadmin.png) 

Nos pedira el nombre de usuario que es **root** y la contraseña que definimos anteriormente y entraremos a la interfaz web donde podremos comenzar a crear bases de datos 🙂

![](/images/phpmyadmin.png) 

Ya con los servicios basicos corriendo solo resta instalar nuestro framework favorito 🙂 **[CakePHP][1]**, de la misma manera podriamos instalar un wordpress o un joomla ya con el servidor web corriendo apache, php y mysql.

<div class="demobox" style="height:auto;">
  El siguiente paso es [Instalación de CakePHP en Linux](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-4)
</div>

 [1]: http://cakephp.org/
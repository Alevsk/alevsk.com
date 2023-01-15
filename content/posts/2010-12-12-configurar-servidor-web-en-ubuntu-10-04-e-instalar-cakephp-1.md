---
title: 'Configurar servidor web en ubuntu 10.04 e instalar CakePHP [1]'
author: Alevsk
type: post
date: 2010-12-12T05:04:36+00:00
url: /2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-1/
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
  - Linux
  - shell
  - slackware
  - software libre
  - Solutions
  - Tutorials
  - ubuntu
  - web

---
![](/images/server_rack.jpg)

La razón por la que he decidido crear este tutorial es por que en la red hay bastantes otros tutoriales muy buenos sobre instalación de un servidor web con los servicios básicos en Linux, sin embargo y para ser sinceros, yo nunca he podido hacer que el servidor quede como yo quiero siguiendo un solo manual jeje, osea que tengo que estar revisando varios a la vez y haciendo y deshaciendo lo que le falte o lo que le sobre a uno y a otro.

También en este tutorial quiero cubrir la parte de la instalación de **[CakePHP][1]** en linux, son solo unos pasos extra que se deben realizar después de montar el servidor web.

**Como sera un tutorial algo extenso he decidido dividirlo en 4 post, el orden del tutorial es el siguiente:**

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

Antes que nada, si tienes prisa y no tienes tiempo de instalar los servicios individualmente y realizar configuraciones te recomiendo mi otro [tutorial de instalación de **lampp**][2] (xampp para linux) en **linux** con el que con 2 clics tendrás tu servidor web listo y corriendo

Comenzamos:

### Instalando **Apache**

Lo primero que tendremos que hacer sera instalar apache, esto lo hacemos rápidamente con un par de comandos en la consola

```Transact-SQL
alevsk@aosnet:~$  sudo apt-get install apache2
alevsk@aosnet:~$  sudo apt-get install apache2-mpm-prefork

```

Necesitamos permisos de super usuario por eso el “**sudo**" delante de cada comando, se les pedirá que confirmen la descarga de los paquetas, escriben “**S**" y comenzara la descarga, cuando termine pueden ver si el servidor esta corriendo escribiendo en su **navegador** **http://localhost**, si todo va bien veran un “It Works" que significa que la instalación de apache fue exitosa.

Ahora tenemos que configurara algunas cosas, nada del otro mundo. Los siguientes pasos son opciones, por default el directorio hacia donde apunta el servidor web se encuentra en **/var/www/** pero podemos modificar esa ruta por alguna que nos convenga mas como por ejemplo nuestra carpeta de usuario, si quisiéramos podría quedar **/home/nombreusuario/www/** por ejemplo, tendremos que editar el archivo default que utiliza apache, esto se hace de la siguiente manera.

```Transact-SQL
alevsk@aosnet:~$ sudo gedit /etc/apache2/sites-available/default

```

Ahí yo estoy abriendo el archivo con el editor de texto **gedit** pero lo pueden hacer con el que ustedes quieran, si usan **Kubuntu** seria **kate** o desde consola **vim**. Cuando abran el archivo veran que mas o menos al principio aparecen 2 **paths** (rutas) que son mas o menos así **/var/www/** esas son las que tienen que modificar por la ruta a la que desen que apunte el servidor web por ejemplo:

<p style="text-align: left;">
![](/images/apache_default.png)
</p>

Como ven yo he remplazado la ruta anterior por **/home/alevsk/www/** que es donde guardare los archivos que quiero compartir en la red, guardan y cierran el archivo.

Ahora tenemos que crear la carpeta www que es la que definimos en el archivo de configuración default (o el nombre que le hayan puesto)

```Transact-SQL
alevsk@aosnet:~$ mkdir /home/nombreusuario/www/

```

Ya que hayan completado los pasos anteriores tenemos que reiniciar el servidor, con el siguiente comando

```Transact-SQL
alevsk@aosnet:~$ sudo /etc/init.d/apache2 restart
```

Aqui yo tube algunos problemas ya que por una razon que desconosco me daba un error, el error en cuestion era “**apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1 for ServerName … waiting apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1 for ServerName**" googleando encontre la solucion, lo que tienen que hacer es editar el archivo **httpd.conf** de apache que por default en la version 2 esta vacio

```Transact-SQL
alevsk@aosnet:~$sudo gedit /etc/apache2/httpd.conf
```

y agregar **ServerName localhost** como aparece en la siguiente imagen.

![](/images/httpd_apache.png) 

Ahora si vuelven a escribir el comando

```Transact-SQL
alevsk@aosnet:~$ sudo /etc/init.d/apache2 restart
```

Y ya no les tiene que dar errores ni nada :).

<div class="demobox" style="height:auto;">
  El siguiente paso es [Instalación de soporte para paginas en PHP](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-2)
</div>

 [1]: http://cakephp.org/
 [2]: http://www.alevsk.com/2010/07/instalando-xampp-en-linux/
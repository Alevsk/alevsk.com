---
title: 'Configurar servidor web en ubuntu 10.04 e instalar CakePHP [4]'
author: Alevsk
type: post
date: 2010-12-12T08:17:50+00:00
url: /2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-4/
Thumbnail:
  - /images/tuto_cake_serv_4.jpg
categories:
  - Linux
  - Personal
  - Programming
  - Sin categor铆a
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
![](/images/cake_info.jpg)

Llegados ha este punto nuestro servidor web debe funcionar sin problemas y ya somos capaz de instalar cualquier script **PHP** que utilice una base de datos :), les recuerdo el orden de los tutoriales por si ha alguien se le olvido 馃檪

<div class="demobox" style="height: auto;">
<ul>
<li>
[Instalaci贸n de Apache](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-1)
</li>
<li>
[Instalaci贸n de soporte para paginas en PHP](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-2)
</li>
<li>
[Instalaci贸n de gestor de base de datos MYSQL y el phpmyadmin](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-3)
</li>
<li>
[Instalaci贸n de CakePHP en Linux](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-4)
</li>
</ul>
</div>

### Instalando **CakePHP**

Ok lo primero que tienen que hacer es [descargarse][1] la ultima versi贸n estable del framework, ya descargado lo descomprimen, lo renombran a **cake** para mayor comodidad y lo pegan en **/home/nombreusuario/www/** o el directorio a donde apunte su servidor web.

Para que funcione bien tenemos que darle permisos de escritura, lectura y ejecuci贸n (como se supone que es un servidor casero nada mas para hacer pruebas no importa mucho a que directorios darle permisos y a cuales no:p) asi que:

```Transact-SQL
alevsk@aosnet:~$ sudo chmod 777 /home/nombreusuario/www/cake/ -R
```

Ahora tenemos que habilitar el modulo mod_rewrite para que el framework funcione bien y poner AllowOverried All en el fichero default

Habilitar el mod rewritte:

```Transact-SQL
alevsk@aosnet:~$ sudo a2enmod rewrite
```

Y ahora abrimos el fichero default y cambiamos el **AllowOverride None** por **AllowOverride All** (nada mas los 2 primeros que aparecen como se muestra en la imagen a continuaci贸n)

```Transact-SQL
alevsk@aosnet:~$ sudo gedit /etc/apache2/sites-available/default
```
![](/images/apache_default.png) 

Y ahora si visitamos **http://localhost/cake/** veremos que cakePHP ya esta listo para ser configurado y usado 馃檪

![](/images/cake_example.png) 

Yo aqu铆 he instalado una aplicaci贸n que hice hace tiempo ya con todo y su base de datos y si funciona muy bien 馃槈

![](/images/dae_example.png) 

salu2 y espero disfruten esta serie de tutoriales, ha instalar servidores web todos xD!

 [1]: https://github.com/cakephp/cakephp/downloads
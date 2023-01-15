---
title: Instalando XAMPP en Linux
author: Alevsk
type: post
date: 2010-07-11T21:31:04+00:00
url: /2010/07/instalando-xampp-en-linux/
image:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/xampp.jpg
slider_thumbnail:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/xampp-thumb.jpg
categories:
  - Technology
  - Tips
  - Tutorials
tags:
  - apache
  - php
  - phpmyadmin
  - proftp
  - www
  - xampp

---
Como todo buen desarrollador web tenemos la necesidad de montar un servidor web en la maquina en la que trabajemos, una buena alternativa es XAMPP ya que nos instala los servicios básicos, APACHE, PHP, MYSQL, PROFTP y el gestor phpmyadmin para que sea mas fácil manejar las bases de datos.

Si usan windows pueden descargar el ejecutable directamente de http://www.apachefriends.org/es/xampp-windows.html y con 2 clics ya lo tendrán instalado, muy fácil, ahora si usan alguna distribución de linux hay que hacer unos cuantos pasos mas pero nada del otro mundo.

Paso 1  
Descarguen-se el xampp para linux (lampp) de este link: http://www.apachefriends.org/en/xampp-linux.html#374 , en este momento la versión es “XAMPP Linux 1.7.3a"

<!--more-->

Paso 2  
Probablemente si usan Firefox el archivo se descargo en la carpeta de Descargas, accedan a esa carpeta y después a descomprimir y a copiar al directorio /opt, el comando es el siguiente

```Transact-SQL
tuusuario@tumaquina:~$  sudo tar xvfz xampp-linux-1.7.2.tar.gz -C /opt
```

Paso 3  
Ya con esto Xampp (Lampp) que da instalado en el directorio /opt/lampp y para levantar los servicios y comenzar a utilizarlo escribimos en la terminal de la siguiente manera:

```Transact-SQL
tuusuario@tumaquina:~$ sudo /opt/lampp/lampp start
```

Si quisiéramos parar el servicio o reiniciarlo solo basta con usar el parámetros STOP o RESTART en lugar de START quedando así:

```Transact-SQL
tuusuario@tumaquina:~$ sudo /opt/lampp/lampp stop
```

o

```Transact-SQL
tuusuario@tumaquina:~$ sudo /opt/lampp/lampp restart
```

Paso 4  
Por ultimo los archivos que son públicos se guardan en /opt/lampp/htdocs/ pero yo por comodidad cree un enlace simbólico en /home/alevsk/www/ y a /opt/lampp/htdocs/ le agregue el directorio www para que quede todo mas organizado, pueden crear su enlace de la siguiente manera

```Transact-SQL
tuusuario@tumaquina:~$ ln -s  /opt/lampp/htdocs/www/
```

Paso 5  
Ya por ultimo solo queda darle permisos, como es un servidor para pruebas nadamas esta bien que le des permisos de escritura, lectura y ejecución (777) a todo el directorio www de la siguiente manera

```Transact-SQL
tuusuario@tumaquina:~$ sudo chmod 777 /opt/lampp/htdocs/www -R
```

El parámetro -R es muy importante para que los permisos se asignen a todos los directorios que contenga www, esto lo debes hacer cada vez que agregues un proyecto nuevo, hay otra forma cambiando el propietario con el comando chown, pero creo que para un servidor de pruebas esta bien esta.

Bueno espero que les haya gustado el tutoríal, cualquier duda postearla en los comentarios por favor

salu2
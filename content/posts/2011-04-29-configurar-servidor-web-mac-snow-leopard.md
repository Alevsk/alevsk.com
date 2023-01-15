---
title: Configurar servidor web en Mac snow leopard
author: Alevsk
type: post
date: 2011-04-29T05:25:35+00:00
url: /2011/04/configurar-servidor-web-mac-snow-leopard/
categories:
  - Linux
  - Mac
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - backtrack
  - campus party
  - Linux Debugging
  - debian
  - distros
  - mac
  - php
  - Solutions
  - Technology
  - Tutorials
  - ubuntu
  - web

---
[![](/images/20624-macbook_super.jpg)](http://www.alevsk.com/2011/04/configurar-servidor-web-mac-snow-leopard/20624-macbook_super/)  
En un post anterior les enseñe como configurar los [host virtuales en MAC][1], por si alguien aun no tiene configurado su servidor web en **MAC** aquí están los pasos a seguir, es muy sencillo y en un dos por tres lo tendrán listo.

## Habilitar Apache

Lo primero es activar el [servidor apache][2], para ello abrimos una terminal (ya saben, spotlight, escriben [Terminal][3] y eligen la primera opción), una vez que la app este abierta escribimos el siguiente comando:

```Text only
sudo apachectl start
```

## Habilitar PHP

Despues de eso necesitamos editar el archivo **httpd.conf** para cargar el modulo de [PHP][4] asi que en la consola escribimos el siguiente comando:

```Text only
sudo /Applications/TextEdit.app/Contents/MacOS/TextEdit /etc/apache2/httpd.conf
```

Luego de eso localizamos la linea donde este

```bash
#LoadModule php5_module libexec/apache2/libphp5.so
```

Y lo des comentamos quitando el signo de #, tambien buscamos la linea donde se encuentre:  
```bash
#DocumentRoot "/Library/WebServer/Documents"
```  
Y lo descomentamos y ponemos la ruta donde tengamos planeado guardar los archivos que seran publicos en el servidor **web**, yo lo deje de la siguiente manera:

```bash
DocumentRoot "/Users/alevsk/Sites"
```

Después de eso reiniciamos el **servidor**

```Text only
sudo apachectl restart
```

Con eso ya nuestro servidor web deberia de estar activado, podemos comprobarlo accediendo a la siguiente direccion http://localhost/, si nos aparece el mensaje de **It works!** quiere decir que el servidor fue activado con éxito.

Los siguientes pasos son opcionales, es solamente para configurar algunas cosas como el **timezone** por ejemplo.

Lo primero es crear un archivo **php.ini** en **/etc** y darle permisos de lectura y escritura, para ello en la **consola** escribimos

```bash
cd /etc  
sudo cp php.ini.default php.ini  
sudo chmod 666 php.ini
```

abrimos el archivo con

```Text only
sudo /Applications/TextEdit.app/Contents/MacOS/TextEdit php.ini
```

y buscamos la linea que diga **;date.timezone =**, la des comentamos (le quitamos el **;** ) y escribimos nuestra zona horaria por ejemplo

```bash
date.timezone =America/Mexico
```

En este [link][5] pueden encontrar una gran lista con la mayoría de las zonas horarias y códigos del mundo.

Despues de eso guardamos, salimos del archivo y reiniciamos **apache**

```Text only
sudo apachectl restart
```

## Habilitar MYSQL

Primero [descargamos el paquete de MYSQL][6], elegimos la version de 32 o 64 bits según sea nuestro caso.

Despues tenemos que instalar todo lo que venga dentro del paquete en el siguiente orden:  
**1)** mysql  
**2)** startup item  
**3)** preference pane

Para verificar que se instalo correctamente desde la consola verificamos accediendo al binario de la siguiente manera

```Text only
/usr/local/mysql/bin/mysql
```

Si nos aparece la consola de [mysql][7] quiere decir que se ha instalado correctamente.

Después de eso regresamos a la consola y editamos el archivo **php.ini** de nuevo y remplazamos las lineas que coincidan con **/var/mysql/mysql.sock** por **/tmp/mysql.sock**

```bash
pdo\_mysql.default\_socket=/tmp/mysql.sock  
mysql.default_socket = /tmp/mysql.sock  
mysqli.default_socket = /tmp/mysql.sock
```

y una vez mas reiniciamos **Apache**

Si todo resulto ahora tenemos [Apache][2], [PHP][8] y [MYSQL][7] en nuestro servidor :).

 [1]: http://www.alevsk.com/2011/04/configuracion-de-host-virtuales-en-mac/
 [2]: http://www.alevsk.com/?s=apache&x=0&y=0
 [3]: http://www.alevsk.com/?s=shell&x=0&y=0
 [4]: http://www.alevsk.com/?s=PHP&x=0&y=0
 [5]: http://php.net/manual/en/timezones.php
 [6]: http://dev.mysql.com/downloads/mysql/5.1.html#macosx-dmg
 [7]: http://www.alevsk.com/?s=mysql&x=0&y=0
 [8]: http://www.alevsk.com/?s=php&x=0&y=0
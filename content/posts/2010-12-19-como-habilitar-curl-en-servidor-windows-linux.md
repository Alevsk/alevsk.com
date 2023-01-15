---
title: Como habilitar cURL en servidor Windows y Linux
author: Alevsk
type: post
date: 2010-12-19T20:32:11+00:00
url: /2010/12/como-habilitar-curl-en-servidor-windows-linux/
Thumbnail:
  - /images/servers.jpg
categories:
  - Linux
  - Technology
  - Tips
  - Tutorials
tags:
  - backtrack
  - Linux Debugging
  - debian
  - Linux
  - shell
  - slackware
  - software libre
  - Solutions
  - Technology
  - Tutorials
  - ubuntu
  - web

---
[![](/images/perfil_facebook.jpg)](http://www.alevsk.com/2010/12/como-habilitar-curl-en-servidor-windows-linux/perfil_facebook/)

Estoy comenzando un nuevo proyecto, que trabajare en mis tiempos libres, y una de las cosas es la utilización de **facebook** connect. **Facebook Connect** permite iniciar sesión en nuestros sitios con la cuenta de facebook del usuario, es una aplicación muy popular que hoy en día podemos ver en comunidades creadas con **joomla** o en foros gestionados por **WordPress** :), y claro también se puede utilizar para nuestros desarrollos.

Uno de los requisitos es la utilización de **cURL**, para mas información http://es.wikipedia.org/wiki/CURL.

En Windows utilizo wamp server por la comodidad de lanzar los servicios con un clic y en Linux si instale cada servicio por separado para tener mas control y bueno el problema es que por defecto cURL no se instala o no viene habilitado, a continuación en-listo los pasos que yo seguí para poder utilizar este modulo en nuestros desarrollos.

### En Windows

Si tienes Wamp server instalado los pasos son los siguientes:

  * Tirar el server abajo (cerrar el wamp)
  * Ir a C:/wamp/bin/php/(tuversion)
  * Abrir el archivo php.ini con algún editor de texto plano como el **notepad** o **notepad++**
  * Buscar la palabra curl, descomentar (sacar el punto y coma) extension=php_curl.dll y guardar
  * Ir a C:/wamp/bin/apache/(tuversion)/bin/
  * Abrir el archivo php.ini con algún editor de texto plano como el notepad o notepad++ (se repite el paso 3)
  * Buscar la palabra curl, descomentar (sacar el punto y coma) extension=php_curl.dll y guardar
  * Levantar el WAMP nuevamente y listo.

### En Linux

Esto lo hice en un Ubuntu 10.04 y funciono 🙂 los pasos para habilitarlo en Linux son estos:

Abrir la consola y escribir:

```Transact-SQL
alevsk@aosnet:~$ sudo apt-get install curl libcurl3 libcurl3-dev php5-curl
```

Pedirá confirmación para instalar los paquetes, escriben “S" y despues de que queden instalados reinician el servidor

```Transact-SQL
alevsk@aosnet:~$ sudo /etc/init.d/apache2 restart

```

Fuentes:  
http://www.rodrigoasensio.com/2010/01/como-habilitar-curl-en-windows/  
http://www.blog.highub.com/php/php-core/linux-ubuntu-install-setup-php-curl/
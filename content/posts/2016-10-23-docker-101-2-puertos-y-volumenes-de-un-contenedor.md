---
title: 'Docker 101 #2: puertos y volúmenes de un contenedor'
author: Alevsk
type: post
date: 2016-10-23T03:51:50+00:00
url: /2016/10/docker-101-2-puertos-y-volumenes-de-un-contenedor/
categories:
  - cloud
  - Geek
  - Linux
  - Personal
  - Technology
  - Tips
  - Tutorials
tags:
  - cloud
  - containers
  - docker
  - iaas
  - Linux
  - Personal
  - Programming
  - shell
  - software libre
  - Solutions
  - Technology
  - Tutorials
  - web

---
[![docker-image](/images/docker-image.png)](http://www.alevsk.com/2016/10/docker-101-1-introduccion-a-docker-y-los-contenedores/docker-image/)

En el artículo anterior comenzamos con una breve [introducción a docker][1], vimos su instalación, configuración e incluso lanzamos un par de [servidores web nginx][2] usando contenedores, en esta ocasión explicare un poco más acerca de los puertos y los volúmenes.

## Puertos

Ok, lo primero que explicare será el mapeo de puertos, abrimos una terminal y ejecutamos el siguiente comando:

```bash
$ sudo docker run –name servidor-web -p 80:80 nginx
```

El parametro **–name** sirve para asignarle un nombre al contenedor.

El parámetro **-p** sirve para realizar el mapeo de puertos y recibe una cadena en el formato **PUERTO-HOST:PUERTO-CONTENEDOR**, es decir, del lado izquierdo definimos el puerto que nuestro sistema operativo le asignara al contenedor de docker y del lado derecho el puerto en el que realmente se ejecuta el servicio dentro del contenedor, en este caso **nginx** (suena un poco confuso al inicio así que regresa y léelo de nuevo hasta que lo entiendas)

En el comando anterior estamos mapeando el **puerto 80** de nuestra computadora con lo que sea que este corriendo en el **puerto 80** del contenedor, es por eso que si vamos a **http://localhost** veremos el servidor web en ejecución 🙂

[![nginx](/images/nginx.png)](http://www.alevsk.com/2016/10/docker-101-2-puertos-y-volumenes-de-un-contenedor/nginx/)

En la consola desde donde ejecutaste el comando podrás ver las peticiones hechas al servidor dentro del contenedor.

[![docker-cli](/images/docker-cli.png)](http://www.alevsk.com/2016/10/docker-101-2-puertos-y-volumenes-de-un-contenedor/docker-cli/)

Al ejecutar el comando y correr el contenedor abras notado que la consola se queda bloqueada por el servidor web, para evitar eso podemos correr el contenedor en modo **detach** con el parámetro **-d**, esto ejecutara el contenedor en segundo plano.

```bash
$ sudo docker run -d –name servidor-web -p 80:80 nginx
```

[![docker_detach](/images/docker_detach.png)](http://www.alevsk.com/2016/10/docker-101-2-puertos-y-volumenes-de-un-contenedor/docker_detach/)

Observa como tan pronto como ejecutamos el comando docker nos devuelve el control de la terminal, cuando ejecutas contenedores de esta forma no olvides que para eliminarlos primero tienes que recuperar su id, el cual puedes obtener haciendo:

```bash
$ sudo docker ps
```

y en la primera columna encontraras el ID del contenedor que después deberás de eliminar usando **sudo docker rm [CONTAINER-ID]**, si lo prefieres un tip muy útil para borrar todos los contenedores que hayas creado es ejecutar:

```bash
$ sudo docker stop $(sudo docker ps -a -q)  
$ sudo docker rm $(sudo docker ps -a -q)
```

El primer comando detiene todos los contenedores que estén en ejecución y el segundo los elimina todos (no puedes eliminar un contenedor que este en ejecución).

Puedes correr todas los contenedores que quieras (o necesites) de nginx en diferentes puertos y con diferentes nombres y cada uno será una instancia completamente diferente del servidor web 🙂  
[![containers](/images/containers.png)](http://www.alevsk.com/2016/10/docker-101-2-puertos-y-volumenes-de-un-contenedor/containers/)

Observa como cada uno de los servidores web corren en un puerto diferente.

[![multi-docker](/images/multi-docker.png)](http://www.alevsk.com/2016/10/docker-101-2-puertos-y-volumenes-de-un-contenedor/multi-docker/)

## Volúmenes

Los volúmenes en docker pueden ser definidos con el parámetro **-v** y nos ayudan a resolver el problema de la persistencia de datos en los contenedores, un volumen puede ser visto como un mapeo entre un directorio de nuestra computadora y un directorio en el sistema de archivos del contenedor, regresemos a nuestro **contenedor de nginx**, ¿cómo le hacemos para mostrar un sitio web en nginx en lugar de la página por default?

Lo primero que haremos será crear una carpeta en donde colocaremos el código fuente de nuestro [sitio web html][3] (por ahora no trabajaremos con nada dinamico), por ejemplo **website**

[![website](/images/website.png)](http://www.alevsk.com/2016/10/docker-101-2-puertos-y-volumenes-de-un-contenedor/website/)

Ejecutamos el siguiente comando mapeando el contenido de **/home/alevsk/dev/sitio-web** hacia **/usr/share/nginx/html** que es el directorio por default que utiliza **nginx** para servir contenido a Internet.

```bash
$ sudo docker run -d –name sitio-web -v /home/alevsk/dev/sitio-web:/usr/share/nginx/html -p 80:80 nginx
```

La próxima vez que visitemos **http://localhost/** veremos nuestro sitio web corriendo.

[![nginx-web](/images/nginx-web.png)](http://www.alevsk.com/2016/10/docker-101-2-puertos-y-volumenes-de-un-contenedor/nginx-web/)

Puedes replicar este contenedor con el contenido del sitio web tantas veces como quieras, es muy util en un escenario donde necesitas varios ambientes para pruebas, desarrollo, etc.

Eso es todo por ahora, en el siguiente tutorial aprenderemos a crear nuestras propias **imágenes de docker** (dockerizar aplicaciones), después de eso veremos otra herramienta bastante útil llamada **docker-compose** para facilitar la orquestación de aplicaciones que utilizan múltiples contenedores.

Saludos y happy hacking.

 [1]: https://www.alevsk.com/2016/10/docker-101-1-introduccion-a-docker-y-los-contenedores/
 [2]: https://www.alevsk.com/?s=nginx
 [3]: https://www.alevsk.com/?s=html
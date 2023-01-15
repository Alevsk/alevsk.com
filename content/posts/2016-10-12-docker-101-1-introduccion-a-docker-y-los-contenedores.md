---
title: 'Docker 101 #1: Introducción a docker y los contenedores'
author: Alevsk
type: post
date: 2016-10-12T02:06:41+00:00
url: /2016/10/docker-101-1-introduccion-a-docker-y-los-contenedores/
categories:
  - cloud
  - Linux
  - Mac
  - Networking
  - Personal
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - cloud
  - containers
  - docker
  - iaas
  - Linux
  - nginx
  - shell

---
[![docker-image](/images/docker-image.png)](http://www.alevsk.com/2016/10/docker-101-1-introducciones-a-docker-y-los-contenedores/docker-image/)

Hola lectores, en los últimos 6 meses he tenido la oportunidad de estar desarrollando mi carrera en una de las empresas de tecnología más grandes que hay en **México**, he estado trabajando muy de cerca en temas de **Cloud computing**, **virtualizacion**, **bare metal** e **IaaS** en general.

Es por eso que he decidido que es una buena idea crear una serie de tutoriales sobre **docker**, herramienta que considero esencial para los desarrolladores hoy en día, sobre todo si te atrae el mundo del **cloud computing** :). Si no tienes conocimientos previos de **docker** no te preocupes, planeo escribir tutoriales desde cero y voy a ir explicando cosas un poco más complejas conforme vayamos avanzando.

## Un poco de teoria

Cuando hablamos de docker hablamos de contenedores. Pero ¿Que es un contenedor?, seguramente podrás encontrar una definición más formal de lo que es, pero imagínate que un contenedor es una caja que contiene tu solución de software, y no solo eso, también contiene las dependencias necesarias para ejecutar tu aplicación, las dependencias pueden ser librerías, configuraciones especiales e incluso otras aplicación o servicios que necesites (como un servidor web, nginx, apache, tomcat, etc.), todas las dependencias y aplicaciones dentro de una imagen están organizadas mediante un concepto de **layers** (capas), de esa manera cuando modificas un contenedor (una imagen) solo actualizas un **layer** en específico.

La gran ventaja de los contenedores es que, a diferencia de las máquinas virtuales estos no tienen asignadas cuotas específicas de recursos del sistema host (memoria, cpu, storage, etc), cuentan con un sistema de archivos virtual que permite que los contenedores se ejecuten de forma independiente y separada de los procesos del sistema, de esta manera la memoria de un proceso del contenedor no interfiere con un proceso de la maquina donde es ejecutado. 

Un contenedor solo incluye consigo la aplicación y sus dependencias lo que hace que las imágenes de **docker** sean bastante livianas.

Otro de los grandes beneficios que nos aportan los contenedores es la potabilidad, me refiero a que si tienes una aplicación y la quieres migrar a otro sistema (por ejemplo de desarrollo a producción) puedes creas una **imagen de docker** que incluya tu solución y ejecutarla en cualquier otro sistema teniendo la certeza de que va a “correr" pues la imagen contiene todas las dependencias necesarias. Existen técnicas para “comunicar" nuestra maquina host con los contenedores como el mapeo de puertos y directorios, eso lo veremos en los siguientes tutoriales.

## Conceptos básicos

  * **Docker:** Tecnología de software para creación y administración de contenedores.
  * **Docker image:** Un sistema de archivos virtual que puede contener aplicaciones y dependencias.
  * **Docker container:** Una imagen de docker que está siendo ejecutada, una instancia de una imagen.
  * **Dockerhub:** Un repositorio que contiene muchísimas imágenes de docker listas para ser descargadas.
  * **DockerFile:** Un script que indica una serie de pasos para construir una imagen de docker.

Bien suficiente teoría, si quieres saber más a fondo sobre docker pueden visitar el [sitio web](https://www.docker.com/) o ir a la [documentación oficial](https://docs.docker.com/)

## Instalar docker

Lo primero que debemos hacer es **instalar docker**, dependiendo de tu **sistema operativo** es el instalador que utilizaras, [descarga docker de la página oficial](https://www.docker.com/products/docker), si estas en Windows descarga el ejecutable y sigue el wizard (siguiente, siguiente, siguiente), en **Mac OSX** puedes descargar una **imagen dmg** y hacer lo mismo, en mi caso lo que tengo a la mano es un sistema **Linux**, **Ubuntu** para ser específico y para proceder con la instalacion lo hago de la siguiente forma:

```bash
$ sudo apt-get install docker.io
```

Sea cual sea tu sistema operativo, una vez hayas instalado **docker** para verificar que la herramienta está bien instalada abre una consola y escribe el comando **docker**

```bash
$ docker
```

[![docker1](/images/docker1.png)](http://www.alevsk.com/2016/10/docker-101-1-introducciones-a-docker-y-los-contenedores/docker1/)

Si el resultado es un output similar al de la imagen significa que instalaste **docker** correctamente, si por el contrario recibes algún mensaje que dice que el comando **docker** no existe esto se puede deber a varias razones pero principalmente si estas en **Windows** verifica que la ruta al binario de **docker** se encuentre definida en tus variables de entorno.

Docker contiene muchisimos comandos pero los más importantes, o al menos los que utilizaras más son:

  * $ docker run
  * $ docker images
  * $ docker build
  * $ docker pull
  * $ docker ps
  * $ docker start
  * $ docker stop
  * $ docker commit
  * $ docker attach

Conforme vayamos avanzando en los tutoriales iré explicando que hace cada uno de ellos

## Nuestro primer contenedor

Estamos listos para crear nuestro primer contenedor, abrimos una consola y escribimos el siguiente comando:

```bash
$ sudo docker run hello-world
```

El comando anterior le dice a docker que ejecute una nueva instancia (un contenedor) de la imagen **hello-world**, primero busca en el repositorio local y si no la encuentra va al dockerhub y procede a con la descarga.

[![docker2](/images/docker2.png)](http://www.alevsk.com/2016/10/docker-101-1-introducciones-a-docker-y-los-contenedores/docker2/)

¿Observas la parte que dice **Pull complete**?:

```bash
Unable to find image 'hello-world:latest' locally  
latest: Pulling from hello-world

264eca88cf85: Pull complete  
f0cb9bdcaa69: Pull complete  
Digest: sha256:548e9719abe62684ac7f01eea38cb5b0cf467cfe67c58b83fe87ba96674a4cdd  
Status: Downloaded newer image for hello-world:latest
```

Ahi es donde docker está mostrando el progreso de la descarga y los **layers** de la image, el resultado final de ejecutar este contenedor es el mensaje que dice: **Hello from Docker!**

```bash
Hello from Docker!  
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:  
1. The Docker client contacted the Docker daemon.  
2. The Docker daemon pulled the "hello-world" image from the Docker Hub.  
3. The Docker daemon created a new container from that image which runs the  
executable that produces the output you are currently reading.  
4. The Docker daemon streamed that output to the Docker client, which sent it  
to your terminal.

To try something more ambitious, you can run an Ubuntu container with:  
$ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker Hub account:  
https://hub.docker.com

For more examples and ideas, visit:  
https://docs.docker.com/engine/userguide/
```

Si ejecutamos el comando **docker images**, obtendremos una lista de las imágenes que tenemos disponibles localmente, y claro ahí tenemos nuestra **imagen hello-world**

```bash
$ docker images
```

[![docker3](/images/docker3.png)](http://www.alevsk.com/2016/10/docker-101-1-introducciones-a-docker-y-los-contenedores/docker3/)

Ahora veremos uno de los conceptos importantes de **docker**, el **sistema de archivos virtual**, vamos a descargar y ejecutar una **imagen docker de ubuntu** con el comando:

```bash
$ sudo docker run ubuntu
```

[![docker4](/images/docker4.png)](http://www.alevsk.com/2016/10/docker-101-1-introducciones-a-docker-y-los-contenedores/docker4/)

Corroboramos que tenemos una nueva imagen almacenada localmente:

```bash
alevsk@ubuntu:~$ sudo docker images  
REPOSITORY TAG IMAGE ID CREATED VIRTUAL SIZE  
ubuntu latest 426844ebf7f7 2 weeks ago 127.1 MB  
hello-world latest f0cb9bdcaa69 3 months ago 1.848 kB
```

Ya tenemos una imagen **docker de ubuntu**, ¿Pero cómo accedemos a ella? ¿Cómo la utilizamos?, podemos utilizar el siguiente comando para acceder al contenedor en tiempo de ejecución utilizando una shell interactiva:

```bash
$ sudo docker run -t -i ubuntu /bin/bash
```

Cuando el contenedor este corriendo podrás navegar su sistema de archivos como lo harías normalmente en Linux, incluso si estas corriendo docker desde una maquina con Windows podrás ver que el sistema de archivos es de Linux, aquí es donde puedes empezar a considerar la opción de dejar atrás [Cygwin](https://www.cygwin.com/) y comenzar a utilizar un **contenedor de ubuntu** con todas las herramientas que necesites.

[![docker5](/images/docker5.png)](http://www.alevsk.com/2016/10/docker-101-1-introducciones-a-docker-y-los-contenedores/docker5/)

_Para salir del contenedor utiliza el comando **exit**, como si terminaras una sesión remota de ssh._

Un punto importante a recalcar es que los contenedores no son persistentes, si creas un archivo dentro del contenedor la siguiente vez que lo ejecutes no existirá, posteriormente veremos cómo podemos solucionar eso. Por el momento quiero que entiendas los conceptos básicos de los contenedores en docker, como descargar imágenes y lanzarlas, los comandos básicos, etc.

Al inicio mencionaba el [dockerhub](https://hub.docker.com/explore/), el repositorio público de donde puedes descargar miles de imágenes de docker, te invito a explorarlo e instalar las que más te gusten:

[![docker6](/images/docker6.png)](http://www.alevsk.com/2016/10/docker-101-1-introducciones-a-docker-y-los-contenedores/docker6/)

## Servidor web nginx utilizando docker

Para terminar el tutorial mostrare rápidamente como podemos ejecutar un servidor web utilizando docker, como mencionaba, el dockerhub tiene miles de imágenes públicas y muchas comunidades de software libre están creando versiones “contenerizadas" de sus soluciones, en este caso el **servidor web nginx**, lo primero que debemos hacer es descargar la imagen de nginx para docker

```bash
$ sudo docker pull nginx
```

[![docker7](/images/docker7.png)](http://www.alevsk.com/2016/10/docker-101-1-introducciones-a-docker-y-los-contenedores/docker7/)

Ejecutamos docker images para verificar que se descargó correctamente:

```bash
alevsk@ubuntu:~$ sudo docker images  
REPOSITORY TAG IMAGE ID CREATED VIRTUAL SIZE  
ubuntu latest 426844ebf7f7 2 weeks ago 127.1 MB  
nginx latest 4c0e7e3661d2 2 weeks ago 181.4 MB  
hello-world latest f0cb9bdcaa69 3 months ago 1.848 kB
```

Ahora para lanzar el contenedor utilizaremos el comando:

```bash
$ sudo docker run –name nginx-server1 -p 80:80 nginx
```

[![docker8](/images/docker8.png)](http://www.alevsk.com/2016/10/docker-101-1-introducciones-a-docker-y-los-contenedores/docker8/)

  * El comando **docker run** especifica que queremos correr un contenedor
  * El parametro **–name** nos permite definir un nombre único y amigable para esa instancia
  * El parametro **-p** nos permite mapear puertos entre el sistema operativo y los servicios que corren dentro del contenedor
  * Al final especificamos el nombre de la imagen de la cual queremos crear el contenedor, **nginx** en este caso

[![docker9](/images/docker9.png)](http://www.alevsk.com/2016/10/docker-101-1-introducciones-a-docker-y-los-contenedores/docker9/)

Incluso podemos abrir una segunda terminal y ejecutar el siguiente comando para lanzar un segundo servidor web contenerizado pero en un puerto diferente:

```bash
$ sudo docker run –name nginx-server2 -p 8080:80 nginx
```

[![docker10](/images/docker10.png)](http://www.alevsk.com/2016/10/docker-101-1-introducciones-a-docker-y-los-contenedores/docker10/)

Al lanzar cada una de las imágenes de nginx habrás notado que la consola se queda “ocupada" corriendo el contenedor, en el siguiente tutorial mostrare como evitar eso, finalmente para detener la ejecución del contenedor presiona **ctrl+c**

Si ejecutas el comando **docker ps -a** podras ver todas los contenedores que hemos creado hasta el momento, la mayoria no estara en ejecucion y puede ser eliminado utilizando **docker rm [CONTAINER ID]**

[![docker11](/images/docker11.png)](http://www.alevsk.com/2016/10/docker-101-1-introducciones-a-docker-y-los-contenedores/docker11/)

Si haz entendido bien los **conceptos básicos** ya te imaginaras el potencial de docker y hacia donde iré en los siguientes tutoriales :).

Saludos y happy hacking.
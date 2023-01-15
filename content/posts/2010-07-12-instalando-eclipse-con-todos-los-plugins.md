---
title: Instalando Eclipse con todos los plugins
author: Alevsk
type: post
date: 2010-07-12T01:34:11+00:00
url: /2010/07/instalando-eclipse-con-todos-los-plugins/
image:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/eclipse.jpg
slider_thumbnail:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/thumb-eclipse.jpg
categories:
  - Programming
  - Technology
  - Tutorials
tags:
  - eclipse
  - plugins
  - Tutorials

---
**De la wikipedia:**

Eclipse es un entorno de desarrollo integrado de código abierto multi plataforma para desarrollar lo que el proyecto llama “Aplicaciones de Cliente Enriquecido", opuesto a las aplicaciones “Cliente-liviano" basadas en navegadores. Esta plataforma, típicamente ha sido usada para desarrollar entornos de desarrollo integrados (del inglés IDE), como el IDE de Java llamado Java Development Toolkit (JDT) y el compilador (ECJ) que se entrega como parte de Eclipse (y que son usados también para desarrollar el mismo Eclipse).

<!--more-->

Si usan Ubuntu como yo actualmente, pueden visitar el centro de software de ubuntu y escribiendo eclipse les aparece, nada mas de seleccionar instalar y ya lo tendrá, sin embargo no viene con los plugins y se los tendrían que poner aparte (que no es muy difícil pero bueno), sin embargo llega Easy Eclipse, es el mismo IDE pero ya vienen los plugins precargados, solo basta configurarlos.

**Paso 1**  
Se descargan el paquete de la siguiente dirección: http://www.easyeclipse.org/site/distributions/lamp.html

**Paso 2**  
Lo descomprimen y lo copian a /usr/lib/ con los siguientes comandos:

```Transact-SQL
tuusuario@tumaquina:~$  sudo tar  xvfz easyeclipse-lamp-1.2.2.2.tar.gz
```

y luego copiamos a la ruta mencionada anteriormente, le ponemos un nombre amigable a la carpeta

```Transact-SQL
tuusuario@tumaquina:~$  sudo cp -R easyeclipse-lamp-1.2.2.2 /usr/lib/eclipse
```

y ya con eso tendremos eclipse, ahora solo falta crear un lanzador, esto es muy rapido y sencillo.

**Paso 3**  
Podemos editar los menús (botón secundario en la esquina superior izquierda), nos aparecerá el Menú principal, vamos al apartado de programación y seleccionamos Elemento nuevo y lo configuramos como muestra la imagen.

<p style="text-align: center;">
[![Photobucket](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/Pantallazo.png)](http://s251.photobucket.com/albums/gg290/midgar156/alevsk-zone/?action=view¤t=Pantallazo.png)<br/> Clic en la imagen para ver en grande
</p>

Ya solo queda correr eclipse y nos preguntara donde queremos guardar nuestros proyectos por default van en /home/usuario/workplaces le decimos que si, de lo contrario elegimos otro path y iniciamos, ahora solo quedaría configurar los plugins, pero eso lo explico en el siguiente post

Espero les sea útil este tutorial, si tienen dudas y comentarios hacérmelo saber.

salu2
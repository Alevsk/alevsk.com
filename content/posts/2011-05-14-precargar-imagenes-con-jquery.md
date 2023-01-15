---
title: Precargar imagenes con Jquery
author: Alevsk
type: post
date: 2011-05-14T05:11:32+00:00
url: /2011/05/precargar-imagenes-con-jquery/
categories:
  - CSS
  - HTML
  - Javascript
  - Jquery
tags:
  - Linux Debugging
  - debian
  - distros
  - Javascript
  - Jquery
  - photoshop
  - Tutorials
  - ubuntu
  - web

---
[![](/images/jquery-javascript-library.jpg)](http://www.alevsk.com/2011/05/precargar-imagenes-con-jquery/jquery-javascript-library/)  
Hoy en día para los desarrolladores **web**, con el uso cada vez mas intenso de las tecnologías como **ajax** que hacen capaz posible que una **aplicación web** se asemeje cada vez mas a una aplicación de escritorio, nos es necesario encontrar una manera en la que nuestras aplicaciones no se saturen con peticiones http al servidor tratando de cargar la gran cantidad de recursos (imágenes, etc) que son tan habituales hoy en día.

Este es un truco bastante sencillo que nos asegura que las imágenes que utilicemos en nuestro sitio web estaran completamente cargadas una vez que las necesitemos :).

Obviamente primero carga la librería de Jquery y después puedes escribir un código como este

```GDScript
var image1 = $('![](None)').attr('src', 'imageURL.jpg');

```

puedes escribir tantas variables como imágenes quieras tener cargadas :), lo que Jquery realiza con el código anterior es la creación y la carga de los elementos del **DOM** que le pasemos, en este caso imágenes, es realmente muy sencillo de implementar y nos asegura que los recursos estarán ahí cuando los necesitemos 🙂

Después de eso lo que podemos hacer es insertar la imagen una vez cargada, el código seria el mas o menos el siguiente

```GDScript
var image1 = $('![](None)').attr('src', 'imageURL.jpg');

// Insertar la imagen precargada
$('.profile').append(image1);
// o
image1.appendTo('.profile')

```

salu2
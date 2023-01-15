---
title: Agregar boton de facebook y twitter
author: Alevsk
type: post
date: 2011-06-25T05:18:49+00:00
url: /2011/06/agregar-boton-de-facebook-y-twitter/
categories:
  - CSS
  - Diseño
  - HTML
  - Javascript
  - Jquery
  - Programming
  - Snippets
  - Tips
  - Tutorials
tags:
  - facebook
  - Linux
  - Programming
  - Social Media
  - Solutions
  - Tutorials
  - twitter
  - ubuntu
  - web

---
[![](/images/twitter_facebook.jpg)](http://www.alevsk.com/2011/06/agregar-boton-de-facebook-y-twitter/twitter_facebook/)  
Existen bastantes plugins que nos permiten dar a nuestros blogs interacción con las r**edes sociales** (**facebook**, **twitter**, **linkedin**, **youtube**, etc) sin embargo hay veces en las que estamos desarrollando un proyecto propio y no queremos agregar código innecesario (solo queremos un botón y ya).

Es muy sencillo, **facebook** nos permite colocar un botón de **like** en nuestro desarrollo por medio de un **iframe** de la siguiente manera

Yo he puesto algunos datos de ejemplo en cada atributo, por ejemplo zonau.com.mx en **href**

```Text only

```



Descripción de cada atributo:

  * href – Direccion URL a compartir.
  * layout – Estilo del botón. Valores: standard o button_count
  * show_faces – Muestra o no el avatar de quienes del gusta la anotación. Valores: true o false.
  * width – Ancho del iframe.
  * height – Alto del iframe.
  * action – Texto del botón. Valores like o recommend.
  * font – Fuente a utilizar.
  * colorscheme – Esquema de colores. Valores: light, dark o evil.

Para agregar el botón de **twitter** es mucho mas sencillo (como si el de facebook fuera muy complicado jaja), tan solo agregar la siguiente línea.

```Transact-SQL
[Tweet](http://twitter.com/share)

```
[Tweet](http://twitter.com/share)

salu2
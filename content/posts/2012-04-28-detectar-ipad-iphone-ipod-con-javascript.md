---
title: Detectar iPad – iPhone – iPod con Javascript
author: Alevsk
type: post
date: 2012-04-28T00:00:10+00:00
url: /2012/04/detectar-ipad-iphone-ipod-con-javascript/
categories:
  - HTML
  - Javascript
  - Jquery
  - Snippets
  - Tips
  - Tutorials
tags:
  - Javascript
  - Jquery
  - php
  - Programming
  - software libre
  - Solutions
  - Technology
  - Tutorials
  - web

---
[![](/images/ipads.png)](http://www.alevsk.com/2012/04/detectar-ipad-iphone-ipod-con-javascript/ipads/)  
Muchas de las personas que desarrollan sitios web seguramente se habrán topado ya con la famosa pregunta “¿y mi sitio se va a poder ver bien desde el [Nuevo iPad][1]?". Existen varias soluciones para esto, si por ejemplo utilizamos algún CMS como **wordpress** o **Joomla** existen bastantes plugins que nos permitirán adaptar nuestros sitios para que puedan ser leídos comodamente en estos dispositivos, algunos de los que me vienen a la mente son **WPtouch**, **WordPress PDA & iPhon**, etc.

Sin embargo si somos de esos desarrolladores mas “artesanales" y nos gusta hacer los trabajos desde 0 tenemos que implementar esas detecciones a mano, en realidad no es tan difícil, se requiere un poco de paciencia mas que nada para desarrollar una buena hoja de estilos, lo demás es bastante fácil.

Basta con colocar un pequeño código **javascript**, por ejemplo:

```Tera Term macro
if((navigator.userAgent.match(/iPhone/i)) || (navigator.userAgent.match(/iPod/i)) || (navigator.userAgent.match(/iPad/i))) 
{
      //El usuario esta utilizando un iPhone, iPad o iPad para visualizar el sitio web
      //Cargar la respectiva hoja de estilos
}
else
{
     //Nos visitan desde un navegador tradicional
     //cargamos la hoja de estilos por defecto :)
}

```

La funcionalidad de esa condición es bastante sencilla, si el navegador con el que nos visitan tiene en su estructura **iPhone**, **iPod** o **iPad**, lo mas seguro es que nos estén visitando desde uno de esos dispositivos, esta validación se puede realizar también desde [PHP][2], sin embargo yo la prefiero hacer del lado del cliente para aligerar algo de carga al servidor.

salu2

 [1]: http://www.ipadizate.es/tag/ipad-3 "Nuevo iPad"
 [2]: http://www.alevsk.com/tag/php/
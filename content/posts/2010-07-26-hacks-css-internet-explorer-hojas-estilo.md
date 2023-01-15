---
title: Hacks CSS para Internet Explorer
author: Alevsk
type: post
date: 2010-07-26T01:46:08+00:00
url: /2010/07/hacks-css-internet-explorer-hojas-estilo/
slider_thumbnail:
  - /images/2010/07/firefox-internet-explorer-150x150.jpg
categories:
  - CSS
  - HTML
  - Programming
  - Tips
  - Tutorials
tags:
  - CSS
  - estandares
  - firefox
  - hacks
  - internet explorer
  - navegadores

---
![](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/internet_explorer_vs_mozilla_by_letitbeatles.png)

Bueno ayer sabado dure un buen rato quebrándome la cabeza con un modulo de joomla, el llamado fbtoolbar, si ese que nos hace posible mostrar una barra como la de facebook en nuestro portal, mi jefe JC me había dicho que el modulo funcionaba bien en todos los navegadores excepto en Internet Explorer y dije ptm U.U tengo que cambiarme a windows, claro que se puede ejecutar con wine o incluso instalar la alternativa de IE4Linux pero no es lo mismo :s, ya inicio sesión en windows, entro al portal y efectivamente veo que la barra esta desfasada :S no como se debiera ver normalmente, pensando que era algun problema de incompatibilidad de librerías javascript (mootools y jquery y de mas que usa el portal) me puse a desactivar todos los modulos y activarlos de uno por uno, tarde mucho haciendo eso -.-" al final supe que era problema de como internet explorer interpretaba las hojas de estilo, entonces me puse a investigar para aplicar algunos hacks y pues bueno es muy fácil de aprender a continuación les pongo algunos ejemplos.

### Detectando la versión de Internet Explorer

Para detectar la versión que está utilizando nuestro visitante, de este navegador, debemos usar los llamados **comentarios condicionales**.

Estos fueron creados por [Microsoft][1] para su navegador y sólo son soportados por éste. Como comienzan con `<!--` cualquier otro [navegador][2] asumirá que es un comentario y no ejecutará el código que hay dentro.

Este tipo de hack se sitúa entre las etiquetas `<strong><head>` y `<strong></strong></head>`. Utilizándolo podremos detectar la versión del navegador y cargar el archivo CSS necesario.

![](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/condicional-ie.jpg) 

Ami en lo personal no me sirvieron :S, talvez no los supe aplicar, otra de las maneras que ami si me funciono fue el uso de la dobe // este hack se aplica de la siguiente manera:

### Usando doble //

```CSS+Lasso
#nonie, #iebased{
    margin: auto;
    margin-top: 20px;
    width: 400px;
    padding: 10px;
    background-color: #f8e6e6;
    border: 1px solid #d2a2a2;
    //background-color: #dbecd3;
    //border: 1px solid #b1d2a2;
    }

    #nonie{
    //display: none;
    }

    #iebased{
    display: none;
    //display: visible;
    }

```

Analizemos las siguientes lineas para empezar

```CSS+Lasso
background-color: #f8e6e6;
    border: 1px solid #d2a2a2;
    //background-color: #dbecd3;
    //border: 1px solid #b1d2a2;

```

El truco consiste en que firefox por ejemplo omite el código css que sigue de **//** mientras que Internet Explorer lo ejecuta entonces firefox tomara el color #f8e6e6 como parámetro del background-color mientras que Internet Explorer al si ejecutar las sentencias que siguen de **//** actualizara ese parámetro por #dbecd3 🙂

Esto no solo se aplica a los colores se puede aplicar a cualquier propiedad incluso estoy casi seguro (no lo he intentado) que a una clase entera o a un identificador, siempre y cuando se encuentren en una sola linea claro 😉

### Usando el guion bajo _

Este hack en especial funciona solo para la versión 6 de IE e inferiores por lo que ya esta descontinuado su uso.

Teniendo en cuenta que los navegadores sobrescriben las propiedades si estas se definen mas de una vez por ejemplo:

```CSS+Lasso
#box
{
    width:600px;
    width:900px;
}

```

El resultado era el div#box de 900px de ancho y no de 600 por que el valor de la propiedad fue sobrescrito al definirse 2 veces y siempre lo que le importa al navegador es el ultimo valor dado xD.

```CSS+Lasso
#textbox{
  width: 450px;		/* Firefox y los demás */
  _width:400px;		/* Internet Explorer 6 e inferiores */
}

```

Para el resto de los navegadores una propiedad con un guión bajo, u otro carácter alfanumérico delante es algo que no existe, y por tanto no la interpretan, pero Internet Explorer las asimila sin problemas. Esto es algo que podemos utilizar para definir propiedades en los estilos, destinadas sólo a este navegador.

### El uso de !important

Este operador es utilizado en los archivos CSS para que los navegadores respeten la importancia de la propiedad que lo contenga y evite que se sobrescriba con otras que se definan posteriormente.

Internet Explorer 6 y las versiones anteriores no interpretan este operador; problema que fue solucionado en la versión 7 de este navegador.

```CSS+Lasso
p {
background: green !important; /* Navegadores superiores a IE 6 respetarán la importancia inmediatamente */
background: red; /* IE 6 y anteriores aplicará este estilo aunque esté marcado la anterior como importante */
}

```

### Sin hacks en nuestros CSS

Luego de seguir investigando encontré que también existe una libreri a javascript que hace que Internet explorer se comporte como un navegador que sigue estándares de hojas de estilo, Para utilizar esta librería debemos descargarla de [Google Code][3] y seguidamente agregar estas líneas entre las etiquetas :

![](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/google_code.jpg) 

### Ejemplo practico

A continuación esta un ejemplo practico de lo que aprendimos en este articulo, asi como el código fuente para que lo descarguen

<div class="demobox">
[![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/download.png)](http://www.megaupload.com/?d=G0CK3QZ8) [![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/demo.png)](http://alevsk.frexa.com.ar/hacks_css/)
</div>

**Y uds amigos lectores tienen algunos otros hacks css que quisieran compartir? favor de hacerlo en los comentarios**

**salu2**

 [1]: http://www.maestrosdelweb.com/editorial/microsoft/
 [2]: http://www.maestrosdelweb.com/editorial/%C2%BFcomo-elegir-un-navegador-web/
 [3]: http://code.google.com/p/ie7-js/downloads/list
---
title: Agregar Favicon en WordPress
author: Alevsk
type: post
date: 2010-07-12T03:36:16+00:00
url: /2010/07/agregar-favicon-en-wordpress/
image:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/icon_finder.jpg
slider_thumbnail:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/wordpress.jpg
categories:
  - Tips
  - Tutorials
tags:
  - codigo
  - favicon
  - wordpress

---
El favicon es esa imagen pequeña que aparece en la pestaña de una pagina web, también es una característica principal de la web 2.0 y de alguna u otra forma sirve para hacerle familiar el sitio al internauta, seguramente los que aun no hayan tenido el suyo se han preguntado como ponérselo a su web, en este caso a su blog de wordpress, pues es muy fácil a continuación en 3 sencillos pasos tendrán el suyo.

**Paso 1**  
Los primero que tienen que hacer es buscarse un buen favicon de 16 x 16 si es posible (ya que sera redimencionado a ese tamaña y es mejor que no se deforme) 

<!--more-->

o pueden hacerse el suyo propio, sino les recomiendo esta pagina en donde pueden encontrar muchos iconos de diferentes dimensiones: http://www.iconfinder.com/

**Paso 2**  
Una vez que tengan su favicon subando por ftp a la carpeta del theme actual que esten usando en wordpress, tiene que ir en la siguiente ruta **/wordpress/wp-content/themes/Themeactual/** como se muestra en la siguiente imagen.

![Photobucket](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/screenshot1.png) 

**Paso 3**  
Modificamos el archivo header.php ya sea por el gestor que trae wordpress (Apariencia > Editor > header.php) o directamente por el ftp. agregamos la siguiente linea 

```Text only




```

Justo despues de la etiqueta 

<head>
  , de tal forma que quede así:
<p>
![Photobucket](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/screenshot2.png)
</p>
<p>
    Listo ya con eso solo queda borrar la cache, salir del navegador y volver a entrar y ya tendremos el favicon xD
  </p>
<p>
    salu2
  </p></head>
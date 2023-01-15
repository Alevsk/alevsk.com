---
title: Juegos en la nube utilizando Dropbox
author: Alevsk
type: post
date: 2013-12-21T10:00:33+00:00
url: /2013/12/juegos-en-la-nube-utilizando-dropbox/
categories:
  - Geek
  - Linux
  - Mac
  - Personal
  - Tips
  - Tutorials
tags:
  - Linux
  - mac
  - Personal
  - Solutions
  - Technology
  - Tutorials
  - web

---
[![blog-11](/images/blog-11.jpg)](http://www.alevsk.com/2013/12/juegos-en-la-nube-utilizando-dropbox/blog-11/)

Hace 10-12 años nadie hubiera imaginado que podríamos comenzar a escribir un documento en nuestra computadora personal, guardarlo, y luego continuar en la computadora de la oficina, todo de forma totalmente automática. El concepto de almacenamiento en la nube era algo muy nuevo que apenas se estaba desarrollando, reservado únicamente para grandes compañías, universidades e instituciones del gobierno. Afortunadamente hoy en día el almacenamiento de archivos en la nube es ya una realidad, muchas compañías como **Dropbox** o **Microsoft** (Skydrive) han sido lo bastante flexibles como para permitir que cualquier persona tenga la oportunidad de utilizar sus servicios y disponer de sus archivos en cualquier lugar y en cualquier momento y de manera gratuita.

Hoy en día la industria de los videojuegos ha evolucionado bastante, plataformas como **Steam** y **Origin** nos permiten utilizar nuestros juegos en cualquier computadora, guardar nuestro progreso y continuar justo donde nos quedamos en cualquier otra computadora que tenga el cliente instalado, todo esto haciendo uso del almacenamiento en la nube :), por supuesto hoy en día solo los juegos más modernos tienen incluida esta característica, pero ¿qué pasa con los juegos viejos que no tienen esta funcionalidad implementada?, en lo personal es bastante molesto empezar una historia (si nuestro juego es de historias, etc) en la computadora que llevamos a la universidad, y al regresar a nuestra casa utilizar la computadora de escritorio y darnos cuenta que tenemos que jugar de nuevo la historia. Es aqui donde entran a nuestro rescate servicios gratuitos como **Dropbox** :).

Para que un videojuego utilice el “almacenamiento en la nube" en lugar del almacenamiento local tenemos que hacer básicamente 2 cosas.

<div class="demobox">
<ul>
<li>
      Encontrar la carpeta donde el juego almacena nuestro progreso
    </li>
<li>
      Engañar de alguna manera al juego para que utilice nuestra carpeta de dropbox
    </li>
</ul>
</div>

El primer punto requiere un poco de investigación, muchas veces en las **FAQ** o en foros se indican cuáles son las carpetas que el juego utiliza para almacenar los avances, siempre podemos dar una revisada a los archivos del juego y tratar de entender cómo se comporta y utilizar google para obtener esta información. El segundo punto es bastante interesa y se puede realizar de varias formas, podemos complicar tanto esta parte como queramos, desde hacer ingeniería inversa al juego y forzar para que escriba directamente en la carpeta que queramos, utilizar **enlaces simbólicos** para “engañarlo" o cambiar la ruta por defecto si el juego nos lo permite :).

Para este ejemplo utilizare un videojuego (novela visual) llamada **[Katawa Shoujo][1]**, es un buen ejemplo puesto que el juego es multiplataforma (Windows, Linux y MAC OSX), asumiendo que tienen instalado **Dropbox** en todas las maquinas donde tendrán sus partidas sincronizadas comenzamos.

Primero tenemos que crear una carpeta en dropbox donde se almacenaran y sincronizaran nuestros datos para el juego

[![ks_dropbox](/images/ks_dropbox.jpg)](http://www.alevsk.com/2013/12/juegos-en-la-nube-utilizando-dropbox/ks_dropbox/)

Como se ve en la imagen la carpeta se llama Renpy, respetando el nombre original, si tenemos progreso local de una vez copiarlo manualmente para que se vaya sincronizando con la nube de dropbox, las rutas de dropbox tanto en windows como en mac quedaron de la siguiente forma

<div class="demobox">
<ul>
<li>
<strong>Mac OS X:</strong> /Users/alevsk/Dropbox/games/katawa_shoujo/RenPy
    </li>
<li>
<strong>Windows 8:</strong> C:\Users\Alevskey\Dropbox\games\katawa_shoujo\RenPy
    </li>
</ul>
</div>

Es importante guardar estas rutas en algún lado ya que más adelante las necesitaremos. Ahora, como mencionaba anteriormente tenemos que conocer es el directorio en donde **Katawa Shoujo** guarda el progreso de los jugadores, así que vamos a buscar esa información en el foro oficial del juego y en menos de 5 minutos encontramos que los directorios son:

<div class="demobox">
<ul>
<li>
<strong>Mac OS X:</strong> /Users/usuario/Library/RenPy
    </li>
<li>
<strong>Windows 8:</strong> C:\Users\usuario\AppData\Roaming\RenPy
    </li>
</ul>
</div>

Bien, ahora tenemos que engañar al programa, como el juego no nos da la libertad de modificar la ruta del directorio donde guarda los progresos y hacerle ingeniería inversa seria tardado optamos por crear enlaces simbólicos, tanto en **Windows** como en sistemas basados en **Unix** esto es muy sencillo de realizar.

En **Mac OSX** lo que tendríamos que hacer seria abrir nuestra terminal y escribir los siguiente comandos

```bash
# Nos movemos al directorio donde está la carpeta Renpy  
$ cd /Users/usuario/Library  
# Si no hiciste un respaldo de tu avance con anterioridad ahora es un buen momento, ya que el siguiente comando borrara la carpeta Renpy  
$ rm -rf Renpy  
# Ahora creamos un enlace simbólico llamado Renpy que apunta a nuestra carpeta sincronizada en dropbox  
$ ln -s /Users/usuario/Dropbox/games/katawa_shoujo/RenPy RenPy
```

Listo terminamos con la versión **Mac** de KS, ahora vamos a **Windows** y hacemos lo mismo, los enlaces simbólicos son creados desde la consola (**CMD**) utilizando el comando **mklink**.

```bash
# Nos movemos al directorio donde está la carpeta Renpy  
> cd C:\Users\usuario\AppData\Roaming  
# Si no hiciste un respaldo de tu avance con anterioridad ahora es un buen momento, ya que el siguiente comando borrara la carpeta Renpy  
> rmdir RenPy /s /q  
# Ahora creamos un enlace simbólico llamado Renpy que apunta a nuestra carpeta sincronizada en dropbox  
> mklink /D RenPy C:\Users\usuario\Dropbox\games\katawa_shoujo\RenPy
```

Y listo con esto Katawa Shoujo ya utiliza la nube, ahora podemos tener sincronizado nuestro progreso de manera automática en todas nuestras computadoras :).

<div class="wp-caption aligncenter" id="attachment_2996" style="width: 610px">
[![Avance guardado en Windows](/images/ks_windows.jpg)](http://www.alevsk.com/2013/12/juegos-en-la-nube-utilizando-dropbox/ks_windows/)
<p class="wp-caption-text" id="caption-attachment-2996">
    Avance guardado en Windows
  </p>
</div>
<div class="wp-caption aligncenter" id="attachment_2998" style="width: 610px">
[![Avance del juego guardado en Mac](/images/ks_mac.jpg)](http://www.alevsk.com/2013/12/juegos-en-la-nube-utilizando-dropbox/ks_mac/)
<p class="wp-caption-text" id="caption-attachment-2998">
    Avance del juego guardado en Mac
  </p>
</div>

Siguiente estos sencillos pasos podemos tener la mayoría de nuestros juegos no tan modernos utilizando la nube en un abrir y cerrar de ojos, con esto quiero que se den cuenta que dropbox no está solo limitado a sincronizar documentos de ofimática, las posibilidades son infinitas :).

 [1]: http://www.katawa-shoujo.com/
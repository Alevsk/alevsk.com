---
title: Como colocar Google Maps en mi sitio web
author: Alevsk
type: post
date: 2011-06-26T00:23:44+00:00
url: /2011/06/como-colocar-google-maps-en-mi-sitio-web/
categories:
  - Diseño
  - Javascript
  - Jquery
  - Programming
  - Snippets
  - Technology
  - Tips
  - Tutorials
tags:
  - Google
  - Programming
  - software libre
  - Solutions
  - Tutorials
  - ubuntu
  - web

---
  
  
[![](/images/6a00d8341c630a53ef0120a921559d970b-800wi.jpg)](http://www.alevsk.com/2011/06/como-colocar-google-maps-en-mi-sitio-web/6a00d8341c630a53ef0120a921559d970b-800wi/)  
**Google Maps** es sin duda una tecnología muy utilizada hoy en día y es posible que cualquier persona pueda hacer uso de ella en una **aplicación** **web** por ejemplo, su implementación es bastante sencilla y es completamente configurable, a continuación les enseñare brevemente como podemos insertar un **mapa** con una coordenada y un icono pre configurado.

Lo primero que tenemos que hacer es mandar llamar la **librería**

```Text only

```

Después preparamos nuestro código:

```GDScript
jQuery(document).ready(function() {
      var mapCenter = new google.maps.LatLng(19.69950000000000000000,-101.20028000000000000000);
			var myOptions = {
				zoom: 16,
				center: mapCenter,
				mapTypeId: google.maps.MapTypeId.ROADMAP
			}
			activeMap = new google.maps.Map(document.getElementById("div_map"), myOptions);
			var devLocation = new google.maps.LatLng(19.69950000000000000000, -101.20028000000000000000);
			var image2 = 'http://preview.zonau.com.mx/img/marker_venta.png';
			var marker = new google.maps.Marker({
				position: devLocation,
				map: activeMap,
				title:"",
				icon: image2
			});
});

```

Tranquilos que ahora explicare que hace cada cosa 🙂

```GDScript
var mapCenter = new google.maps.LatLng(19.69950000000000000000,-101.20028000000000000000);

```

con el metodo **new google.maps.LatLng();** le damos las coordenadas en las que comenzara la vista del mapa, guardamos los datos en la variable mapCenter.

Vayan a la seccion de Mapa (la pestaña de mapa junto a la de video, plano e imagen).

Después de eso, para inicializar el mapa creamos el objeto Map Options que tendrá las configuraciones iniciales.

```GDScript
var myOptions = {
				zoom: 16,
				center: mapCenter,
				mapTypeId: google.maps.MapTypeId.ROADMAP
			}

```

  * zoom: especifica el nivel de zoom con que se iniciara, entre mas zoom mas cerca.
  * center: indica la coordenada inicial que previamente definimos
  * mapTypeId: el tipo de mapa que utilizaremos, se aceptan los siguientes parámetros:

  * **ROADMAP**, que muestra los mosaicos normales en 2D predeterminados de Google Maps.
  * **SATELLITE**, que muestra imágenes de satélite.
  * **HYBRID**, que muestra una mezcla de mosaicos fotográficos y una capa de mosaicos para los elementos del mapa más destacados (carreteras, nombres de ciudades, etc.).
  * **TERRAIN**, que muestra mosaicos de relieve físico para indicar las elevaciones del terreno y las fuentes de agua (montañas, ríos, etc.).

Ya inicializado después tenemos que indicar el contenedor del mapa, en este casi un div con id **div_map** y le pasamos como parámetro el objeto de inicializacion **myOptions**

```Text only
activeMap = new google.maps.Map(document.getElementById("div_map"), myOptions);

```

Ahora ya con esto nuestro **Mapa** esta funcionando, pero no nos conformamos con eso x'D, crearemos un **marcador** 🙂

```GDScript
var devLocation = new google.maps.LatLng(19.69950000000000000000, -101.20028000000000000000);
			var image2 = 'http://preview.zonau.com.mx/img/marker_venta.png';
			var marker = new google.maps.Marker({
				position: devLocation,
				map: activeMap,
				title:"",
				icon: image2
			});

```

De la misma manera creamos una nueva coordenada y las almacenamos en devLocation después de image2 cargamos una imagen que será el icono de nuestro **marcador** y por ultimo creamos el objeto pasándole como parámetro los atributos position (la posición devLocation que indicamos), map (nuestro mapa! el ActiveMap), title (un titulo para el marcador), icon (el recurso, image2).

Esta es una buena manera de complementar información haciendo uso de **ubicaciones geográficas** :), sin embargo cuando son muchísimos los datos que tenemos que marcar en un mapa no lo aremos manualmente, entonces tenemos que hacer uso de una tecnología para mandar los datos, como por ejemplo **JSON** o **XML** (en mi proyecto [Zonau – U][1] hago uso de JSON y varias otras cosas).  
**  
Google Maps** también nos permite cargar **layers** en nuestro **Mapa** por medio de código **KML**, pero eso será para un post futuro 🙂

<div id="div_map" style="width:600px;height:400px;margin:0 auto;">
</div>
<div class="demobox" style="margin-top:10px;">
[![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/demo.png)](http://zonau.com.mx/inmueble/5761)
</div>

[Demo][2], vayan a la seccion Mapa (la tab de mapa junto a la de video, plano e imagen).

 [1]: http://preview.zonau.com.mx
 [2]: http://zonau.com.mx/desarrollo/168/LO-NUEVO-DE-ALTOZANO
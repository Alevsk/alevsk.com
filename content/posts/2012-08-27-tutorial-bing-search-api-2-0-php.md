---
title: Tutorial Bing Search API 2.0 y PHP
author: Alevsk
type: post
date: 2012-08-27T20:28:59+00:00
url: /2012/08/tutorial-bing-search-api-2-0-php/
categories:
  - HTML
  - Jquery
  - Programming
  - Tips
  - Tutorials
tags:
  - CSS
  - Java
  - Javascript
  - Jquery
  - Programming
  - Solutions
  - Technology
  - Tutorials
  - web

---
Ha inicios del mes de agosto la gente de Microsoft mejoro (por no decir que modifico) la forma en que los desarrolladores interactuaban con la api, mejor conocida como **bing api 2.0** ahora. Esto lógicamente causo bastantes problemas a las empresas y programadores independientes que no realizaron adoptaron los cambios en sus aplicaciones rápidamente, la mayor novedad que nos presenta ahora la **api** es que trabaja directamente con **Windows Azure Marketplace**.

Muchas personas pensaran que modificar sus aplicaciones para que vuelvan a funcionar va a ser una tarea muy tediosa, pero de hecho es bastante sencillo, a continuación he escrito una serie de pasos que te permitirá **migrar una aplicación a bing api 2.0**, mas concretamente utilizaremos la **Bing search api 2.0**

  * [Registrarte][1] en el Windows Azure Marketplace (usando tu cuenta de hotmail es suficiente)
  * Una vez registrado puedes acceder a la sección de datos del marketplace donde además de Bing Search Api (que es el servicio que utilizaremos en este tutorial) también podrás hacer uso de otros servicios como **Microsoft Translator**, etc. [Lista de servicios de Bing][2]

[![](/images/bing_apis.png)](http://www.alevsk.com/2012/08/tutorial-bing-search-api-2-0-php/bing_apis/)

  * Al hacer clic en el servicio serás enviado a una vista donde se proporciona mas información acerca de la api así como una lista de precios por utilizar la api mensualmente, si crees que tu aplicación no tendrá mas de 5000 peticiones por mes a la api podrías utilizar el paquete gratuito al servicio (el ultimo precio que se muestra) de lo contrario te recomiendo adquirir algún otro paquete con las transacciones por mes que mas se ajusten a tus necesidades
  * Una vez suscrito al paquete de tu preferencia (hacer clic, aceptar términos, etc, etc.) en la sección de [claves de cuenta][3] podrás encontrar la **key** necesaria para poder conectarte al servicio y empezar a hacer uso de el. Así mismo en la sección de [Mis datos][4] encontraras un resumen de las aplicaciones que estas utilizando actualmente y el estado del numero de consultas restantes por mes, etc.

[![](/images/bing_consultas.png)](http://www.alevsk.com/2012/08/tutorial-bing-search-api-2-0-php/bing_consultas/)

Listo eso es todo lo que tienes que configurar para comenzar a hacer uso de la api de bing :), ahora para no dejar el articulo a medias les dejo un pequeño código en **PHP** que nos regresa los resultados encontrados de la query que le pasemos a la api.

```php
<?php

$api = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/v1/Web?$format=json&$top=8&Query=';  
$accountKey = "LA KEY QUE APARECE EN LA SECCION DE CLAVES DE CUENTA";  
$context = stream\_context\_create(array(  
'http' => array(  
'request_fulluri' => true,  
'header' => "Authorization: Basic " . base64_encode($accountKey . ":" . $accountKey)  
)  
));

$query = 'alevsk';  
$request = $api . '%27'.$query.'%27′;

$jsonResponse = json\_decode(file\_get_contents($request, 0, $context));  
print_r($jsonResponse);

?>
```

El código es bastante sencillo pero creo que deja bastante claro cuales son los requerimientos mínimos para interactuar con la api como la autentificación, los sources y el formato de respuesta, si tienes mas dudas acerca de los parámetros que recibe la api puedes utilizar el [generador de consultas][5] que proporciona el sitio o también acceder a el utilizando el enlace de “Usar" (el que esta a la derecha en la imagen anterior).

[![](/images/consultas_bing.png)](/images/consultas_bing.png)

El **generador de consultas de bing api 2.0** se trata de una herramienta bastante útil ya que te permite configurar tus request de una manera muy amigable y al final en la parte superior te muestra como quedaría la petición (la URL) que deberías de hacer a la api para obtener los resultados mostrados abajo :).

Muy importante, aquí les dejo la [documentacion completa de la api][6] que podrán utilizar como referencia.

Con esto espero que haya quedado claro o por lo menos entendible la nueva manera de interactuar con la api de bing y como siempre digo, si hay dudas respecto al código pueden escribirlas en los comentarios y con gusto las resolveré.

salu2

 [1]: https://datamarket.azure.com/
 [2]: https://datamarket.azure.com/browse/Data
 [3]: https://datamarket.azure.com/account/keys
 [4]: https://datamarket.azure.com/account/datasets
 [5]: https://datamarket.azure.com/dataset/explore/5ba839f1-12ce-4cce-bf57-a49d98d29a44
 [6]: http://www.bing.com/community/site_blogs/b/developer/archive/2010/03/12/bing-api-version-2-documentation-available-for-download.aspx
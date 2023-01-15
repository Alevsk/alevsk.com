---
title: Jquery formato de Precio
author: Alevsk
type: post
date: 2011-06-25T22:46:35+00:00
url: /2011/06/jquery-formato-de-precio/
categories:
  - Javascript
  - Jquery
  - Programming
  - Snippets
tags:
  - Javascript
  - Jquery
  - Programming
  - Solutions

---
  
  
[![](/images/jquery_code.jpg)](http://www.alevsk.com/2011/06/jquery-formato-de-precio/jquery_code/)

Existe un plugin para [JQuery][1] llamado [jquery-formatcurrency][2] que te nos permite dar **formato de precio** a nuestras cifras numéricas, una gran ayuda en cuando a estética en nuestro sitio web.

Utilizar el **plugin** es realmente sencillo, primero tenemos que hacer la llamada en nuestro archivo, después de a ver cargado la librería de javascript Jquery.

```Text only

```

Y después dentro del 

```Text only
$(document).ready(function(){ });
```

tan solo utilizar el método 

```Text only
formatCurrency()
```

el código quedaría de la siguiente manera:

```Text only
$(document).ready(function(){
          $('#precio').formatCurrency();
});

```

Ejemplo  
Tenemos el texto original:  
**<span>1000000</span>** y ahora aplicándole **formatcurrency()** quedaria **<span id="precio">1000000</span>**

salu2

 [1]: http://www.alevsk.com/category/jquery/
 [2]: http://www.alevsk.com/2011/06/jquery-formato-de-precio/
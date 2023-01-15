---
title: Comentario tipo facebook utilizando jQuery
author: Alevsk
type: post
date: 2013-12-22T14:00:51+00:00
url: /2013/12/comentario-tipo-facebook-utilizando-jquery/
categories:
  - CSS
  - HTML
  - Javascript
  - Jquery
  - Programming
  - Snippets
  - Technology
  - Tips
  - Tutorials
tags:
  - CSS
  - php
  - Social Media
  - software libre
  - Solutions
  - Technology
  - Tutorials
  - web

---
Muchas veces mientras desarrollamos una aplicación web nos vemos en la necesidad de implementar algo que permita a los usuarios involucrarse en lo que sea que estemos haciendo, los sistemas de comentarios son una parte muy común en toda plataforma web de hoy en día, se trata de una de las características principales que no pueden faltar en ningún sitio, blog o red de noticias, básicamente un sistema de comentarios abre un canal de comunicación entre nosotros y los visitantes. Teniendo esto en cuenta no está de más mencionar que existen muchos servicios gratuitos en la red que nos permiten implementar un **sistema de comentarios** de forma muy rápida como por ejemplo [Disqus](http://disqus.com/).

En principio lo mínimo que tiene que tener un sistema de comentarios es un nombre de quien comenta, avatar y texto del comentario, entonces siguiendo este principio básico hoy vamos a implementar una interfaz de sistema de **comentarios tipo Facebook** utilizando **HTML** y **jQuery**. Los comentarios en **Facebook** tienen una característica muy particular, ha diferencia de muchos otros, Facebook no recarga la página una vez que escribimos y presionamos enter, esto es posible gracias al uso de [Ajax](http://en.wikipedia.org/wiki/Ajax_(programming)), a grandes rasgos Ajax es una tecnología que permite que nuestro navegador (**Chrome**, Firefox, safari, etc) pueda mandar petición al servidor de manera asíncrona, dándonos después la posibilidad de modificar ciertas secciones de nuestra pagina usando JavaScript.

Echemos un vistazo a como lucen los comentarios en Facebook, después podremos comenzar a desarrollar nuestra copia (y aprender de ello en el proceso :))

[![facebook_comments](/images/facebook_comments.jpg)](http://www.alevsk.com/2013/12/comentario-tipo-facebook-utilizando-jquery/facebook_comments/)

Como mencionaba más arriba, básicamente se compone de, un cuadro de texto para escribir el comentario, y cada comentario tiene nombre, avatar y texto, pues manos a la obra.

## Paso 1: Crear la estructura en HTML

Usando HTML vamos a comenzar a crear lo que será nuestro formulario y una lista de comentarios de ejemplo, para esto utilizaremos divs.  
El formulario para escribir comentarios puede ser muy sencillo y constar solo de 2 campos, el texto y el nombre de usuario:

```html
<form accept-charset="utf-8" action="post.php" id="postComment" method="post">
<input autocomplete="off" id="newComment" name="newComment" placeholder="¿En que estas pensando?" required="" type="text"/>
<input id="username" name="username" type="hidden" value="Alevsk"/>
</form>
```

Y nuestro “modelo" de comentario estará conformado solamente por una imagen y un espacio que mostrara texto, algo como:

```html
<div class="comment">
<div class="avatar">
![](img/1.png)
</div>
<div class="autoComment">
<span>Alevsk </span>  
Comentario de ejemplo  
</div>
</div>
```

Ok, entonces ahora combinando ambas cosas el código completo de nuestro index.html se tendría que ver más o menos así.

```html
<!DOCTYPE html>

<head>
<meta charset="utf-8"/>
<meta content="width=device-width" name="viewport"/>
<title>Comentarios tipo facebook con jQuery</title>
<script src="jquery.js" type="text/javascript"></script>
<script src="jquery.validate.js" type="text/javascript"></script>
</head>
<body>
<div id="container">
<div id="comments">
<div class="comment">
<div class="avatar">
![](img/1.png)
</div>
<div class="autoComment">
<span>Alevsk </span>  
Comentario de ejemplo  
</div>
</div>
<div class="comment">
<div class="avatar">
![](img/2.png)
</div>
<div class="autoComment">
<span>Chell </span>  
Comentario de ejemplo  
</div>
</div>
<div class="comment">
<div class="avatar">
![](img/3.png)
</div>
<div class="autoComment">
<span>Calorine </span>  
Comentario de ejemplo  
</div>
</div>
</div>
<div id="commentBox">
<form accept-charset="utf-8" action="post.php" id="postComment" method="post">
<input autocomplete="off" id="newComment" name="newComment" placeholder="¿En que estas pensando?" required="" type="text"/>
<input id="username" name="username" type="hidden" value="Alevsk"/>
</form>
</div>
</div>
</body>
```

Notaran que el Head he agregado de una vez la librería de **jQuery** y un plugin de validación, estos los necesitaremos más adelante ya que nos facilitaran bastante el trabajo :), con el código anterior llevamos algo como la siguiente imagen, ¿no se ve muy lindo verdad?, eso es porque nos falta agregarle un poco de estilos.

[![facebook_comments_1](/images/facebook_comments_1.jpg)](http://www.alevsk.com/2013/12/comentario-tipo-facebook-utilizando-jquery/facebook_comments_1/)

## Paso 2: Agregar estilos

Agregamos el siguiente código **CSS** en cualquier lugar dentro de las etiquetas de head (lo correcto sería tener el css en un archivo aparte, pero para fines demostrativos está bien así por ahora).

```css
<style type="text/css">  
body  
{  
font-family: 'lucida grande',tahoma,verdana,arial,sans-serif;  
font-size: 11px;  
}  
#container  
{  
width: 290px;  
margin: 0 auto;  
height: auto;  
overflow: auto !important;  
}  
#commentBox  
{  
background: #edeff4;  
height: 25px;  
overflow: hidden;  
display: block;  
padding: 10px;  
}  
#postComment input  
{  
width: 100%;  
}  
#postComment .enviar  
{  
clear: both;  
float: left;  
}

#comments  
{  
margin-top: 15px;  
float: left;  
width: 100%;  
background: #edeff4;  
overflow: auto;  
}  
#comments .comment  
{  
padding: 10px;  
border-bottom: 1px solid #fff;  
overflow: auto;  
}  
#comments .comment .avatar  
{  
float: left;  
margin-right: 10px;  
}  
#comments .comment .avatar img  
{  
width: 32px;  
height: 32px;  
}  
#comments .comment .autoComment  
{  
float: right;  
width: 225px;  
}  
#comments .comment .autoComment span  
{  
font-weight: bold;  
color: #3b5998;  
cursor:pointer;  
}  
</style>
```

Recargamos la página y como por arte de magia esto se va pareciendo un poco más a los **comentarios de facebook**

[![facebook_comments_2](/images/facebook_comments_2.jpg)](http://www.alevsk.com/2013/12/comentario-tipo-facebook-utilizando-jquery/facebook_comments_2/)
[![ijCBM2h1of0vE](/images/ijCBM2h1of0vE.gif)](http://www.alevsk.com/2013/12/comentario-tipo-facebook-utilizando-jquery/ijcbm2h1of0ve/)

En este punto tenemos algo ya muy bonito, lamentablemente no hace nada!, pero no nos desesperemos ya que solo nos falta una cosa :).

## Paso 3: Utilizar jQuery para agregar los nuevos comentarios

Lo que tendremos que hacer ahora será que cuando el usuario escriba su comentario y pulse la tecla enter este sea enviado de manera asíncrona (utilizando Ajax) al servidor, después tendremos que dibujar en la pantalla de alguna manera lo que el visitante acaba de comentar, todo esto sin recargar la página. Esto puede sonar más complicado de lo que es, sobre todo si eres nuevo con jQuery. Por suerte jQuery nos permite manipular el [DOM](http://en.wikipedia.org/wiki/Document_Object_Model), podemos incluir elementos diatónicamente en nuestro sitio de manera muy sencilla.

¿Recuerdan el [plugin de validación](http://jqueryvalidation.org/) que había agregado en un inicio?, bueno pues ahora viene la parte interesante, el plugin nos permite agregar validaciones de todo tipo en los campos y capturar ciertos eventos que ocurren en un formulario, por ahora utilizaremos uno llamado **submitHandler**. submitHandler nos permite indicar código para ser ejecutado una ves que el formulario ha activa el disparador **submit**, esto es especialmente util a la hora de validar campos y mostrar información en la pantalla. De nuevo, este código va en cualquier parte de nuestro index.html pero lo recomendable es que este colocado entre las etiquetas head y después de haber includio la **libreria jQuery** y el plugin de validation.

```html
<script type="text/javascript">  
$(document).ready(function(){  
$('#postComment').validate({  
submitHandler: function(form) {

},  
errorPlacement: function(error,element) {  
return;  
},  
});  
});  
</script>
```

Después el bloque de código que se ejecutara dentro del submitHandler será una petición post al servidor utilizando ajax.

```javascript
$.ajax({  
type: "POST",  
contentType: "application/json; charset=utf-8",  
url: $(form).attr('action'),  
data: $(form).serialize(),  
success: function (result) {

var comment = $('<div></div>').addClass('comment');  
var avatar = $('<div></div>').addClass('avatar');  
var img = $('![](None)').attr({'src':'img/1.png'});  
var text = $('<div></div>').addClass('autoComment').html('<span>'+$('#username').val()+' </span>'+$('#newComment').val());

avatar.append(img);  
comment.append(avatar);  
comment.append(text);

$('#comments').append(comment);  
$('#newComment').val(");  
}  
});
```

Por el momento el formulario está mandando una petición al archivo **post.php** que no tiene nada, pero sería posible agregar código en este archivo que permitiera guardar los comentarios una base de datos (tal vez muestre como hacer eso en un artículo futuro)

```php
<?php  
// Guardar el contenido en una base de datos  
// O lo que quieras  
echo "Ok";  
?>
```

Ok, continuamos, lo verdaderamente importante aquí es el siguiente código: 

```javascript
var comment = $('<div></div>').addClass('comment');  
var avatar = $('<div></div>').addClass('avatar');  
var img = $('![](None)').attr({'src':'img/1.png'});  
var text = $('<div></div>').addClass('autoComment').html('<span>'+$('#username').val()+' </span>'+$('#newComment').val());

avatar.append(img);  
comment.append(avatar);  
comment.append(text);

$('#comments').append(comment);
```  
Como mencionaba más arriba **jQuery** nos permite manipular el DOM, con las instrucciones anteriores estamos creando los divs necesarios con el texto y el nombre del visitante que después serán agregados a la lista de comentarios existentes, esto nos dará la ilusión de que el comentario fue agregado inmediatamente después de ser escrito (aunque podría ser el caso de que la información no haya terminado de ser procesada en el servidor).

Combinando el **HTML**, el **CSS** y el **javascript** nuestro archivo **index.html** tendría que verse de la siguiente manera:

```html
<!DOCTYPE html>

<head>
<meta charset="utf-8"/>
<meta content="width=device-width" name="viewport"/>
<title>Comentarios tipo facebook con jQuery</title>
<script src="jquery.js" type="text/javascript"></script>
<script src="jquery.validate.js" type="text/javascript"></script>
<script type="text/javascript">  
$(document).ready(function(){  
$('#postComment').validate({  
submitHandler: function(form) {

$.ajax({  
type: "POST",  
contentType: "application/json; charset=utf-8",  
url: $(form).attr('action'),  
data: $(form).serialize(),  
success: function (result) {

var comment = $('<div></div>').addClass('comment');  
var avatar = $('<div></div>').addClass('avatar');  
var img = $('<img/>').attr({'src':'img/1.png'});  
var text = $('<div></div>').addClass('autoComment').html('<span>'+$('#username').val()+' </span>'+$('#newComment').val());

avatar.append(img);  
comment.append(avatar);  
comment.append(text);

$('#comments').append(comment);  
$('#newComment').val(");  
}  
});  
},  
errorPlacement: function(error,element) {  
return;  
},  
});  
});  
</script>
<style type="text/css">  
body  
{  
font-family: 'lucida grande',tahoma,verdana,arial,sans-serif;  
font-size: 11px;  
}  
#container  
{  
width: 290px;  
margin: 0 auto;  
height: auto;  
overflow: auto !important;  
}  
#commentBox  
{  
background: #edeff4;  
height: 25px;  
overflow: hidden;  
display: block;  
padding: 10px;  
}  
#postComment input  
{  
width: 100%;  
}  
#postComment .enviar  
{  
clear: both;  
float: left;  
}

#comments  
{  
margin-top: 15px;  
float: left;  
width: 100%;  
background: #edeff4;  
overflow: auto;  
}  
#comments .comment  
{  
padding: 10px;  
border-bottom: 1px solid #fff;  
overflow: auto;  
}  
#comments .comment .avatar  
{  
float: left;  
margin-right: 10px;  
}  
#comments .comment .avatar img  
{  
width: 32px;  
height: 32px;  
}  
#comments .comment .autoComment  
{  
float: right;  
width: 225px;  
}  
#comments .comment .autoComment span  
{  
font-weight: bold;  
color: #3b5998;  
cursor:pointer;  
}  
</style>
</head>
<body>
<div id="container">
<div id="comments">
<div class="comment">
<div class="avatar">
![](img/1.png)
</div>
<div class="autoComment">
<span>Alevsk </span>  
Comentario de ejemplo  
</div>
</div>
<div class="comment">
<div class="avatar">
![](img/2.png)
</div>
<div class="autoComment">
<span>Chell </span>  
Comentario de ejemplo  
</div>
</div>
<div class="comment">
<div class="avatar">
![](img/3.png)
</div>
<div class="autoComment">
<span>Calorine </span>  
Comentario de ejemplo  
</div>
</div>
</div>
<div id="commentBox">
<form accept-charset="utf-8" action="post.php" id="postComment" method="post">
<input autocomplete="off" id="newComment" name="newComment" placeholder="¿En que estas pensando?" required="" type="text"/>
<input id="username" name="username" type="hidden" value="Alevsk"/>
</form>
</div>
</div>
</body>
```

Bueno con este concluye este corto y básico tutorial, les pueda servir como base a la hora de implementar sus **sistemas de comentarios** y como siempre en los siguientes enlaces pueden descargar el **codigo fuente** y ver un ejemplo funcionando. Cualquier duda pueden escribirla en la sección de comentarios xD.

salu2

<div class="demobox">
[![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/download.png)](https://mega.co.nz/#!NkIUBCgD!GkNprQkBUJRLGPIcAh9xd2FBoGBwwDGcRgsjZWnEgwE)[![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/demo.png)](http://www.alevsk.com/proyectos/comentarios_facebook/)
</div>
---
title: Formularios bonitos con JQUERY
author: Alevsk
type: post
date: 2010-08-07T03:49:48+00:00
url: /2010/08/formularios-jquery-focus-blur/
categories:
  - CSS
  - Diseño
  - HTML
  - Javascript
  - Jquery
  - Programming
  - Tutorials
tags:
  - CSS
  - Hello world
  - Javascript
  - Jquery
  - Programming
  - Tutorials
  - web

---
[![Photobucket](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/form_jquery.jpg)](http://s251.photobucket.com/albums/gg290/midgar156/alevsk-zone/?action=view¤t=form_jquery.jpg)

Bueno desde hace ya unas semanas quería darme un tiempo para hacer un post donde hablara de la creación de formularios web 2.0 usando la librería JAVASCRIPT de JQUERY, si han visto por ejemplo los formulario de registro de facebook, twitter, algunos blogs de wordpress o portales en joomla en los que cuando hacen clic en el input como que este sobresale y algunos otros que ya traen un texto con una leyenda de la información que tiene que ser incluida en el, veran como se ven de bonitos estéticamente ;).

Al terminar obtendremos un formulario como el que muestro a continuación:

<div class="demobox">
[![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/download.png)](http://www.megaupload.com/?d=KPQOZ58M) [![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/demo.png)](http://www.alevsk.com/proyectos/form)
</div>

Entonces en este post planeo mostrar el código explicado de un formulario básico con efecto de focus y blur (si ese que les comenten de que el input como que se enciende) y el efecto del texto por defecto … iniciamos.

## Paso 1

Lo primero es crear la estructura y el HTML donde incluiremos los formularios, como este sera una pagina de registro muy sencilla nada mas incluiremos nombre, domicilio, mail y pagina web, el código nadamas es XHTML básico.

```Text only
Campos de entrada bonitos con JQUERY




  
    Complete el siguiente formulario para la Suscripción
  
  
  
  
  
  
    
      Nombre:
    
    
    
    
    
    
  
  
  
  
  
  
    
      Domicilio:
    
    
    
    
    
    
  
  
  
  
  
  
    
      Mail:
    
    
    
    
    
    
  
  
  
  
  
  
    
      Pagina web:
    
    
    
    
    
    
  
  
  
  
  
  
    
  
  



	
	

```

## Paso 2

El 50% de la estética de nuestros formularios sera el código CSS, el que usamos en nuestras hojas de estilos, puedes escribir código y combinar colores y crear bordes hasta que quedes satisfecho el que he utilizado yo es el siguiente:

```GDScript
@CHARSET "UTF-8";

/******* GENERAL RESET *******/
html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em,
font, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody,
 tfoot, thead, tr, th, td {
border:0pt none;
font-family:inherit;
font-size:100%;
font-style:inherit;
font-weight:inherit;
margin:0pt;
padding:0pt;
vertical-align:baseline;
}
body{
	line-height: 1em;
	font-size: 12px;
	background: #262626 url(img/bg.png) repeat scroll 0 0;
	font-family: Myriad Pro, Arial, Helvetica, sans-serif;
	margin: 0pt;
	cursor: default;
}
table{
	border-collapse: separate;
	border-spacing: 0pt;
}
strong{
	font-weight: 700;
}
caption, th, td{
	font-weight:normal;
	text-align:left;
}
blockquote:before, blockquote:after, q:before, q:after{
	content:"";
}
blockquote, q{
	quotes:"" "";
}
pre{
	font-family: Arial, Helvetica, sans-serif;
}
input{
	border: 0;
	margin: 0;
	font-family: Arial, Helvetica, sans-serif;
}
textarea{
	font-family: Arial, Helvetica, sans-serif;
	color: #888888;
	padding: 7px 3px 0 4px;
	font-size: 11px;
}
select{
	font-size: 11px;
	color: #888888;
	background: #fff;
	font-family: Arial, Helvetica, sans-serif;
	border: 1px solid #CAD2CE;
}
ul{
	list-style: none;
	list-style-type: none;
	list-style-position: outside;
}
a{
	cursor: pointer;
	color: #296ba5;
	text-decoration: none;
	outline: none !Important;
}
html,body{
	height:100%;
}
.clear{
	clear: both;
	height: 0;
	visibility: hidden;
	display: block;
	line-height: 0;
}
.clearfix{
	overflow: hidden;
}
.fleft{
	float: left;
}
.fright{
	float: right;
}
.italic{
	font-style: italic;
}
/******* FIN GENERAL RESET *******/

body{
	line-height: 1em;
	font-size: 12px;
	background: #262626 url(img/bg.png) repeat scroll 0 0;
	font-family: Myriad Pro, Arial, Helvetica, sans-serif;
	margin: 0pt;
	cursor: default;
}
/* Estilo del contenedor principal, lo centramos y le damos un espacio arriba */
div#container
{
	width: 700px;
	margin: 0pt auto;
	padding-top: 50px;
}
/* Clase de las secciones */
.seccion
{
	margin-bottom:20px;
}
/* Titulo principal */
h1
{
	color: #fff;
	font-size: 30px;
	line-height: 3em;
}
/* Decidi que los labels de los inputs fueran




  para mayor comodidad */
  /* Pero podria ser una clase o un identificador si quieren*/
  h2
  {
  	color: #fff;
  	font-size: 18px;
  	display:block;
  	float:left;
  	text-align:right;
  	padding-right:15px;
  	width:100px;
  	//width:150px;
  	line-height: 3em;
  }
  input.text{
  	width: 500px;
  	background: #171717 url(img/search.png) no-repeat scroll right 2px;
  	padding: 13px;
  	color: #8c8c8c;
  	border: 1px solid #393939;
  	margin-bottom: 30px;
  	border-radius: 5px;
  	-moz-border-radius: 5px;
  	-webkit-border-radius: 5px;
  	-khtml-border-radius: 5px;
  	font-size: 16px;
  }
  input.text.active{
  	background: #343434 url(img/search.png) no-repeat scroll right -43px;
  	border-color: #000;
  	color: #fff;
  }
  .button_centrar
  {
  	width:300px;
  	margin:0 auto;
  }
  input[type="submit"] {
  background:#343434;
  border:1px solid #000;
  color:#FFFFFF;
  cursor:pointer;
  font-size:11px;
  font-weight:700;
  height:40px;
  line-height:28px;
  outline-style:none;
  padding:0 20px;
  text-transform:uppercase;
  width:200px;
  }


```

Como ven al inicio puse un comentario que dice /\****\*\\*\* GENERAL RESET \*\*\*****/ el General Reset no es mas que un código css que nos permite reiniciar la mayoría de las propiedades de los elementos, la ventaja es que así tenemos un mayor control de como se ve el sitio en los navegadores webs (firefox, IE, Opera …), es una buena costumbre usarlo siempre :).

## Paso 3

Ahora viene lo mas interesante y lo que hace la “magia", en el código html vieron que agregue 2 lineas donde se mandan llamar codigos en javascript, las lineas son estas:

```Text only

```

En la primera mandamos llamar el archivo jquery.js que es la libreria JQUERY de Javascript y en el segundo es donde se encuentra el codigo que hemos programado nosotros, para mayor comodidad he escrito el codigo en un archivo aparte.

**Codigo Javascript**

```GDScript
//Seccion de variables
var cajaBoxes = $(".text");
var cajaBox1 = $("#dato1");
var cajaBox2 = $("#dato2");
var cajaBox3 = $("#dato3");
var cajaBox4 = $("#dato4");
var defaultText1 = "Escribe tu nombre ...";
var defaultText2 = "Escribe tu domicilio...";
var defaultText3 = "Escribe tu correo electronico...";
var defaultText4 = "Escribe la url de tu web si tienes...";

//Seccion del evento de focus y blur
cajaBoxes.focus(function(){
	$(this).addClass("active");
});
cajaBoxes.blur(function(){
	$(this).removeClass("active");
});

//Seccion donde mostramos y ocultamos el texto correspondiente
//de cada input
//cajabox2
cajaBox1.focus(function(){
	if($(this).attr("value") == defaultText1) $(this).attr("value", "");
});
cajaBox1.blur(function(){
	if($(this).attr("value") == "") $(this).attr("value", defaultText1);
});

//cajabox2
cajaBox2.focus(function(){
	if($(this).attr("value") == defaultText2) $(this).attr("value", "");
});
cajaBox2.blur(function(){
	if($(this).attr("value") == "") $(this).attr("value", defaultText2);
});

//cajabox3
cajaBox3.focus(function(){
	if($(this).attr("value") == defaultText3) $(this).attr("value", "");
});
cajaBox3.blur(function(){
	if($(this).attr("value") == "") $(this).attr("value", defaultText3);
});

//cajabox4
cajaBox4.focus(function(){
	if($(this).attr("value") == defaultText4) $(this).attr("value", "");
});
cajaBox4.blur(function(){
	if($(this).attr("value") == "") $(this).attr("value", defaultText4);
});

```

**Como ven el código no es nada del otro mundo, vamos a desglosar y analizar para que es cada cosa.**

_En la primera parte declaro variables globales, es de costumbre jeje y además ayuda en el tema de la optimización_

```GDScript
//Seccion de variables
var cajaBoxes = $(".text");
var cajaBox1 = $("#dato1");
var cajaBox2 = $("#dato2");
var cajaBox3 = $("#dato3");
var cajaBox4 = $("#dato4");
var defaultText1 = "Escribe tu nombre ...";
var defaultText2 = "Escribe tu domicilio...";
var defaultText3 = "Escribe tu correo electronico...";
var defaultText4 = "Escribe la url de tu web si tienes...";

```

_En la siguiente parte es donde manejamos el evento de Focus y el evento Blur, aquí añadimos la clase “active" cuando el usuario entra a un input y lo remueve cuando sale_

```Scilab
//Seccion del evento de focus y blur
cajaBoxes.focus(function(){
	$(this).addClass("active");
});
cajaBoxes.blur(function(){
	$(this).removeClass("active");
});

```

_Y por ultimo nos queda la parte del texto por defecto en los inputs, aqui nadamas compara si el input tiene el foco y el **value** del input es el valor del texto por defecto defaultText entonces le da un valor the null y eso hace que el texto desaparezca y podamos escribir 🙂 y para que se el texto aparezca al salir del foco del input compara si el **_value_** es nulo y entonces le asigna el texto por defecto .. sencillo 🙂_

```Scilab
//Seccion donde mostramos y ocultamos el texto correspondiente
//de cada input
//cajabox2
cajaBox1.focus(function(){
	if($(this).attr("value") == defaultText1) $(this).attr("value", "");
});
cajaBox1.blur(function(){
	if($(this).attr("value") == "") $(this).attr("value", defaultText1);
});

//cajabox2
cajaBox2.focus(function(){
	if($(this).attr("value") == defaultText2) $(this).attr("value", "");
});
cajaBox2.blur(function(){
	if($(this).attr("value") == "") $(this).attr("value", defaultText2);
});

//cajabox3
cajaBox3.focus(function(){
	if($(this).attr("value") == defaultText3) $(this).attr("value", "");
});
cajaBox3.blur(function(){
	if($(this).attr("value") == "") $(this).attr("value", defaultText3);
});

//cajabox4
cajaBox4.focus(function(){
	if($(this).attr("value") == defaultText4) $(this).attr("value", "");
});
cajaBox4.blur(function(){
	if($(this).attr("value") == "") $(this).attr("value", defaultText4);
});

```

Bueno eso es todo, espero les haya gustado, si tiene alguna duda ponerla en los comentarios y con gusto les ayudare 😀

**En mi próximo post planeo continuar con este formulario y comenzar a agregar validación de entrada de datos, veran que tambien es realmente sencillo :).**

salu2
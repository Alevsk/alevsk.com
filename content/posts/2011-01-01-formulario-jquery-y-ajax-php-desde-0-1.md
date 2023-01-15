---
title: 'Formulario Jquery y Ajax desde 0 [HTML y CSS]'
author: Alevsk
type: post
date: 2011-01-01T21:13:43+00:00
url: /2011/01/formulario-jquery-y-ajax-php-desde-0-1/
categories:
  - CSS
  - Diseño
  - Javascript
  - Jquery
  - Programming
  - Tutorials
tags:
  - CSS
  - Javascript
  - Jquery
  - Programming
  - software libre
  - Solutions
  - Tutorials
  - web

---
[![](/images/tuto_form.jpg)](http://www.alevsk.com/2011/01/formulario-jquery-y-ajax-php-desde-0-1/tuto_form/)  
Comenzamos el año recargados :), con nuevos tutoriales sobre programación, diseño y Seguridad Informática.

En post anteriores vimos como hacer [menus usando solo CSS][1] y también como crear [formularios 2.0 usando Jquery][2].

Ahora toca juntar todo lo que aprendimos y crear un formulario de contacto completo :), nuestros objetivos serán:

  * [Crear un formulario 2.0 usando **CSS** y HTML][3]
  * [Usando Jquery para darle vida a nuestro formulario][4]
  * [Realizar validaciones con **Jquery** del lado del cliente][5]
  * [Hacer uso de la tecnología **Ajax** para mandar los datos al **script PHP** sin recargar la pagina][6]
  * [Realizar validaciones con **PHP** del lado del servidor][7]
  * [Finalmente enviar el mensaje a un mail][8]

### La estructura HTML/CSS

Comenzamos, lo primero es tener en mente como sera el diseño del formulario, que imágenes utilizaremos, etc yo les recomiendo que el estilo sea parecido al diseño del sitio donde lo van a implementar, entonces revisen bien en los colores primarios de su sitio, las imágenes que utilizan, etc. Ya que se tiene conceptual-izado lo que queremos hacer nos ponemos a escribir el código html y css que sera como el esqueleto de todo eso 😉

**HTML**

```Text only

  
    
  
  						
  
  
    Formulario de Contacto
  
  						
  							
  
  
    
      
    
    							
  
  				


```

Ese seria el código HTML de un formulario simple, como ven son menos de 30 lineas nada del otro mundo, omitimos las etiquetas previas (<head>
  ) para no hacer tan grande el código, pero uds se las ponen :D, continuamos, ya tenemos el <strong>HTML</strong> escrito ahora falta el <strong>CSS</strong>
<p>
<strong>El CSS</strong>
</p>
```cplint

h1,h2,h3{
	font-weight:bold;
}
body, html{
	font-family: Verdana, Arial, Helvetica, sans-serif;
	font-size: .9em;
	background: #f3f7ff;
	height: 100%;
}
.centrado
{
	margin: 0 auto;
	width:500px;
}
a{
	color: #598F8F;
}
.outerbox{
	width: 700px;
	float: left;
	height: 100%;
	/*margin: 0 0 0 400px;*/
	margin: 0 0 0 430px;
	display: inline;
	position: relative;
}
#infobox{
	float: right;
	margin: 0 300px 0 300px ;
}
#infobox p.box, #infobox div.box{
	height: 450px;
}
.box{
	background: transparent url(..//images/fff50.png);
	width: 500px;
	height: 420px;
	float: left;
	font-size: 0.85em;
	position: relative;
	color: #686868;
	margin: 40px 0 0 0;
	padding: 10px 10px 35px 10px;
	display: inline;
	border: 1px solid #CCCCCC;
		border-radius: 5px 5px 5px 5px;
	-moz-border-radius: 5px 5px 5px 5px;
	-webkit-border-radius: 5px 5px 5px 5px;
	-khtml-border-radius: 5px 5px 5px 5px;
}
.outerbox > .box{
	height: auto;
	min-height: 420px;
}
.box p, .box h2{	
	margin: 3px 0;
	float: left;
	clear: left;
	text-align: justify;
	width: 500px;
}
.box h2{
	width: 500px;
	font-size: 1.4em;
	margin: 10px 0 5px 0;
}
#info, .info{
	padding: 10px;
}
.info{
	background: transparent url(..//images/fff50.png);
}

.description
{
height:170px;
position:absolute;
right:-16px;
top:-17px;
width:170px;
}
.contacto
{
	background:url("..//images/contacto.png") no-repeat scroll right top transparent;
}
/*FORMS*/
label
{
	display:block;
	font-size:14px;
	line-height:2em;
}
#loading img {
	padding: 0;
	margin: 0;
}
textarea
{
		width:80%;
		margin:0 auto;
		height:100px;
		color:#888888;
}
form input[type="text"]{
color:#888888;
}
input.submit {
/*
color:#000000;
margin-top:20px;
padding:5px;
width:auto !important;*/
	background-image:url("/images/bg_nav_hover.png");
	background-repeat:repeat-x;
	border-color:#077DB3 #077DB3 #05537C;
	border-style:solid;
	border-width:1px;
	color:#FFFFFF;
	font-size:11px;
	font-weight:bold;
	height:32px;
	margin-top:10px;
	text-decoration:none;
	text-transform:uppercase;
	width:auto;
}
.requisites{
	display:none;
}
.error{
	background: #fff8cc;
	padding:5px;
	margin-left:10px;
	/*color: #171717;*/
	color:#d42323;
	border-radius: 5px;
	-moz-border-radius: 5px;
	-webkit-border-radius: 5px;
	-khtml-border-radius: 5px;
}
.messageerror
{
	margin-left:30%;
	display:none;
}
input.error{

}
#loading {
	background:url("/images/transparent.png") repeat scroll 0 0 transparent;
	margin:0 auto;
	color:#FFFFFF;
	padding:10px;
	position:relative;
	text-align:center;
	top:-250px;
	width:300px;
	display:none;
	font-weight:bold;
	border-radius: 5px 5px 5px 5px;
	-moz-border-radius: 5px 5px 5px 5px;
	-webkit-border-radius: 5px 5px 5px 5px;
	-khtml-border-radius: 5px 5px 5px 5px;
}
#transparencia {
    -moz-border-radius: 5px 5px 5px 5px;
    background: url("/images/transparent.png") repeat scroll 0 0 transparent;
    color: #FFFFFF;
    display: none;
    font-weight: bold;
    height: auto;
    left: 30%;
    margin: 0 auto;
    padding: 10px;
    position: absolute;
    text-align: center;
    top: 30%;
    width: 230px;
    z-index: 999;
}
#botonEnviar, .button {
	bottom: 15px;
    float: left;
    margin-right: 10px;
    right: 15px;
}

#botonEnviar, .button.fit {
    float: left;
}

#botonEnviar, .button {
    -moz-border-radius: 3px 3px 3px 3px;
    -moz-box-shadow: 0 1px 0 0 rgba(0, 0, 0, 0.1);
    background-color: #FF920D;
    background-image: -moz-linear-gradient(center top , #ff0000 0%, #CF1010 100%);
    border: 1px solid #333333;
    color: #FFFFFF !important;
    cursor: pointer;
    display: block;
    font-weight: bold;
    line-height: 18px;
    min-width: 40px;
    padding: 4px 15px 6px;
    text-align: center;
    text-shadow: 0 -1px 0 #333;
}
/*FORMS*/

```
<p>
    Ya con esto el formulario se ve mas decente xD, ahora necesitamos darle vida al formulario, si por ejemplo que en los inputs muestre un texto explicativo y cuando el usuario de clic en el desaparezca, un efecto de focus y blur también estaría bien ;).
  </p>
<div class="demobox" style="height: auto;">
    El siguiente paso es [Usar Jquery para darle vida a nuestro Formulario](http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-2)
</div>

 [1]: http://www.alevsk.com/2010/06/bonito-menu-horizontal-desplegable-con-css/
 [2]: http://www.alevsk.com/2010/08/formularios-jquery-focus-blur/
 [3]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-1
 [4]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-2
 [5]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-3
 [6]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-4
 [7]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-5
 [8]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-6</head>
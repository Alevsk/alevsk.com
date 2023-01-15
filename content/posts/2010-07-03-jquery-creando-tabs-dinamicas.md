---
title: 'Jquery: Creando Tabs dinamicas!'
author: Alevsk
type: post
date: 2010-07-03T21:06:34+00:00
url: /2010/07/jquery-creando-tabs-dinamicas/
image:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/jquery.jpg
slider_thumbnail:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/thumb-tabs.jpg
categories:
  - CSS
  - HTML
  - Javascript
  - Jquery
tags:
  - compartir
  - Javascript
  - Jquery
  - menus
  - Programming
  - tabs
  - Tutorials

---
**Primero la definición de la [Wikipedia][1]:**  
jQuery es una biblioteca o framework de Javascript, creada inicialmente por John Resig, que permite simplificar la manera de interactuar con los documentos HTML, manipular el arbol DOM, manejar eventos, desarrollar animaciones y agregar interacción con la tecnología AJAX a páginas web.

Bueno en esta ocacion quiero mostrarles lo fácil, sencillo e intuitivo que es desarrollar bonitos efectos con la las librerías de jquery, uno de los frameworks de javascript con mas aceptación por los desarrolladores, muchos nos hemos topado con proyectos que requieren de un menú de navegación por pestañas (tabs) para tener el contenido mas organizado o por simple cuestión de estética, la manera antigua era utilizando php y usando IF o los case y pasando los datos ya fuera por GET o POST xD, sin embargo en la actualidad jquery nos permite hacer lo mismo pero con mas dinamismo y mejor estética, pueden ver el demo y descargar el código al final del post, enjoy it!!

<!--more-->
![Photobucket](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/tab-azul.jpg)
![Photobucket](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/tab-verde.jpg)
![Photobucket](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/tab-roja.jpg) 

**index.html**

```Objective-C
Prueba de jQuery
    

	 




  
    Menu Tab con jQuery
  
  
  
  
  
  
    
      
        [Diseno](#)
      
      
      
      	
      
      
        [Programacion](#)
      
      
      
      	
      
      
        [Seguridad](#)
      
      
      
    
    
    
    
    
    
      
        
          
            [Maquetacion de estilos](#)
          
          
          
          	
          
          
            [Photoshop](#)
          
          
          
          	
          
          
            [Digital](#)
          
          
          
        
        
      
      
      
      
      
      
        
          
            [C++](#)
          
          
          
          	
          
          
            [PHP / MYSQL](#)
          
          
          
          	
          
          
            [AJAX](#)
          
          
          
          	
          
          
            [Framework Jquery](#)
          
          
          
          	
          
          
            [Java](#)
          
          
          
        
        
      
      
      
      
      
      
        
          
            [Web](#)
          
          
          
          	
          
          
            [Redes](#)
          
          
          
          	
          
          
            [Desbordamientos de Memoria](#)
          
          
          
          	
          
          
            [Ingenieria Inversa](#)
          
          
          
          	
          
          
            [Ingenieria Inversa](#)
          
          
          
        
        
      
      
    
    
  
  



```

**azul_estilo.css**

```GAS
/*Estilos de la pagina principal, el tipo de letra sera
eredado por las demas clases y los identificadores*/

body
{
	font-family:Arial, Helvetica, sans-serif;
	background: #023c4b;
	color:#FFFFFF;
}

/*list-style nos sirve para definir el "icono" que usaran los elementos de la lista
le ponemos none para que no aparezca hay mas tipos, googlen :p*/
ul,li
{
	list-style:none;
}

/*El primer identificador, es el container que contendra todos los elementos*/
#container
{
	margin:0 auto;
	width:400px;
}

/*Tab_contenedor va a tener dentro tanto los menus como los contenidos de cada uno*/
#tab_contenedor
{
	padding:8px 8px;
	width:auto;
	min-width:350px;
	background:#097793;
	border:1px solid #000000;
}
#texto
{
	padding:5px;
	background:#FFFFFF;
	border:1px solid #04667f;
}
/*Seran los menus o botones principales para cambiar de contenido*/
ul.menu{
	margin:0px;
	padding:0px;
	margin-top:5px;
	margin-bottom:6px;
	font-weight:bold;
}
/*Mostramos los elementos listas del menu en una sola linea
seria posible lograrlo con un float:left*/
ul.menu li
{
	display:inline;
}

/*Damos formato a los links de los menus*/

ul.menu li a
{
	color:#097793;
	padding:5px 10px 6px 10px;
	font-size:14px;
	text-transform:uppercase;
	border:1px solid #04667f;
	background:#FFFFFF;
	text-decoration:none;
}

ul.menu li a:hover
{
	border:1px solid #CCCCCC;
}
ul.menu li a.activo
{
	color:#000000;

	border-bottom: 2px solid #ffffff;
	background:#FFFFFF;
}
ul.menu li a.activo:hover
{

}
a.tab{
font: bold 15px Arial, Helvetica, sans-serif;
text-decoration:none;
}

/*Aqui es para darle algo de estetica a los elementos
listas y links del textoo*/
.texto ul
{
	margin:10px 0px;
	padding:0 11px;
}
.texto ul li
{
	margin-bottom:3px;
	font-size:15px;
}
.texto ul li a
{
	color:#3f4c4f;
}
.texto ul li a:hover
{
	color:#899fa5;
}

/*Aqui es donde entra la magia de jquery por default mostramos el contenido 2 y 3 como none
osea oculto, despues con jquery cambiaremos esos parametros en los eventos clic*/
#texto_2, #texto_3
{
	display:none;

```

Como es de costumbre a continuación pongo el link para que descarguen el código fuente que use en el ejemplo, así como el link al live demo

<div class="demobox">
[![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/download.png)](http://www.megaupload.com/?d=G4DBIU0A) [![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/demo.png)](http://alevsk.frexa.com.ar/jquery-tab/)
</div>

salu2

 [1]: https://secure.wikimedia.org/wikipedia/es/wiki/JQuery
---
title: Bonito Menu horizontal desplegable con CSS
author: Alevsk
type: post
date: 2010-06-30T21:35:23+00:00
url: /2010/06/bonito-menu-horizontal-desplegable-con-css/
image:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/menu.jpg
slider_thumbnail:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/thumb-css.jpg
categories:
  - CSS
  - Diseño
  - Geek
  - HTML
  - Jquery
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - CSS
  - horizontal
  - Javascript
  - menu
  - Programming
  - Technology
  - Tutorials
  - twitter
  - ubuntu
  - web

---
[![](/images/css_imagination.jpg)](http://www.alevsk.com/2010/06/bonito-menu-horizontal-desplegable-con-css/css_imagination/)

Bueno hace rato mientras comía por puro ocio hice un menú desplegable con puro CSS nada de Javascript xD, bueno aquí se los pongo por si les gusta y lo quieren implementar en sus desarrollos (nunca esta demás tener recursos por ahí guardados)

A continuación esta el link para que descarguen el código fuente y un link hacia el ejemplo practico en acción:

<div class="demobox">
[![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/download.png)](http://www.megaupload.com/?d=1G9RVNCE) [![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/demo.png)](http://alevsk.frexa.com.ar/menucss/)
</div>
<!--more-->

**index.html**

```Objective-C

  
    
      ![](img/Profile.png) Mi Perfil
      
      
        
          [Editar Perfil](#)
        
        
        
        	
        
        
          [Listar](#)
        
        
        
        	
        
        
          [Agregar](#)
        
        
        
      
      
    
    
    
    	
    
    
      ![](img/Home.png) Mi escuela
      
      
        
          [Agregar](#)
        
        
        
      
      
    
    
    
    	
    
    
      ![](img/Teacher.png) Profesores
      
      
        
          [Agregar](#)
        
        
        
        	
        
        
          [Activos](#)
        
        
        
        	
        
        
          [Inactivos](#)
        
        
        
        	
        
        
          [Modificar](#)
        
        
        
        	
        
        
          [Borrar](#)
        
        
        
      
      
    
    
    
    	
    
    
      ![](img/Student.png) Alumnos
      
      
        
          [Mostrar todos](#)
        
        
        
      
      
    
    
    
    	
    
    
      ![](img/Grades.png) Grados
      
      
        
          [Agregar](#)
        
        
        
      
      
    
    
    
    	
    
    
      ![](img/Claves.png) Claves
      
      
        
          [Agregar](#)
        
        
        
      
      
    
    
    
    	
    
    
      ![](img/Status.png) Status
      
      
        
          [Agregar](#)
        
        
        
      
      
    
    
    
    	
    
    
      ![](img/Types.png) Tipos
      
      
        
          [Agregar](#)
        
        
        
      
      
    
    
    
  
  




```

**menu.css**

```CSS+Lasso
#menu {  /*text-align: center;

font-size: 0.7em;

width: 820px;

margin: 20px auto;*/

float:left; padding:10px; border:2px solid #003D4C;  background-color: #fff; margin: 0px 0; font-weight:normal; color:#003D4C;

}

#menu ul { /*list-style-type: none;*/

	margin:0;

	padding:0;

	width:auto;

	float:right;

	list-style:none;

}

#menu ul li.nivel1 { /*float: left;

width: 162px;

margin-right: 2px;*/

	display:block;

	float:left;

	margin:0 0px;

	margin-right:10px;

}

#menu ul li a {/*display: block;

text-decoration: none;

color: #fff;

background-color: #399;

border: solid 1px #fff;

padding: 8px;

position: relative;*/

}

#menu ul li:hover {position: relative;

list-style:none;

}

#menu ul li a:hover, #menu ul li:hover a.nivel1 {/*background-color: #6CC;

color: #000;

position: relative;*/

	color: #003d4c;

	text-decoration:none;

}

#menu ul li a.nivel1 {display: block!important;display: none;

position: relative;

}

#menu ul li ul {display: none;

}

#menu ul li a:hover ul, #menu ul li:hover ul {display: block;

position: absolute;left: 0px;border:1px solid #003D4C;

background-color: #fff;padding:5px;

}

#menu ul li ul li a {

/*width: 160px;

padding: 6px 0px 8px 0px;

border-top-color: #000;

display:block;*/

width:160px;

background:none repeat scroll 0 0 #e0f8ae;

	border:1px solid #7f9455;

	line-height:15px;

	margin:10px 0 0;

	overflow:hidden;

	text-align:center;

	display:block;

	height:auto;

	color:#333333;

	direction:ltr;

	font-family:"lucida grande",tahoma,verdana,arial,sans-serif;

	font-size:11px;

	padding:7px 3px;

}

#menu ul li ul li a:hover {

/*border-top-color: #000;

position: relative;

border:1px solid #003D4C;

background-color:#ecf5f8;*/

position: relative;

background:none repeat scroll 0 0 #FFEBE8;

	border:1px solid #DD3C10;

	line-height:15px;

	margin:10px 0 0;

	overflow:hidden;

	text-align:center;

	display:block;

	height:auto;

	color:#333333;

	direction:ltr;

	font-family:"lucida grande",tahoma,verdana,arial,sans-serif;

	font-size:11px;

	padding:7px 3px;

}

table.falsa {border-collapse:collapse;

border:0px;

float: left;

position: relative;

}

```

salu2
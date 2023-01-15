---
title: 'Formulario Jquery y Ajax desde 0 [Javascript]'
author: Alevsk
type: post
date: 2011-01-17T01:15:41+00:00
url: /2011/01/formulario-jquery-y-ajax-php-desde-0-2/
categories:
  - CSS
  - Diseño
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

Hola de nuevo, en el tutorial anterior ya creamos lo que es la estructura de nuestro formulario (**HTML**) y le dimos presentación usando **CSS**.

El orden de los tutoriales es el siguiente (por si alguien anda medio despistado):

  * [Crear un formulario 2.0 usando **CSS** y HTML][1]
  * [Usando Jquery para darle vida a nuestro formulario][2]
  * [Realizar validaciones con **Jquery** del lado del cliente][3]
  * [Hacer uso de la tecnología **Ajax** para mandar los datos al **script PHP** sin recargar la pagina][4]
  * [Realizar validaciones con **PHP** del lado del servidor][5]
  * [Finalmente enviar el mensaje a un mail][6]

Nuestro objetivo en esta ocasión es darle algo de vida a nuestro formulario para ello escribiremos un código Javascript que nos muestre un texto descriptivo en los inputs del formulario y que este desaparezca al hacer clic en el, evento focus y blur, el codigo sera el siguiente:

```GDScript
jQuery(document).ready(function(){
	//variables globales
	var formBoxes= jQuery(".text");
	var inputUsername = jQuery("#inputNombre");
	var inputEmail = jQuery("#inputCorreo");
        var inputWebsite = jQuery("#inputWeb");
	var textareaMessage = jQuery("#inputComentario");

	var defaultUsername = "Escribe tu nombre...";
	var defaultEmail = "Escribe tu email...";
	var defaultWebsite = "Url de tu web si tienes...";
	
	//controlamos el foco / perdida de foco para los input text
	formBoxes.focus(function(){
		jQuery(this).addClass("active");
	});
	formBoxes.blur(function(){
		jQuery(this).removeClass("active");  
	});

	//Para que los inputs tengan un texto descriptivo de la informacion requerida
	//se ve bonito
	inputUsername.focus(function(){
		if(jQuery(this).attr("value") == defaultUsername) jQuery(this).attr("value", "");
	});
	inputUsername.blur(function(){
		if(jQuery(this).attr("value") == "") jQuery(this).attr("value", defaultUsername);
	});
	
	inputEmail.focus(function(){
		if(jQuery(this).attr("value") == defaultEmail) jQuery(this).attr("value", "");
	});
	inputEmail.blur(function(){
		if(jQuery(this).attr("value") == "") jQuery(this).attr("value", defaultEmail);
	});
	
	inputWebsite.focus(function(){
		if(jQuery(this).attr("value") == defaultWebsite) jQuery(this).attr("value", "");
	});
	
	inputWebsite.blur(function(){
		if(jQuery(this).attr("value") == "") jQuery(this).attr("value", defaultWebsite);
	});
	
});

```

Vemos que el código anterior es muy sencillo, si ya tienes nociones básicas del uso de la librería Jquery en Javascript veras que al inicio lo que hacemos es declarar variables que son son “vinculadas" a elementos del DOM usando el nombre de una clase como .text o identificadores en el caso de #inputNombre ;), etc. También declaramos defaultUsername, defaultEmail, defaultWebsite que seran los strings que queremos que se muestren como descripcion (Nota: estos mensajes tienen que ser los mismos que tengan los **values**) de los inputs para poderlos comparar mas adelante.

Mas abajo donde comienza la linea de:

```Text only
formBoxes.focus(function(){
		jQuery(this).addClass("active");
	});
	formBoxes.blur(function(){
		jQuery(this).removeClass("active");  
	});

```

Hacemos uso del evento focus y blur de Jquery que significa, focus = cuando el input esta seleccionado, blur cuando esta de-seleccionado, aquí les dejo un link hacia una lista de eventos que **jquery** es capaz de manejar http://api.jquery.com/category/events/, como podemos ver si el input tiene el foco le añadimos la clase active y si pierde el foco (evento blur) removemos la clase, de igual forma podríamos agregar lo que quisiéramos.

Y al final realizamos las comparaciones, si los textos que tienen nuestras 3 variables (defaultUsername, defaultEmail y defaultWebsite) son iguales a los values de los inputs significa que el usuario no ha escrito nada y entonces al darle clic jquery limpiara el campo de texto, si el campo de texto se mantiene vacio y el input entra en estado de blur le agregamos el texto descriptivo 🙂 y eso es todo.

Lo siguiente sera crear reglas de validación para nuestros campos de texto 🙂  
**  
Nota: se puede usar tanto la palabra jQuery como el simbolo $, por ejemplo $(this) o jQuert(this) seria exactamente lo mismo, se utiliza para que el codigo no estre en conflicto con otras librerias de Javascript.**_
<div class="demobox" style="height: auto;">
  El siguiente paso es [Validar datos del lado del cliente con Javascript](http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-3)
</div>

 [1]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-1
 [2]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-2
 [3]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-3
 [4]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-4
 [5]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-5
 [6]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-6
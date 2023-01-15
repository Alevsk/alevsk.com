---
title: 'Formulario Jquery y Ajax desde 0 [Validacion JQuery]'
author: Alevsk
type: post
date: 2011-01-17T01:11:44+00:00
url: /2011/01/formulario-jquery-y-ajax-php-desde-0-3/
categories:
  - CSS
  - Diseño
  - Jquery
  - Programming
  - Tutorials
tags:
  - CSS
  - Jquery
  - Programming
  - software libre
  - Solutions
  - Technology
  - Tutorials
  - web

---
[![](/images/tuto_form.jpg)](http://www.alevsk.com/2011/01/formulario-jquery-y-ajax-php-desde-0-1/tuto_form/)

Una de las partes mas importantes de la programación es la validación de datos, es decir que los datos que estamos recibiendo sean los correctos, en la programación web hay 2 tipos de validaciones, del lado del cliente que ocurre en el navegador y que es en la que nos enfocaremos en este **tutorial** utilizando **Jquery** y la validaciones del lado del servidor que como su nombre lo indica se realizan con algun lenguaje de programación del lado del servidor como puede ser **PHP, ASP .NET, PERL** o incluso **JSP**.

¿Para que nos sirve validar datos y proteger nuestras aplicaciones web?  
Pues la mayoria de los usuarios que usan la red solo se limitan a eso, a utilizar los servicios, pero existen otro tipos de usuarios que tienen profundos conocimientos relacionados a la seguridad informática y que son capaces de encontrar bugs en nuestros códigos (generalmente por fallos de programación) y a partir de ahí intentar tomar un servidor para hacer usos distintos con el ;).

Por si alguien esta perdido el orden de los tutoriales es el siguiente:

  * [Crear un formulario 2.0 usando **CSS** y HTML][1]
  * [Usando Jquery para darle vida a nuestro formulario][2]
  * [Realizar validaciones con **Jquery** del lado del cliente][3]
  * [Hacer uso de la tecnología **Ajax** para mandar los datos al **script PHP** sin recargar la pagina][4]
  * [Realizar validaciones con **PHP** del lado del servidor][5]
  * [Finalmente enviar el mensaje a un mail][6]

### La validación de datos usando JQuery del lado del cliente

Seguiremos utilizando nuestro archivos .JS al cual llamamos validacion_form.js en el tutorial pasado, sobre ese archivos seguiremos escribiendo nuestro código que al final quedo asi.

```GDScript
jQuery(document).ready(function(){
	//variables globales
	var formBoxes= jQuery(".text");
	var inputUsername = jQuery("#inputNombre");
	var reqUsername = jQuery("#req-username");
	var inputEmail = jQuery("#inputCorreo");
	var reqEmail = jQuery("#req-email");
	var inputWebsite = jQuery("#inputWeb");
	var textareaMessage = jQuery("#inputComentario");
	var reqMessage = jQuery("#req-message");
	
	var defaultUsername = "Escribe tu nombre...";
	var defaultEmail = "Escribe tu email...";
	var defaultWebsite = "Url de tu web si tienes...";
	
	//funciones de validacion
	function validateMessage(){
		//Si el mensaje esta vacio
		if(textareaMessage.val().length == 0){
			reqMessage.fadeIn('fast');
			reqMessage.removeClass("requisites");
			return false;
		}

		else{
			reqMessage.fadeOut('fast');
			reqMessage.addClass("requisites")//oculta el mensaje de nuevo
			return true;
		}	
	}
	
	function validateUsername(){
		//NO cumple longitud minima
		if(inputUsername.val().length < 4 || inputUsername.val == defaultUsername){
			reqUsername.fadeIn('fast');
			reqUsername.removeClass("requisites");
			return false;
		}
		//SI longitud pero NO solo caracteres A-z
		else if(!inputUsername.val().match(/^[a-zA-Z]+$/)){
			reqUsername.fadeIn('fast');
			reqUsername.removeClass("requisites");
			return false;
		}
		// SI longitud, SI caracteres A-z
		else{
			reqUsername.fadeOut('fast');
			reqUsername.addClass("requisites")//oculta el mensaje de nuevo
			return true;
		}
	}
	function validateEmail(){
		//NO hay nada escrito
		if(inputEmail.val().length == 0){
			reqEmail.fadeIn('fast');
			reqEmail.removeClass("requisites");
			return false;
		}
		// SI escrito, NO VALIDO email
		else if(!inputEmail.val().match(/^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i)){
			reqEmail.fadeIn('fast');
			reqEmail.removeClass("requisites");
			return false;
		}
		// SI rellenado, SI email valido
		else{
			reqEmail.fadeOut('fast');
			reqEmail.addClass("requisites");//oculta el mensaje de nuevo
			return true;
		}
	}
	
	//controlamos la validacion en los distintos eventos
	// Perdida de foco
	inputUsername.blur(validateUsername);
	inputEmail.blur(validateEmail);
	textareaMessage.blur(validateMessage);
	
	// En cuanto el usuario esta pulsando teclas (escribiendo)
	inputUsername.keyup(validateUsername);
	inputEmail.keyup(validateEmail);
	textareaMessage.keyup(validateMessage);
	
	// Envio de formulario
	jQuery("#form1").submit(function(){
		if(validateUsername() == true && validateEmail() == true && validateMessage() == true)
		{
			jQuery("#loading").animate({height:'show',width:'show',opacity:'show'},{duration:'slow'});
			return true;
		}
		else
		{
			return false;
		}
	});
	
	//controlamos el foco / perdida de foco para los input text
	formBoxes.focus(function(){
		jQuery(this).addClass("active");
	});
	formBoxes.blur(function(){
		jQuery(this).removeClass("active");  
	});

	//Para que los inputs tengan un texto descriptivo de la informacion requerida
	//se ve bonito :)
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

Como ven hemos agregado las siguientes lineas al inicio

```GDScript
var reqUsername = jQuery("#req-username");
	var reqEmail = jQuery("#req-email");
	var reqMessage = jQuery("#req-message");

```

Si analizamos nuestro código HTML esos son los ID's de los divs que mostraran un mensaje de error, en caso de que la validación de nombre, email o mensaje no se cumpla.

Mas abajo creamos unas pequeñas funciones que nos ayudaran a validar los datos por ejemplo la funcion que valida el nombre de usuario:

```Tera Term macro
function validateUsername(){
		//NO cumple longitud minima
		if(inputUsername.val().length < 4 || inputUsername.val == defaultUsername){
			reqUsername.fadeIn('fast');
			reqUsername.removeClass("requisites");
			return false;
		}
		//SI longitud pero NO solo caracteres A-z
		else if(!inputUsername.val().match(/^[a-zA-Z]+$/)){
			reqUsername.fadeIn('fast');
			reqUsername.removeClass("requisites");
			return false;
		}
		// SI longitud, SI caracteres A-z
		else{
			reqUsername.fadeOut('fast');
			reqUsername.addClass("requisites")//oculta el mensaje de nuevo
			return true;
		}
	}

```

En la cual al inicio realiza una comparación de longitud de caracteres o que el texto en el value no sea igual al texto descriptivo, si la validación falla nos devuelve un false y un mensaje de error aparece, esto se logra añadiéndole una clase que tiene un **display:block;** y un evento de fadeIn para que el mensaje (el div) aparezca fácilmente, también comprobamos que el nombre de usuario no contenga caracteres especiales como **/?¿'*** etc, de la misma forma cuando la validación se cumple se le agrega la clase que tiene el **display:none;** y se utiliza la fadeOut para desaparecer el mensaje suavemente.

Si analizas el código fuente veras que las demas funciones que validan los siguientes campos son muy similares.

Ahora ¿como disparamos esas funciones de validación? pues de nueva cuenta hacemos uso de los eventos focus y blur que nos brinda **JQuery** y esta vez también hacemos uso de un nuevo evento llamado keyup que detecta cuando el usuario ha pulsado una tecla.

```Scilab
//controlamos la validación en los distintos eventos
	// Perdida de foco
	inputUsername.blur(validateUsername);
	inputEmail.blur(validateEmail);
	textareaMessage.blur(validateMessage);
	
	// En cuanto el usuario esta pulsando teclas (escribiendo)
	inputUsername.keyup(validateUsername);
	inputEmail.keyup(validateEmail);
	textareaMessage.keyup(validateMessage);

```

Y al final tenemos un código que sera el que se comunique con el codigo del siguiente tutorial hecho con AJAX :D, este codigo capturara el evento **submit** de nuestro formulario y dependiendo de si cumple o no con las validaciones devolvera un true o un false segun sea el caso, a su vez también mostrara una .

```GDScript
// Envio de formulario
	jQuery("#form1").submit(function(){
		if(validateUsername() == true && validateEmail() == true && validateMessage() == true)
		{
			jQuery("#loading").animate({height:'show',width:'show',opacity:'show'},{duration:'slow'});
			return true;
		}
		else
		{
			return false;
		}
	});

```

Ya casi terminamos 🙂

<div class="demobox" style="height: auto;">
  El siguiente paso es [Hacer uso de la tecnología Ajax para mandar los datos al script PHP sin recargar la pagina](http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-4)
</div>

 [1]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-1
 [2]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-2
 [3]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-3
 [4]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-4
 [5]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-5
 [6]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-6
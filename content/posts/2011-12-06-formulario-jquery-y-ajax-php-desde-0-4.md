---
title: 'Formulario Jquery y Ajax desde 0 [Ajax]'
author: Alevsk
type: post
date: 2011-12-06T08:48:29+00:00
url: /2011/12/formulario-jquery-y-ajax-php-desde-0-4/
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
  - Javascript
  - Jquery
  - Programming
  - Solutions
  - Technology
  - Tutorials

---
[![](/images/tuto_form.jpg)](http://www.alevsk.com/2011/01/formulario-jquery-y-ajax-php-desde-0-1/tuto_form/)

Hola, me ha costado mucho seguir con este tutorial por cuestiones de tiempo, pero para no quedar mal con mis lectores y en especial con la gente que ha estado siguiendo este manual (que son muchos) aqui estamos trabajando 🙂

Les recuerdo el orden de los post por si alguien esta perdido y no los encuentra.

  * [Crear un formulario 2.0 usando **CSS** y HTML][1]
  * [Usando Jquery para darle vida a nuestro formulario][2]
  * [Realizar validaciones con **Jquery** del lado del cliente][3]
  * [Hacer uso de la tecnología **Ajax** para mandar los datos al **script PHP** sin recargar la pagina][4]
  * [Realizar validaciones con **PHP** del lado del servidor][5]
  * [Finalmente enviar el mensaje a un mail][6]

**Ajax**, acrónimo de **A**synchronous **J**avaScript **A**nd **X**ML (JavaScript asíncrono y XML), es una técnica de desarrollo web para crear aplicaciones interactivas o RIA (Rich Internet Applications). Estas aplicaciones se ejecutan en el cliente, es decir, en el navegador de los usuarios mientras se mantiene la comunicación asíncrona con el servidor en segundo plano. De esta forma es posible realizar cambios sobre las páginas sin necesidad de recargarlas, lo que significa aumentar la interactividad, velocidad y usabilidad en las aplicaciones.

**Ajax** es una tecnología asíncrona, en el sentido de que los datos adicionales se requieren al servidor y se cargan en segundo plano sin interferir con la visualización ni el comportamiento de la página. JavaScript es el lenguaje interpretado (scripting language) en el que normalmente se efectúan las funciones de llamada de Ajax mientras que el acceso a los datos se realiza mediante [XMLHttpRequest][7], objeto disponible en los navegadores actuales. En cualquier caso, no es necesario que el contenido asíncrono esté formateado en XML.

Sabiendo esto, podemos decir que el propósito general de la tecnología ajax es enviar y recibir información sin que el navegador tenga que refrescar la pagina y por ende el usuario interrumpir su navegación :).

Hoy en día para hacer uso de esta tecnología tenemos varias opciones, la primera, a la antigua seria escribiendo el código en javascript tal cual, las segunda que es mucho mas sencilla seria hacer uso de alguna librería como **Jquery**, la libreria **jquery** implementa métodos que nos facilitan mucho la vida a la hora de enviar y recibir información asíncronamente. Sin embargo como el propósito principal de este tutorial es aprender lo aremos de la manera fea (old school) es decir, sin librería :p.

tenemos el siguiente archivo **funciones.js**

```GDScript
// Variables para setear
onload=function() 
{

	divTransparente=document.getElementById("transparencia");
	divMensaje=document.getElementById("transparenciaMensaje");
	form=document.getElementById("formulario");
	urlDestino="mail.php";
	
	claseNormal="input";
	claseError="inputError";
	

	
	preCarga("img/ok.png", "img/loading4.gif", "img/error.png");
}

function preCarga()
{
	imagenes=new Array();
	for(i=0; i=minimo && cantCar<=maximo) return true;
		else return false;
	}
}

function validaCorreo(valor)
{
	var reg=/(^[a-zA-Z0-9._-]{1,30})@([a-zA-Z0-9.-]{1,30}$)/;
	if(reg.test(valor)) return true;
	else return false;
}

function validaForm()
{
	limpiaForm();
	error=0;
	
	var nombre=eliminaEspacios(form.inputNombre.value);

	var web=eliminaEspacios(form.inputWeb.value);
	var correo=eliminaEspacios(form.inputCorreo.value);
	var comentarios=eliminaEspacios(form.inputComentario.value);
	
	if(!validaLongitud(nombre, 0, 4, 50)) campoError(form.inputNombre);

	if(!validaLongitud(web, 1, 4, 50)) campoError(form.inputWeb);
	if(!validaCorreo(correo)) campoError(form.inputCorreo);
	if(!validaLongitud(comentarios, 0, 5, 500)) campoError(form.inputComentario);
	
	if(error==1)
	{
		var texto="![Error](img/error.png)Error: Complete los campos necesarios.Ok";
		muestraMensaje(texto);
	}
	else
	{
		var texto="![Enviando](img/loading4.gif)Enviando. Por favor espere.Ocultar";
		muestraMensaje(texto);
		
		var ajax=nuevoAjax();
		ajax.open("POST", urlDestino, true);
		ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		ajax.send("nombre="+nombre+"&web="+web+"&correo="+correo+"&comentarios="+comentarios);
		
		ajax.onreadystatechange=function()
		{
			if (ajax.readyState==4)
			{
				var respuesta=ajax.responseText;
				if(respuesta=="OK")
				{
					var texto="![Ok](img/ok.png)Gracias por su mensaje.Le responderemos a la brevedad.Ok";
				}
				else var texto="![](img/error.png)Error: intente más tarde.Ok";
				
				muestraMensaje(texto);
			}
		}
	}
}
// Mensajes de ayuda

if(navigator.userAgent.indexOf("MSIE")>=0) navegador=0;
else navegador=1;

```

A continuación explicare que es lo que hace cada bloque de código, las primeras instrucciones a ejecutar, una vez cargado los archivos de JavaScript y la pagina serian las que están dentro del método **onload** y que en Jquery seria equivalente a 

```Text only
jQuery(document).ready(function(){});
```

La función de la que hablamos es:

```GDScript
onload=function() 
{

	divTransparente=document.getElementById("transparencia");
	divMensaje=document.getElementById("transparenciaMensaje");
	form=document.getElementById("formulario");
	urlDestino="mail.php";
	
	claseNormal="input";
	claseError="inputError";
	

	
	preCarga("img/ok.png", "img/loading4.gif", "img/error.png");
}
```

Lo que hacemos básicamente es guardar las referencias a los elementos del DOM (Document Object Map) en variables para mas tarde poder utilizarlas, indicamos el archivo php que procesara la petición que envié nuestro formulario por medio de **ajax** (urlDestino="mail.php";), si tu archivo se llamara de otra forma ahí tendrías que modificar el nombre, y por ultimo utilizamos la función preCargar a la cual le pasamos 3 strings (que son rutas de imágenes).

```Matlab
function preCarga()
{
	imagenes=new Array();
	for(i=0; i

Esta función es muy pequeña y lo que hace es pre cargar las imágenes que le pasemos antes de que sean mostradas al usuario, esto con finalidades de estética del formulario, realice un post aparte que explica un poco mas sobre esto [Precargar imágenes con Jquery][8]

Y ahora viene la función mas importante, donde se realiza toda la transacción y esa es **validaForm()**, si recuerdan en el botón de submit de nuestro formulario tenemos una instrucción OnClick

Enviar Formulario

vuelvo a repetir, este tipo de técnicas ya no son muy utilizadas, ya que desde **Jquery** fácilmente podríamos capturar el evento submit del formulario, pero siempre es bueno conocer las bases de las nuevas tecnologías.

La función tiene el siguiente código

function validaForm()
{
	limpiaForm();
	error=0;
	
	var nombre=eliminaEspacios(form.inputNombre.value);

	var web=eliminaEspacios(form.inputWeb.value);
	var correo=eliminaEspacios(form.inputCorreo.value);
	var comentarios=eliminaEspacios(form.inputComentario.value);
	
	if(!validaLongitud(nombre, 0, 4, 50)) campoError(form.inputNombre);

	if(!validaLongitud(web, 1, 4, 50)) campoError(form.inputWeb);
	if(!validaCorreo(correo)) campoError(form.inputCorreo);
	if(!validaLongitud(comentarios, 0, 5, 500)) campoError(form.inputComentario);
	
	if(error==1)
	{
		var texto="![Error](img/error.png)Error: Complete los campos necesarios.Ok";
		muestraMensaje(texto);
	}
	else
	{
		var texto="![Enviando](img/loading4.gif)Enviando. Por favor espere.Ocultar";
		muestraMensaje(texto);
		
		var ajax=nuevoAjax();
		ajax.open("POST", urlDestino, true);
		ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		ajax.send("nombre="+nombre+"&web="+web+"&correo="+correo+"&comentarios="+comentarios);
		
		ajax.onreadystatechange=function()
		{
			if (ajax.readyState==4)
			{
				var respuesta=ajax.responseText;
				if(respuesta=="OK")
				{
					var texto="![Ok](img/ok.png)Gracias por su mensaje.Le responderemos a la brevedad.Ok";
				}
				else var texto="![](img/error.png)Error: intente más tarde.Ok";
				
				muestraMensaje(texto);
			}
		}
	}
}


### Validando

En las primeras líneas realizamos validaciones con funciones previamente definidas como **validaLongitud** y **validaCorreo**, esas funciones son muy sencillas y básicamente lo que harán serán regresar **true** o **false** dependiendo de si se cumplen o no las condiciones definidas, esto con el fin de saber si debemos de enviar o no el formulario, echemos un vistazo a la función **validaLongitud**.

function validaLongitud(valor, permiteVacio, minimo, maximo)
{
	var cantCar=valor.length;
	if(valor=="")
	{
		if(permiteVacio) return true;
		else return false;
	}
	else
	{
		if(cantCar>=minimo && cantCar<=maximo) return true;
		else return false;
	}
}

function campoError(campo)
{
	campo.className=claseError;
	error=1;
}

La función recibe 4 parámetros, el string (valor, lo que queremos comprobar), dato para ver si es valido que el campo sea nulo, la longitud mínima y la longitud máxima, con la línea:

var cantCar=valor.length;

obtenemos la cantidad de caracteres del stringa a evaluar y lo comparamos mas abajo en las condicionales, después utilizaremos una función llamada campoError que pondrá en 0 o 1 la variable Error dependiendo del resultado de la evaluación.

Si Error es igual a 1 significa que algo anda mal y entonces mostramos un mensaje de aviso al usuario

if(error==1)
	{
		var texto="![Error](img/error.png)Error: Complete los campos necesarios.Ok";
		muestraMensaje(texto);
	}
	else
	{

Como pueden observar en el código, guardamos un trozo de instrucciones en HTML en una variable la cual es pasada a una función llamada **muestraMensaje**

function muestraMensaje(mensaje)
{
	divMensaje.innerHTML=mensaje;
	divTransparente.style.display="block";
}

Este método es el responsable de que aparezca el mensaje de alerta en el formulario.

### Enviando la petición

Por el contrario si todo va bien entonces las instrucciones que el navegador ejecutara serán las siguientes:

var texto="![Enviando](img/loading4.gif)Enviando. Por favor espere.Ocultar";
		muestraMensaje(texto);
		
		var ajax=nuevoAjax();
		ajax.open("POST", urlDestino, true);
		ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		ajax.send("nombre="+nombre+"&web="+web+"&correo="+correo+"&comentarios="+comentarios);
		
		ajax.onreadystatechange=function()
		{
			if (ajax.readyState==4)
			{
				var respuesta=ajax.responseText;
				if(respuesta=="OK")
				{
					var texto="![Ok](img/ok.png)Gracias por su mensaje.Le responderemos a la brevedad.Ok";
				}
				else var texto="![](img/error.png)Error: intente más tarde.Ok";
				
				muestraMensaje(texto);
			}
		}

Guardamos la porción de código **html** en la variable texto, después se ejecuta la función **nuevoAjax()**, la cual prepara el HTTP request Object para posteriormente ser utilizado como podemos observar en las lineas.

ajax.open("POST", urlDestino, true);
		ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		ajax.send("nombre="+nombre+"&web="+web+"&correo="+correo+"&comentarios="+comentarios);

Donde indicamos el método de envió de datos (GET o POST), el destino y el tipo de petición, es decir asíncrono, con el método send indicamos los parámetros que enviaremos, es decirlos datos que introdujo el usuario en el formulario.

Después de preparar la petición siguen validación del estado de la petición (ajax.readyState==4), si el mensaje fue entregado o no, etc. Para saber mucho mas afondo de como funciona XMLHttpRequest les recomiendo lean la siguiente documentación [XMLHttpRequest][9].

Recibimos la respuesta de nuestro script **php** y dependiendo de si el mensaje fue entregado correctamente (un OK) o hubo algún error en la transmisión mostramos un mensaje al usuario

var respuesta=ajax.responseText;
				if(respuesta=="OK")
				{
					var texto="![Ok](img/ok.png)Gracias por su mensaje.Le responderemos a la brevedad.Ok";
				}
				else var texto="![](img/error.png)Error: intente más tarde.Ok";
				
				muestraMensaje(texto);

Hasta aquí llega esta parte!, ya casi terminamos 🙂


  El siguiente paso es [Realizar validaciones con PHP del lado del servidor](http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-5)


 [1]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-1
 [2]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-2
 [3]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-3
 [4]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-4
 [5]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-5
 [6]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-6
 [7]: http://es.wikipedia.org/wiki/XMLHttpRequest
 [8]: http://www.alevsk.com/2011/05/precargar-imagenes-con-jquery/
 [9]: http://www.w3.org/TR/XMLHttpRequest/
```
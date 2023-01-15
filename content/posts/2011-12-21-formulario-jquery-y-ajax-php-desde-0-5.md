---
title: 'Formulario Jquery y Ajax desde 0 [PHP]'
author: Alevsk
type: post
date: 2011-12-21T05:58:12+00:00
url: /2011/12/formulario-jquery-y-ajax-php-desde-0-5/
categories:
  - CSS
  - Diseño
  - HTML
  - Javascript
  - Jquery
  - Programming
  - Tips
  - Tutorials
tags:
  - Hello world
  - Javascript
  - Jquery
  - php
  - Programming
  - Solutions
  - Technology
  - Tutorials
  - web

---
[![](/images/tuto_form.jpg)](http://www.alevsk.com/2011/01/formulario-jquery-y-ajax-php-desde-0-1/tuto_form/)

Muy bien, si haz llegado hasta esta parte del tutorial te felicito, ya casi acabas el formulario, en los post anteriores hicimos las validaciones del lado del cliente, ahora toca hacer las validaciones del lado del servidor y **enviar el correo** utilizando **PHP**.

Los post del tutorial son los siguientes:

  * [Crear un formulario 2.0 usando **CSS** y HTML][1]
  * [Usando Jquery para darle vida a nuestro formulario][2]
  * [Realizar validaciones con **Jquery** del lado del cliente][3]
  * [Hacer uso de la tecnología **Ajax** para mandar los datos al **script PHP** sin recargar la pagina][4]
  * [Realizar validaciones con **PHP** del lado del servidor][5]
  * [Finalmente enviar el mensaje a un mail][6]

Es un hecho que al final del día no podemos confiar en los usuarios que utilizaran la aplicación (suena mal, pero así es), existen practicas de seguridad que son básicas como por ejemplo asegurarnos que los datos que recibimos sean correctos, es decir si pedimos que el usuario ingrese un correo electrónico sea un correo electrónico valido, etc.

Tenemos que crear un nuevo archivo php, asegúrate de que el nombre sea el mismos que el que indicaste en el javascript

```Transact-SQL
=$minimo && $cantCar<=$maximo) return TRUE;
		else return FALSE;
	}
}

function validaCorreo($valor)
{
	if(eregi("([a-zA-Z0-9._-]{1,30})@([a-zA-Z0-9.-]{1,30})", $valor)) return TRUE;
	else return FALSE;
}

// MAIN	

if($_POST)
{
	foreach($_POST as $clave => $valor) $$clave=addslashes(trim(utf8_decode($valor)));
	sleep(5);
	if(!validaLongitud($nombre, 0, 4, 50)) $error=1;
	if(!validaLongitud($web, 1, 4, 50)) $error=1; 
	if(!validaCorreo($correo)) $error=1;
	if(!validaLongitud($comentarios, 0, 5, 500)) $error=1;
	
	if($error==1) echo "Error";
	else
	{
		$fecha=date("d/m/y - H:i");
		$mensaje="
Tienes un nuevo mensaje desde el Sitio:

Fecha: $fecha
Nombre: $nombre
Sitio web: $web
Correo electrónico: $correo
Comentarios: $comentarios";

		//Debug en un archivo ... probando haber si imprime
		
		/*$master=fopen('mensajes.txt',a);
		fwrite($master,",".$fecha.",".$nombre.",".$web.",".$correo.",".$comentarios);
		fclose($master);*/
		
		mail("fulano@hotmail.com", "Comentario desde la Web", $mensaje, "From: Sitio Web ");
		echo "OK";
	}
}
?>

```

Ok, explicare el código paso por paso, al inicio del script hay 2 funciones que se utilizaran mas abajo, lo importante comienza donde esta el

```Tera Term macro
if($_POST)
{

```

Estamos indicando que si el arreglo asociativo $_POST no esta vacío entonces ejecutaremos el código entre las llaves. La primera línea

```Text only
foreach($_POST as $clave => $valor) $$clave=addslashes(trim(utf8_decode($valor)));

```

Foreach lo que hace es recorre el array y crear una variable por cada valor que encuentre y le asigna como nombre el mismo (similar a si utilizáramos extract($_POST); o algo similar), además de eso por seguridad le aplica la función trim que elimina espacios en blanco al inicio y al final y addslashes que agrega barras invertidas en caso de encontrar caracteres extraños como comillas simple.

Ahora realizamos las validaciones haciendo uso de las funciones de arriba

```Tera Term macro
if(!validaLongitud($nombre, 0, 4, 50)) $error=1;
	if(!validaLongitud($web, 1, 4, 50)) $error=1; 
	if(!validaCorreo($correo)) $error=1;
	if(!validaLongitud($comentarios, 0, 5, 500)) $error=1;

```

Las funciones validaLongitud y validaCorreo son muy similares a las que hicimos anteriormente en Javascript 🙂

```Matlab
function validaLongitud($valor, $permiteVacio, $minimo, $maximo)
{
	$cantCar = strlen($valor);
	if(empty($valor))
	{
		if($permiteVacio) return TRUE;
		else return FALSE;
	}
	else
	{
		if($cantCar>=$minimo && $cantCar<=$maximo) return TRUE;
		else return FALSE;
	}
}

```

La **función** recibe 4 parámetros, el valor, una variable para ver si puede estar vacía, una longitud mínima y una máxima, después obtenemos la longitud de la cadena, revisamos si la variable esta vacía y de ser así vemos si esta permitido que lo este, de ser verdadero esto regresamos true, por el otro lado si la variable no viene vacía tenemos que ver que la longitud cumpla con la longitud mínima y máxima, en cado de cumplirse la condición regresamos verdadero.

```Matlab
function validaCorreo($valor)
{
	if(eregi("([a-zA-Z0-9._-]{1,30})@([a-zA-Z0-9.-]{1,30})", $valor)) return TRUE;
	else return FALSE;
}

```

En esta **función** solamente se evalúa con la función **eregi** que la cadena **$valor** cumpla con las condiciones de la expresion regular, de ser cierto devolvemos true, de lo contrario false, no hay nada mas que decir.

Esta demás decir que dependiendo de si el resultado de las validaciones es verdadero o falso pondremos un 1 o dejaremos en 0 la variable $error.

Después revisamos si hubo algún error (si error es igual a 1), de ser así imprimimos con echo error, si no hubo errores procedemos a enviar el mensaje con el siguiente código.

```Transact-SQL
if($error==1) echo "Error";
	else
	{
		$fecha=date("d/m/y - H:i");
		$mensaje="
Tienes un nuevo mensaje desde el Sitio:

Fecha: $fecha
Nombre: $nombre
Sitio web: $web
Correo electrónico: $correo
Comentarios: $comentarios";

		//Debug en un archivo ... probando haber si imprime
		
		/*$master=fopen('mensajes.txt',a);
		fwrite($master,",".$fecha.",".$nombre.",".$web.",".$correo.",".$comentarios);
		fclose($master);*/
		
		mail("CORREO EJ. fulano@hotmail.com", "Comentario desde la Web", $mensaje, "From: Sitio Web ");
		echo "OK";
	}


```

Lo que hacemos básicamente es armar el cuerpo del mensaje, después utilizar la función mail

```Transact-SQL
mail("fulano@hotmail.com", "Comentario desde la Web", $mensaje, "From: Sitio Web ");

```

La función mail envía un mensaje de acuerdo a parámetros recibidos, mas adelante aprenderemos que hay maneras mas sofisticadas de enviar correo electrónico con todas las cabeceras en orden, pero por el momento esta bien de esta manera.

Al final para avisarle al javascript (el cual hizo la petición ajax) que todo ha ido bien regresamos un OK 🙂

Y listo con esto el mensaje ha sido enviado!

<div class="demobox" style="height: auto;">
  El ultimo paso es [ Finalmente enviar el mensaje a un mail y la despedida
](http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-6)</div>

 [1]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-1
 [2]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-2
 [3]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-3
 [4]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-4
 [5]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-5
 [6]: http://www.alevsk.com/formulario-jquery-y-ajax-php-desde-0-6
---
title: Link en un DIV con Jquery
author: Alevsk
type: post
date: 2011-04-21T02:59:58+00:00
url: /2011/04/link-en-un-div-jquery/
categories:
  - CSS
  - Javascript
  - Jquery
  - Tips
  - Tutorials
tags:
  - CSS
  - Javascript
  - Jquery
  - Social Media
  - software libre
  - Solutions
  - Tutorials

---
[![](/images/div.jpg)](http://www.alevsk.com/2011/04/link-en-un-div-jquery/div/)

Hola lectores :), en esta ocasión me da mucho gusto escribir, ya que aunque en este momento estoy muy cansado (vengo llegando del trabajo) logramos terminar todo lo que teníamos que hacer junto con el equipo de desarrolladores :).

Ahora si de lo que trata este post es lo siguiente, un pequeño truco con **jquery** pero que es muy útil es encontrar elementos dentro de otros elementos que hayamos elegido con nuestro selector, queremos hacer que un **div** sea clickeable, ¿para que nos puede servir esto?, podemos diseñar bonitos botones y agregarle todo el CSS y el diseño que queramos y no estar solamente limitados a que sea un link comun y corriente.

El código **Javascript** para hacer eso es el siguiente:

```Tera Term macro
$(".myBox").click(function(){
     window.location=$(this).find("a").attr("href");
     return false;
});

```

Aqui estamos indicando que cuando se haga click en nuestro div con clase **mybox**

```Text only

  
```
<p>
    la pagina sera redireccionada (<strong>window.location</strong>) al valor que tenga el atributo <strong>href</strong> del elemento <strong>a</strong> (<strong>un link</strong>) que este contenido dentro del <strong>div</strong> :), si nuestro <strong>div</strong> no tuviera una clase sino un <strong>id</strong> (identificador) entonces quedaría de la siguiente forma:
  </p>
```Tera Term macro

$("#myBox").click(function(){
     window.location=$(this).find("a").attr("href");
     return false;
});

```
<p>
<strong>#</strong> = identificadores, <strong>.</strong> = clases.
  </p>
<p>
    Y por ultimo el <strong>html</strong> seria algo como esto:
  </p>
```Transact-SQL




  Texto del boton
      [link](http://google.com)
  


```
<p>
    Si quisieran mostrar solamente el texto dentro del <strong>div</strong> y no el <strong>link</strong> podrían el siguiente código en su hoja de estilos
  </p>
```GAS

.mybox a
{
     display:none;
}

```
<p>
    Con lo anterior el <strong>link</strong> quedaría invisible y solo se visualizaría el texto.
  </p>
<p>
    salu2
  </p>
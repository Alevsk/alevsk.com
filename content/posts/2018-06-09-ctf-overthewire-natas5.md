---
title: 'CTF OverTheWire: Natas5'
author: Alevsk
type: post
date: 2018-06-09T07:31:07+00:00
url: /2018/06/ctf-overthewire-natas5/
categories:
  - Ethical Hacking
  - Javascript
  - Personal
  - Programming
  - Technology
  - Tutorials
tags:
  - capture the flag
  - ctf
  - hacking
  - Ethical Hacking
  - owasp

---
[![](/images/Screen-Shot-2018-05-29-at-1.57.38-AM-1200x596.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-1-57-38-am/)

Continuamos con la serie de tutoriales del [CTF Natas](http://overthewire.org/wargames/natas/), ahora toca el turno de [natas5](http://overthewire.org/wargames/natas/natas5.html).

```bash
Natas Level 4 → Level 5  
Username: natas5  
URL: http://natas5.natas.labs.overthewire.org
```

Utilizamos la bandera obtenida en el reto anterior y accedemos a la URL indicada en las instrucciones del reto, veremos una pantalla como la siguiente.

[![](/images/Screen-Shot-2018-06-09-at-1.58.29-AM-1200x347.png)](http://www.alevsk.com/2018/06/ctf-overthewire-natas5/screen-shot-2018-06-09-at-1-58-29-am/)

> Acceso deshabilitado. No estas autenticado

Generalmente cuando te autenticas en un sitio web el servidor crea una sesión en memoria/base de datos/archivos/etc… y genera una [cookie de sesión](https://en.wikipedia.org/wiki/HTTP_cookie) que es retornada al usuario, esta cookie puede ser incluida en las siguientes peticiones y de esta forma el servidor nos puede identificar mas rápido ([HTTP stateless protocol](https://stackoverflow.com/questions/13200152/why-say-that-http-is-a-stateless-protocol)).

Procedemos a revisar las cookies de la pagina web, si utilizas [chrome](https://www.google.com/chrome/) lo puedes hacer desde la [google developer toolbar](https://developers.google.com/web/tools/chrome-devtools/) en la pestaña de aplicación

[![](/images/Screen-Shot-2018-06-09-at-2.08.59-AM-1200x262.png)](http://www.alevsk.com/2018/06/ctf-overthewire-natas5/screen-shot-2018-06-09-at-2-08-59-am/)

Inmediatamente vemos que hay una cookie llamada **loggedin** con un valor de **cero**, lo cambiamos a **uno** (1) y refrescamos la pagina.

[![](/images/Screen-Shot-2018-06-09-at-2.17.27-AM-1200x380.png)](http://www.alevsk.com/2018/06/ctf-overthewire-natas5/screen-shot-2018-06-09-at-2-17-27-am/)

La bandera para acceder a **natas6** es **aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1**

> Al igual que en el reto anterior, esta pagina tiene una vulnerabilidad de [broken access control](https://www.owasp.org/index.php/Top_10-2017_A5-Broken_Access_Control) puesto que es posible engañar al servidor con tan solo modificar el valor de la cookie loggedin

Happy hacking 🙂
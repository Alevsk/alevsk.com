---
title: 'CTF OverTheWire: Natas6'
author: Alevsk
type: post
date: 2018-08-17T22:21:42+00:00
url: /2018/08/ctf-overthewire-natas6/
categories:
  - Ethical Hacking
  - IT News
  - Personal
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - capture the flag
  - ctf
  - hackers
  - hacking
  - Linux
  - Programming
  - Tutorials
  - web

---
[![](/images/Screen-Shot-2018-05-29-at-1.57.38-AM-1200x596.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-1-57-38-am/)

Continuamos con la serie de tutoriales del [CTF Natas](http://overthewire.org/wargames/natas/), ahora toca el turno de [natas6](http://overthewire.org/wargames/natas/natas6.html).

```bash
Natas Level 5 → Level 6  
Username: natas6  
URL: http://natas6.natas.labs.overthewire.org
```

Utilizamos la bandera obtenida en el reto anterior y accedemos a la URL indicada en las instrucciones del reto, veremos una pantalla como la siguiente.

[![](/images/Screen-Shot-2018-08-17-at-4.58.09-PM-1200x461.png)](http://www.alevsk.com/2018/08/ctf-overthewire-natas6/screen-shot-2018-08-17-at-4-58-09-pm/)

Es solo un formulario donde nos piden ingresar una contraseña o secreto, al introducir cualquier cosa obtenemos un mensaje de error.

[![](/images/Screen-Shot-2018-08-17-at-4.58.58-PM-1200x480.png)](http://www.alevsk.com/2018/08/ctf-overthewire-natas6/screen-shot-2018-08-17-at-4-58-58-pm/)

En la misma pagina hay un enlace que dice **view sourcecode** (ver código fuente), damos clic y veremos lo siguiente.

[![](/images/Screen-Shot-2018-08-17-at-5.02.25-PM-1160x800.png)](http://www.alevsk.com/2018/08/ctf-overthewire-natas6/screen-shot-2018-08-17-at-5-02-25-pm/)

La parte importa es:

```php
<?

include "includes/secret.inc";

if(array\_key\_exists("submit", $_POST)) {  
if($secret == $_POST['secret']) {  
print "Access granted. The password for natas7 is <censored>";  
} else {  
print "Wrong secret";  
}  
}  
?>
```

Es un código php muy sencillo, podemos ver que obtiene un parámetro via POST (el que enviamos mediante el formulario) y lo compara con la variable **$secret**, ademas hace include de un archivo interesante **includes/secret.inc**

Accedemos a ese archivo usando el navegador.

[![](/images/Screen-Shot-2018-08-17-at-5.05.04-PM.png)](http://www.alevsk.com/2018/08/ctf-overthewire-natas6/screen-shot-2018-08-17-at-5-05-04-pm/)

Y utilizamos el **secret** que acabamos de descubrir en el formulario inicial.

[![](/images/Screen-Shot-2018-08-17-at-5.05.48-PM-1200x522.png)](http://www.alevsk.com/2018/08/ctf-overthewire-natas6/screen-shot-2018-08-17-at-5-05-48-pm/)

La bandera para acceder a **natas7** es **7z3hEENjQtflzgnT29q7wAvMNfZdh0i9**

> En este reto aprovechamos un fallo de seguridad llamado [Source code disclosure](https://www.acunetix.com/blog/articles/source-code-disclosure-dangerous/), en donde tenemos acceso a código que solo debería ser consumido del lado del servidor.

Happy hacking 🙂
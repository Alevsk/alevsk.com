---
title: BurpSuite para desarrolladores
author: Alevsk
type: post
date: 2015-03-10T01:48:43+00:00
url: /2015/03/burpsuite-para-desarrolladores/
categories:
  - Ethical Hacking
  - Personal
  - Technology
  - Tips
  - Tutorials
tags:
  - Hello World
  - Java
  - Personal
  - Programming
  - Solutions
  - Technology
  - Tutorials

---
**BurpSuite** es una herramienta muy popular en el mundo de la seguridad informática, se trata de una completa suite para hacer auditoria y explotación de aplicaciones web, entre sus muchas funcionalidades se encuentra el proxy, el **escáner de vulnerabilidades** y un repetidor de peticiones, entre muchas otras mas.

Una versión gratuita puede ser descargada del siguiente enlace  
[http://portswigger.net/burp/download.html](http://portswigger.net/burp/download.html).

_¿Y ahora que? ¿Que tiene que ver una herramienta de seguridad informática en un trabajo de desarrollo de software?_

## Lo mejor de ambos mundos

Muchas veces cuando estamos desarrollando aplicaciones móviles complejas, es decir que requieren de algún mecanismo de comunicación con servicios web podemos llegar a retrasarnos y tener problemas debido a que no tenemos una manera clara y eficiente de saber que es lo que esta enviando y recibiendo en la app, el **debugger** de **Android Studio** siempre funciona y es de bastante utilidad pero no es una herramienta especializada para interceptar paquetes de red.

Lo que vamos a hacer es, una vez que hayamos instalado **BurpSuit**, ya sea para Windows, Linux o Mac, lo ejecutamos, como el ejecutable es un .jar requerimos Java para correrlo por lo que si no lo tenemos deberíamos también descargarlo e instalarlo.

[![burp_2](/images/burp_2.png)](http://www.alevsk.com/2015/03/burpsuite-para-desarrolladores/burp_2/)

Ya en **BurpSuite** la opción que nos interesa es la de proxy, así que hacemos clic en la pestaña y después nos vamos a opciones, tendremos una interfaz similar a la siguiente.

[![burp_1](/images/burp_1.png)](http://www.alevsk.com/2015/03/burpsuite-para-desarrolladores/burp_1/)

Por default BurpSuite solo esta escuchando conexiones de localhost (127.0.0.1) por lo que para interceptar peticiones de otros usuarios de nuestra red debemos agregar un nuevo listener, hacemos clic en el botón que dice **Add** y seleccionamos **All interfaces**, finalmente escribimos un puerto diferente al **8080** asignado por default al primer listener, por ejemplo **8085**.

[![burp_3](/images/burp_3.png)](http://www.alevsk.com/2015/03/burpsuite-para-desarrolladores/burp_3/)

Damos clic en el botón de OK y en la pestaña de Alerts, en los Logs BurpSuite nos indicara que el nuevo listener ya esta corriendo.

[![burp_4](/images/burp_4.png)](http://www.alevsk.com/2015/03/burpsuite-para-desarrolladores/burp_4/)

Lo siguiente será obtener la dirección de ip asignada a nuestra maquina, eso depende de que sistema operativo estemos usando y no es difícil encontrarla, utilicen Google para investigar mas al respecto.

[![burp_5](/images/burp_5.png)](http://www.alevsk.com/2015/03/burpsuite-para-desarrolladores/burp_5/)

Tomamos esa dirección y la guardamos, **192.168.43.204**, ya que mas tarde la necesitaremos.

Ahora en nuestro dispositivo, para este ejemplo yo utilizo Android, pero hoy en dia cualquier Smartphone, ya sea Android, iOS, Windows Phone o BlackBerry tienen una opción para configurar proxy, en ese apartado debemos colocar la ip de nuestro **servidor proxy** junto con el puerto en el que escucha.

[![burp_8](/images/burp_8.png)](http://www.alevsk.com/2015/03/burpsuite-para-desarrolladores/burp_8/)

Esperamos un par de segundos y comenzamos a interactuar con nuestra aplicación en desarrollo, si todo quedo bien configurado deberíamos comenzar a interceptar las peticiones de nuestra aplicación en **BurpSuite**.

[![burp_6](/images/burp_6.png)](http://www.alevsk.com/2015/03/burpsuite-para-desarrolladores/burp_6/)

Ahora podemos ver los las cabeceras y los parámetros que estamos enviando y revisar que es lo que esta fallando en nuestra **aplicación** de manera mas cómoda.

[![burp_7](/images/burp_7.png)](http://www.alevsk.com/2015/03/burpsuite-para-desarrolladores/burp_7/)

Para interceptar **comunicaciones seguras con SSL** en **BurpSuite** hacen falta un par de pasos de configuración extra, pero nada del otro mundo, se los dejo de tarea o tal vez publique un tutorial al respecto en un post futuro.

Nota: No olvides quitar la configuración del proxy en tu Smartphone una vez que termines las pruebas, ya que si apagas tu computadora te quedaras sin acceso a internet.
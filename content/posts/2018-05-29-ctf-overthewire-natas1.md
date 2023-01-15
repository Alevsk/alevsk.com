---
title: 'CTF OverTheWire: Natas1'
author: Alevsk
type: post
date: 2018-05-29T07:04:08+00:00
url: /2018/05/ctf-overthewire-natas1/
categories:
  - Ethical Hacking
  - Javascript
  - IT News
  - Personal
  - Tips
  - Tutorials
tags:
  - capture the flag
  - ctf
  - hacking
  - Ethical Hacking

---
[![](/images/Screen-Shot-2018-05-29-at-1.57.38-AM-1200x596.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-1-57-38-am/)

En el articulo anterior, [OWASP – Riviera Maya e introducción a Overthewire CTF][1], comenzamos con una breve introducción a los CTFs y resolvimos **Natas0**, con la bandera que obtuvimos ahora toca el turno de Natas1, el nivel es muy similar pero tiene algo que lo hace diferente.

# Natas1

```bash
Natas Level 0 → Level 1  
Username: natas1  
URL: http://natas1.natas.labs.overthewire.org
```

Vamos a la URL del reto, [http://natas1.natas.labs.overthewire.org](http://natas1.natas.labs.overthewire.org), ingresamos **natas1** como username, la bandera obtenida en el reto anterior como contraseña y veremos la siguiente pantalla.

[![](/images/Screen-Shot-2018-05-29-at-12.55.46-AM-1200x411.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-12-55-46-am/)

si intentamos hacer lo mismo que en el reto anterior, _click derecho > ver código fuente_, nos aparece un [alert](https://www.w3schools.com/jsref/met_win_alert.asp) de Javascript indicando que el clic derecho esta deshabilitado.

[![](/images/Screen-Shot-2018-05-29-at-12.56.01-AM-1200x421.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-12-56-01-am/)

Ok, hay código javascript que bloquea la acción de click derecho, sin embargo conocemos otras formas de acceder al código fuente de un sitio web, por ejemplo usando shortcuts (alt + command + U en mac, etc.) o con [CURL](https://en.wikipedia.org/wiki/CURL)

CURL es un cliente para linea de comandos que nos permite enviar o recibir datos utilizando distintos protocolos, entre ellos [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol), abrimos una consola y escribimos el siguiente comando (en Windows **CURL** no esta instalado por default, pero podemos utilizar esta solución [https://curl.haxx.se/download.html](https://curl.haxx.se/download.html))

```bash
$ curl -u natas1:gtVrDuiDfck831PqWsLEZy5gyDz1clto http://natas1.natas.labs.overthewire.org
``` 

El parámetro **-u** nos permite definir credenciales para autenticarnos ante el servidor.

[![](/images/Screen-Shot-2018-05-29-at-1.30.33-AM-1200x677.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-1-30-33-am/)

CURL nos muestra el código fuente de la **URL** que le indicamos, también podemos ver el código javascript que bloquea el clic derecho y la solución de este reto.

```html
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">
```

La bandera para acceder a **natas2** es **ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi**

> * Aprendimos que hay otras formas de consumir una pagina web ademas de los navegadores que normalmente usamos (firefox, chrome, ie, safari, etc)

Happy hacking 🙂

 [1]: https://www.alevsk.com/2018/05/owasp-riviera-maya-2018/</body>
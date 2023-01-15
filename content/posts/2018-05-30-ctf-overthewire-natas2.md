---
title: 'CTF OverTheWire: Natas2'
author: Alevsk
type: post
date: 2018-05-30T04:53:47+00:00
url: /2018/05/ctf-overthewire-natas2/
categories:
  - Ethical Hacking
  - IT News
  - Personal
  - Technology
  - Tutorials
tags:
  - capture the flag
  - ctf
  - hacking
  - Ethical Hacking

---
[![](/images/Screen-Shot-2018-05-29-at-1.57.38-AM-1200x596.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-1-57-38-am/)

Continuamos con la serie de tutoriales del [CTF Natas](http://overthewire.org/wargames/natas/), ahora toca el turno de [natas2](http://natas2.natas.labs.overthewire.org).

```bash
Natas Level 1 → Level 2  
Username: natas2  
URL: http://natas2.natas.labs.overthewire.org
```

Al igual que en los artículos anteriores, utilizamos la bandera obtenida en el reto anterior y accedemos a la URL indicada en las instrucciones del reto, veremos una pantalla como la siguiente.

[![](/images/Screen-Shot-2018-05-29-at-10.59.29-PM-1200x410.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas2/screen-shot-2018-05-29-at-10-59-29-pm/)

Repetimos lo que nos ha funcionado hasta ahora e inspeccionamos el código fuente de la pagina.

[![](/images/Screen-Shot-2018-05-29-at-11.05.32-PM-1200x458.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas2/screen-shot-2018-05-29-at-11-05-32-pm/)

Efectivamente no vemos nada que haga referencia al password / bandera para acceder a **natas3**, sin embargo algo nos llama la atención, hay una imagen png de un pixel en el documento, eso es algo nuevo.

La imagen por si misma no es nada especial, [http://natas2.natas.labs.overthewire.org/files/pixel.png](http://natas2.natas.labs.overthewire.org/files/pixel.png), pero la ruta donde esta alojada si 🙂 así que visitamos la URL [http://natas2.natas.labs.overthewire.org/files/](http://natas2.natas.labs.overthewire.org/files/) y **voilà**.

[![](/images/Screen-Shot-2018-05-29-at-11.35.29-PM.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas2/screen-shot-2018-05-29-at-11-35-29-pm/)

_Debido a una mala configuración del servidor es posible listar los archivos de directorios que no contengan un index o pagina principal: index.html, index.php, index.jsp, etc. Esta es una vulnerabilidad de revelación de información llamada [Directory Listing](https://cwe.mitre.org/data/definitions/548.html)._

Dentro de **users.txt** encontraremos una lista de usuarios y contraseñas, entre ellos la bandera para acceder al siguiente reto

```bash
# username:password  
alice:BYNdCesZqW  
bob:jw2ueICLvT  
charlie:G5vCxkVV3m  
natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14  
eve:zo4mJWyNj2  
mallory:9urtcpzBmH
```

La bandera para acceder a **natas3** es **sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14**

Happy hacking 🙂
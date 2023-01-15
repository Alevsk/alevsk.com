---
title: 'CTF OverTheWire: Natas7'
author: Alevsk
type: post
date: 2018-12-02T01:07:49+00:00
url: /2018/12/ctf-overthewire-natas7/
categories:
  - Ethical Hacking
  - Linux
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

---
[![](/images/Screen-Shot-2018-05-29-at-1.57.38-AM-1200x596.png)](https://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-1-57-38-am/)

Continuamos con la serie de tutoriales del [CTF Natas](http://overthewire.org/wargames/natas/), ahora toca el turno de [natas7](http://overthewire.org/wargames/natas/natas7.html).

```bash
Natas Level 6 → Level 7  
Username: natas7  
URL: http://natas7.natas.labs.overthewire.org  
```

Utilizamos la bandera obtenida en el reto anterior y accedemos a la URL indicada en las instrucciones del reto, veremos una pantalla como la siguiente.

[![](/images/natas7_1.png)](https://www.alevsk.com/2018/12/ctf-overthewire-natas7/natas7_1/)

Inspeccionamos el código fuente de la pagina y observamos un par de cosas interesantes:

[![](/images/natas7_2.png)](https://www.alevsk.com/2018/12/ctf-overthewire-natas7/natas7_2/)

Vemos dos hypervinculos (index.php?page=home y index.php?page=about) y un comentario que dice:

```html
<!--– hint: password for webuser natas8 is in /etc/natas_webpass/natas8 –-->  
```

Dependiendo el valor del **parámetro page** el contenido de la pagina cambia, todo apunta a que estamos ante una vulnerabilidad de tipo [Local File Inclusion](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#Local_File_Inclusion), escribimos texto aleatorio solo para verificar la vulnerabilidad.

[![](/images/natas7_3.png)](https://www.alevsk.com/2018/12/ctf-overthewire-natas7/natas7_3/)

Efectivamente podemos ver la ruta del archivo php en el servidor ([path disclosure](https://www.owasp.org/index.php/Full_Path_Disclosure)), debido a esta vulnerabilidad podemos leer cualquier archivo al que el usuario que ejecuta el servidor web tenga acceso, por ahora solo nos centraremos en obtener la bandera del reto con [http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8](http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8)
[![](/images/natas7_4.png)](https://www.alevsk.com/2018/12/ctf-overthewire-natas7/natas7_4/)

La bandera para acceder a **natas8** es **DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe**

> En este reto aprovechamos un fallo de seguridad llamado [Local File Inclusion](https://en.wikipedia.org/wiki/File_inclusion_vulnerability#Local_File_Inclusion), con el que es posible leer otros archivos que no son accesibles directamente en el servidor.

Happy hacking 🙂
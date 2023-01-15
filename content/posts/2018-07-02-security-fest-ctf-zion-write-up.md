---
title: 'Security Fest #CTF – Zion write up'
author: Alevsk
type: post
date: 2018-07-02T19:41:14+00:00
url: /2018/07/security-fest-ctf-zion-write-up/
categories:
  - Geek
  - Ethical Hacking
  - Linux
  - Mac
  - Personal
  - Programming
  - Snippets
  - Technology
  - Tips
  - Tutorials
tags:
  - capture the flag
  - ctf
  - hackers
  - hacking
  - Ethical Hacking
  - Linux
  - Programming
  - software libre
  - Solutions
  - Technology

---
Para este reto nos daban un archivo comprimido **zion.tar.gz**, procedemos a descomprimirlo y obtenemos otro archivo llamado **YouKnow**.

[![](/images/Screen-Shot-2018-07-02-at-1.38.14-PM.png)](http://www.alevsk.com/2018/07/security-fest-ctf-zion-write-up/screen-shot-2018-07-02-at-1-38-14-pm/)

El archivo no tiene extension pero utilizamos el comando file para ver que tipo de archivo es.

[![](/images/Screen-Shot-2018-07-02-at-1.40.25-PM.png)](http://www.alevsk.com/2018/07/security-fest-ctf-zion-write-up/screen-shot-2018-07-02-at-1-40-25-pm/)

Parece un archivo de Microsoft Word Office y sabemos que los archivos docx en realidad son archivos en formato zip.

[![](/images/Screen-Shot-2018-07-02-at-1.41.06-PM.png)](http://www.alevsk.com/2018/07/security-fest-ctf-zion-write-up/screen-shot-2018-07-02-at-1-41-06-pm/)

Procedemos a descomprimir **YouKnow**

[![](/images/Screen-Shot-2018-07-02-at-1.53.58-PM.png)](http://www.alevsk.com/2018/07/security-fest-ctf-zion-write-up/screen-shot-2018-07-02-at-1-53-58-pm/)

Obtenemos varios archivos y carpetas, comenzamos a analizarlos de uno por uno, sin embargo no encontramos nada que haga referencia a la bandera del reto. (analice la imagen del conejo con un par de herramientas de esteganografía pero no había nada)

[![](/images/Screen-Shot-2018-07-02-at-1.55.29-PM-1200x450.png)](http://www.alevsk.com/2018/07/security-fest-ctf-zion-write-up/screen-shot-2018-07-02-at-1-55-29-pm/)

Damos un paso atrás y abrimos el archivo **YouKnow** en un editor hexadecimal de su elección, you utilice [Sublime](https://www.sublimetext.com/3)

Observamos la cabecera estándar PK del [formato ZIP](https://en.wikipedia.org/wiki/Zip_(file_format))
[![](/images/Screen-Shot-2018-07-02-at-1.57.57-PM.png)](http://www.alevsk.com/2018/07/security-fest-ctf-zion-write-up/screen-shot-2018-07-02-at-1-57-57-pm/)

Al ir analizando el archivo, hacia el final, algo salta inmediatamente a la vista.

[![](/images/Screen-Shot-2018-07-02-at-2.11.07-PM.png)](http://www.alevsk.com/2018/07/security-fest-ctf-zion-write-up/screen-shot-2018-07-02-at-2-11-07-pm/)

Parece que hay otro archivo Zip concatenado al primero pero los bytes están en orden inverso (observen como el archivo termina en KP, y vemos algunos strings como lmx que seria xml).

Podemos utilizar **python** para invertir los bytes del archivo fácilmente.

[![](/images/Screen-Shot-2018-07-02-at-2.17.21-PM.png)](http://www.alevsk.com/2018/07/security-fest-ctf-zion-write-up/screen-shot-2018-07-02-at-2-17-21-pm/)

```python
open('YouKnow_reversed','wb').write(open('YouKnow','rb').read()[::-1])
```

Obtenemos el archivo con los bytes invertidos y procedemos a descomprimirlo.

[![](/images/Screen-Shot-2018-07-02-at-2.18.03-PM.png)](http://www.alevsk.com/2018/07/security-fest-ctf-zion-write-up/screen-shot-2018-07-02-at-2-18-03-pm/)

Obtenemos nuevamente varios archivos y carpetas.

[![](/images/Screen-Shot-2018-07-02-at-2.21.34-PM.png)](http://www.alevsk.com/2018/07/security-fest-ctf-zion-write-up/screen-shot-2018-07-02-at-2-21-34-pm/)

Y en donde estaba la imagen anterior del conejo rojo ahora encontramos otra imagen, esta vez de un conejo azul que nos muestra la bandera del reto 🙂

[![](/images/Screen-Shot-2018-07-02-at-2.22.23-PM.png)](http://www.alevsk.com/2018/07/security-fest-ctf-zion-write-up/screen-shot-2018-07-02-at-2-22-23-pm/)

La bandera del reto es **sctf{m41nfr4m3\_4cc3ss\_c0d3\_1337\_4lw4s}**

## Bonus

Programe una pequeña herramienta en **python** llamada [reverse bytes](https://github.com/Alevsk/reverse-bytes) para invertir los bytes de un archivo utilizando una cli mas amigable.

```bash
usage: rbytes.py \[-h\] \[-o OUTFILE\] infile

A simple python script for reverse the bytes of a file.

Author: Lenin Alevski Huerta Arias  
Year: 2018

positional arguments:  
infile Input file

optional arguments:  
-h, –help show this help message and exit  
-o OUTFILE, –outfile OUTFILE  
Output file
```

Happy hacking 🙂
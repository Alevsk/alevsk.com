---
title: 'CTF OverTheWire: Natas3'
author: Alevsk
type: post
date: 2018-05-31T06:19:02+00:00
url: /2018/05/ctf-overthewire-natas3/
categories:
  - Ethical Hacking
  - IT News
  - Personal
  - Programming
  - Technology
  - Tutorials
tags:
  - capture the flag
  - ctf
  - hacking
  - Ethical Hacking
  - Programming
  - Technology

---
[![](/images/Screen-Shot-2018-05-29-at-1.57.38-AM-1200x596.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-1-57-38-am/)

Continuamos con la serie de tutoriales del [CTF Natas](http://overthewire.org/wargames/natas/), ahora toca el turno de [natas3](http://natas3.natas.labs.overthewire.org/).

```bash
Natas Level 2 → Level 3  
Username: natas3  
URL: http://natas3.natas.labs.overthewire.org
```

Utilizamos la bandera obtenida en el reto anterior y accedemos a la URL indicada en las instrucciones del reto, veremos una pantalla como la siguiente.

[![](/images/Screen-Shot-2018-05-31-at-12.31.04-AM.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas3/screen-shot-2018-05-31-at-12-31-04-am/)

Inspeccionamos el código fuente de la pagina.

[![](/images/Screen-Shot-2018-05-31-at-12.31.13-AM.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas3/screen-shot-2018-05-31-at-12-31-13-am/)

Parece que se nos acabaron las pistas :S, revisamos el código fuente de la pagina pero no encontramos nada que sugiera cual es la bandera de este reto, también revisamos cada uno de los archivos **js** y **css** en busca de la solución pero no hay resultados. Cada detalle cuenta en este tipo de retos.

Recordando el reto anterior, la bandera se encontraba en un archivo llamado **users.txt** en [http://natas2.natas.labs.overthewire.org/files/users.txt](http://natas2.natas.labs.overthewire.org/files/users.txt). La bandera de este reto podria estar en un archivo similar sin embargo no hay ningún directorio **files**, pero no descartamos la idea por completo, vamos a utilizar una herramienta llamada [dirbuster](https://tools.kali.org/web-applications/dirb) para buscar otros archivos y directorios.

**Dirbuster** es un scanner de contenido web, la herramienta puede ser utilizada para encontrar archivos y directorios de forma automática utilizando diccionarios y fuerza bruta.

[![](/images/Screen-Shot-2018-05-31-at-12.57.38-AM.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas3/screen-shot-2018-05-31-at-12-57-38-am/)

**Dirbuster** nos muestra un archivo interesante, [http://natas3.natas.labs.overthewire.org/robots.txt](http://natas3.natas.labs.overthewire.org/robots.txt) vamos a esa URL y veremos lo siguiente

```bash
User-agent: *  
Disallow: /s3cr3t/
```

> Un archivo robots.txt es un archivo que se encuentra en la raíz de un sitio e indica a qué partes no quieres que accedan los rastreadores de los motores de búsqueda. El archivo utiliza el Estándar de exclusión de robots, que es un protocolo con un pequeño conjunto de comandos que se puede utilizar para indicar el acceso al sitio web por sección y por tipos específicos de rastreadores web (como los rastreadores móviles o los rastreadores de ordenador).

Claramente alguien no quiere que los buscadores indexen el directorio [http://natas3.natas.labs.overthewire.org/s3cr3t/](http://natas3.natas.labs.overthewire.org/s3cr3t/) :), vamos a esa URL a ver que encontramos.

[![](/images/Screen-Shot-2018-05-31-at-1.08.55-AM.png)](http://www.alevsk.com/2018/05/ctf-overthewire-natas3/screen-shot-2018-05-31-at-1-08-55-am/)

Genial, otro archivo [users.txt](http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt), revisamos su contenido.

```bash
natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
```

La bandera para acceder a **natas4** es **Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ**

Happy hacking 🙂
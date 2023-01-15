---
title: Video en Ascii con Mplayer
author: Alevsk
type: post
date: 2011-03-17T15:41:18+00:00
url: /2011/03/video-en-ascii-con-mplayer/
categories:
  - Geek
  - Linux
  - Personal
  - Technology
  - Tips
tags:
  - backtrack
  - Linux Debugging
  - debian
  - distros
  - Linux
  - Personal
  - software libre
  - Tutorials
  - ubuntu

---
[![](/images/linux-geek.jpg)](http://www.alevsk.com/2011/03/video-en-ascii-con-mplayer/linux-geek/)  
Hola lectores, esta vez les quiero mostrar una cosa muy curiosa del reproductor **Mplayer** que encontré mientras investigaba que tipo de parámetros soportaba la aplicación, todo esto para un proyecto que estaba desarrollando de controlar unas pantallas vía una **aplicación web** … pero bueno eso es otra cosa.

Nos vamos directamente a la terminal, la que sea de su preferencia y dependiendo la distribución Linux que usen.  
Y ojo, ya con el reproductor **Mplayer** instalado, si no:

```Text only
sudo apt-get install mplayer
```

Navegan hacia el directorio donde este el video que quieren reproducir y escriben el siguiente comando.

```Text only
mplayer -vo caca video.avi
```

Después de eso se abrirá el programa y comenzara a reproducir el video que le indicaron en forma de texto muy raro, y coloreado, simulando así el vídeo, es muy **cool**, sin embargo la unica utilidad que le he visto hasta ahora es a llegar donde haya un grupo de windowseros y decirles “miren su **Windows Media Player** no puede hacer esto xD".

[![](/images/screenshot23.png)](http://www.alevsk.com/2011/03/video-en-ascii-con-mplayer/screenshot2-4/)

salu2
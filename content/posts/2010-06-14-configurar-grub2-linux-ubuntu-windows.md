---
title: Configure mi GRUB2
author: Alevsk
type: post
date: 2010-06-14T04:14:19+00:00
url: /2010/06/configurar-grub2-linux-ubuntu-windows/
image:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/robuntu-1.jpg
slider_thumbnail:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/thumb-grub.jpg
categories:
  - Geek
  - Linux
  - IT News
  - Personal
  - Programming
  - Technology
  - Tutorials
tags:
  - backtrack
  - campus party
  - debian
  - distros
  - grub
  - hackers
  - Linux
  - Programming
  - software libre
  - Technology
  - ubuntu

---
[![](/images/grub_mint.jpg)](http://www.alevsk.com/2010/06/configurar-grub2-linux-ubuntu-windows/grub_mint/)

Bueno había formateado todos mis discos duros hace ya como 3 meses y tenia a la mano el live de Debian lenny lo iba a instalar pero luego escuche todo el alboroto que traían con Ubuntu Karmic y pues lo instale haber que jeje, mmm los que me conocen saben que yo soy mas bien debianero, pero le quise dar una oportunidad y pues ubuntu esta muy bueno, me siento cómodo ya luego actualice a Lucid Lynx y todo me va bien.

Luego me surgieron algunas otras cosas por las que tuve que usar Windows la mayoria del tiempo :S (Work en IQ-Zone jeje) pero este fin de de semana me di tiempo para acondicionar Linux para lo que ocupo y creo que ya quedo al 100%.

<!--more-->

Una de las primeras cosas que me encontré en esta nueva versión de Ubuntu fue que me reconoció todo el Hardware al instante x'D, cosa por la que sufrí cuando inicie en el mundo de Linux (estas juventudes de hoy la tienen mas fácil jej), otra cosa fue que por default se integra GRUB2, bueno no me tomo mucho tiempo actualizarme y comprender su funcionamiento, a continuación pongo brevemente como configure el mio y ojala les pueda servir a uds.

Les recomiendo la siguiente guía para que entiendan a fondo como trabaja GRUB2 > http://www.guia-ubuntu.org/index.php?title=GRUB#Grub_2

Aquí pongo nada mas lo que a mi me intereso (Recomiendo hagan Backup antes de modificar cualquier archivo, lo pueden hacer copiando x archivo y poniéndole el prefijo **bak_** al nombre, así lo hago yo para reconocerlos al instante =)

  1. El GRUB  muestra varios Kernels para bootear, primero creen una carpeta con x nombre para guardar ahi los kernels, por ejemplo: ```Transact-SQL
alevsk@Aosnet:~$ sudo mkdir /boot/kernels
```

  2. Luego copien  la imagen del Kernel a su carpeta en este caso kernels por ejemplo ```Transact-SQL
alevsk@Aosnet:~$ sudo mv /boot/vmlinuz-2.6.31-20-generic-pae /boot/kernels/
```

  3. De igual manera pueden mover las imágenes que se usan para entrar en el modo de recuperación ```Transact-SQL
alevsk@Aosnet:~$ sudo mv /boot/initrd.img-2.6.31-20-generic-pae /boot/kernels/
```

  4. Al final recuerden que para que los cambios surtan efecto hay que actualizar el grub.cfg que se genera automáticamente ```Transact-SQL
alevsk@Aosnet:~$ sudo update-grub2
```

_Bueno otra cosa que también quise hacer fue ponerle la imagen de fondo, ya saben por cuestión de estética nada mas jeje_

  1. Primero si no lo han hecho descarguense algunas imagenes para el grub ```Transact-SQL
alevsk@Aosnet:~$ sudo apt-get install grub2-splashimages
```

  2. Ahí en la carpeta de **/usr/share/images/grub/** se descargaran, si uds quieren crear las suya propia como yo lo hice, la pueden editar en gimp, redimensionenla a 640 x 480 y guardenla con extensión .png o .tga y metan la a esa misma carpeta.
  3. Luego modifiquen el archivo 05\_debian\_theme en la siguiente ruta (hagan bakup primero por si algo sale mal) ```Transact-SQL
alevsk@Aosnet:~$sudo gedit /etc/grub.d/05_debian_theme
```

  4. Busquen la linea donde dice WALLPAPER=" y ahi delante escriban la ruta de su imagen, les pongo un trozo de código ```Bash
#!/bin/bash -e

source /usr/lib/grub/grub-mkconfig_lib

# this allows desktop-base to override our settings
f=/usr/share/desktop-base/grub_background.sh
if test -e ${f} ; then
  source ${f}
else
  WALLPAPER="/usr/share/images/grub/robuntu.tga"
  COLOR_NORMAL="black/black"
  COLOR_HIGHLIGHT="magenta/black"
fi
```

  5. Ya al final como le comente anteriormente ```Transact-SQL
alevsk@Aosnet:~$ sudo update-grub2
```

Asi lo hice yo y quedo bien, les dejo la imagen que yo use en mi grub al inicio del post por si les gusto ya nada mas uds pasenla a .tga por que el photobucket no me deja subir esa extensión y me da flojera buscar otro hosting de imágenes x'D

salu2
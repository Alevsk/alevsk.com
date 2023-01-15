---
title: Activar compositing manager en backtrack 5
author: Alevsk
type: post
date: 2011-07-16T17:49:15+00:00
url: /2011/07/activar-compositing-manager-en-backtrack-5/
categories:
  - Ethical Hacking
  - Linux
  - Tips
tags:
  - backtrack
  - Linux Debugging
  - debian
  - Storage
  - distros
  - grep
  - grub
  - hackers
  - Linux
  - slackware
  - software libre
  - Solutions

---
[![](/images/download-backtrack-5.jpg)](http://www.alevsk.com/2011/07/activar-compositing-manager-en-backtrack-5/download-backtrack-5/)  
Hola lectores, en esa ocasión les traigo no un tutorial si no mas bien un breve tip, resulta que en la empresa donde actualmente trabajo (si esa donde desarrollo **aplicaciones móviles** y **web**) ahora esta comenzando proyectos de **seguridad** de la mano de **PROSA** xD y pues la verdad tenia ya algunos meses que no hacia algo de **hacking**.

Tengo otra laptop con **ubuntu** 10.04 dije, manos a la obra pero me pedía actualizar así que opte por mejor des instalar esa distribución e instalar **backtrack** (se que trae muchas herramientas que tal vez no utilizare), una **distribución** mas acorde a los fines que tengo que realizar, como soy un usuario de **gnome** algo que me agrado es que ahora **backtrack** trae de forma nativa ese escritorio :), instale el sistema operativo, lo actualice y voila.

Aun habían algunas cosas que tenia que arreglar antes, algo que me agrado mucho es que a diferencia de **distribuciones** pasadas era un lio primero hacer que las interfaces de red funcionaran, después la tarjeta de video etc, solo me resto activar el **compositing manager**, para los que no sepan que es, son esos pequeños efectos del gestor de ventanas **Metacity** que hacen que nuestro escritorio se vea un poco mejor, sin sacrificar recursos de la computadora (sombras en las ventanas, transparencias, etc).

Una vez que tenemos todos los paquetes actualizados

```Transact-SQL
root@bt:~# apt-get upgrade

```

tan simple como:

```Transact-SQL
root@bt:~# apt-get install xcompmgr

```

Después tan solo ejecuten el comando xcompmgr y listo

```Transact-SQL
root@bt:~# xcompmgr

```

Como es muy molesto estar escribiendo el comando cada vez que inicia **Backtrack** hay varias maneras para ejecutarlo al iniciar el sistema operativo, una seria crear un script en **/etc/init.d/**miScript o añadirlo a la lista de comandos en el archivo **/etc/rc.local**, etc. Pero para mas fácil tan solo nos vamos a **System > Preferences > Startup Applications**, seleccionamos Add (indicando que queremos añadir una nueva tarea) y en comando escribimos **xcompmgr** y listo 🙂 **compositing-manager** activado.

salu2
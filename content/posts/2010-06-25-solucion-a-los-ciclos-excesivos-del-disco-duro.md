---
title: Solucion a los Ciclos excesivos del disco duro
author: Alevsk
type: post
date: 2010-06-25T16:58:34+00:00
url: /2010/06/solucion-a-los-ciclos-excesivos-del-disco-duro/
image:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/rack_hd.jpg
slider_thumbnail:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/thumb-discoduro.jpg
categories:
  - Linux
  - Tutorials
tags:
  - backtrack
  - Linux Debugging
  - debian
  - Storage
  - distros
  - Linux
  - slackware
  - Solutions
  - ubuntu

---
Bueno este problema ya tiene un buen rato y aclaro que solo afecta a ordenadores portátiles, pero por suerte ya encontré la solución y se hace desde linux xD, en windows aun no he encontrado la manera, pero debe de haber alguna ya que si no se resuelve a tiempo hace que el disco duro se joda en menos de 2 años, ahora posteo la información.

Realizado desde ubuntu / Kubuntu ambas versiones 8.10, para las demás distro me imagino que lo único que cambia es la forma de instalar los programas y algunas rutas de archivos

Primero que nada revisaremos los ciclos actuales de nuestro HD haciendo lo siguiente

<!--more-->

Se instala el smartmontools así:

```GDScript
sudo apt-get install smartmontools

```

Y luego para ver los ciclos

```Text only
sudo smartctl -a /dev/sda | egrep 'ID|Load_Cycle'
```

o

```Text only
sudo smartctl -a /dev/hda | egrep 'ID|Load_Cycle'
```

Dependiendo de si su disco es sda o hda, si no están seguro de cual es, pongan primero un comando y luego otro les debe funcionar si o si xD, la cantidad de ciclos es el valor que se muestra en Raw_Value.

En mi caso me mostró:

```Text only
ID# ATTRIBUTE_NAME     FLAG   VALUE WORST THRESH TYPE   UPDATED WHEN_FAILED RAW_VALUE
193 Load_Cycle_Count    0×0012  093   093   000 begin_of_the_skype_highlighting              0012 093 093 000      end_of_the_skype_highlighting begin_of_the_skype_highlighting              0012 093 093 000      end_of_the_skype_highlighting begin_of_the_skype_highlighting              0012 093 093 000      end_of_the_skype_highlighting    Old_age  Always       -

```

78553

Mi disco duro tiene 78553 ciclos, nadamal para 2 años y medio xD, volviendo al tema, calen ese comando cada x tiempo por ejemplo cada 3 minutos, siven que los ciclos aumentan rapidamente, sigan este manual si no, pues no xD, ami me aumentaban como 6 ciclos cada 30 seg :S.

Ahora para solucionarlo tenemos que irnos a la raiz desde la consola (shell)  
ya saben cd .. , cd .. , cd.. , nos tiene que quedar asi la ruta

alevsk@kubuntu-tek:/$

mi usuario es alevsk, en el suyo saldrá su nombre de usuario y el de su pc, ya ubicados en esa ruta debemos de editar algunos archivos, escribimos:

gedit o kate dependiendo el programa que tengamos para editar archivos de texto, por lo general ubuntu =gedit / kubuntu = kate

sudo gedit /etc/laptop-mode/laptop-mode.conf  
o  
sudo kate /etc/laptop-mode/laptop-mode.conf

Mucha atención aquí ya que un solo error y nuestro sistema quedara inestable :S, asi que ya saben mucho cuidado, tenemos que encontrar las siguientes lineas en el archivo y sustituirlas como muestro a continuación (pongale los valores que aquí muestro):

```Text only
CONTROL_HD_IDLE_TIMEOUT=1
  LM_AC_HD_IDLE_TIMEOUT_SECONDS=300
  LM_BATT_HD_IDLE_TIMEOUT_SECONDS=300
  NOLM_HD_IDLE_TIMEOUT_SECONDS=7200
  CONTROL_HD_POWERMGMT=1
  BATT_HD_POWERMGMT=239
  LM_AC_HD_POWERMGMT=239
  NOLM_AC_HD_POWERMGMT=239

```

Guardamos y salimos, ahora editamos el siguiente archivo

```Text only
sudo gedit /etc/default/acpi-support
```

o

```Text only
sudo kate /etc/default/acpi-support
```

Según sea el caso como mencione anteriormente, aquí modificamos la siguiente linea:

```verilog
ENABLE_LAPTOP_MODE=true
  y agregamos esta linea hasta el final
  SPINDOWN_TIME=60

```

Igual guardamos y salimos, ahora sigue la parte adaptada para la version 8.10, nos vamos a la siguiente ruta en la shell

```Text only
cd /etc/acpi/battery.d
```

y luego

```Text only
sudo gedit 90-hdparm.sh
```

o

```Text only
sudo kate 90-hdparm.sh
```

Dentro cambiamos

```Tera Term macro
if hdparm -i $dev 2> /dev/null | grep -q 'AdvancedPM=yes' ; then

  if [ $STATE = "BATTERY" ] ; then
  hdparm -B 128 $dev
  else
  hdparm -B 254 $dev

```

por

```Tera Term macro
if hdparm -i $dev 2> /dev/null | grep -q 'AdvancedPM=yes' ; then
  if [ $STATE = "BATTERY" ] ; then
  hdparm -B 239 $dev
  else
  hdparm -B 254 $dev

  Repetir lo mismo en /etc/acpi/ac.d

```

Guardamos y salimos, por ultimo reiniciamos, si hicieron todo bien, al iniciar revisan sus ciclos y verán como se quedan quietesitos, no aumentan rápidamente como antes.
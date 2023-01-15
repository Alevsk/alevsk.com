---
title: 'How to: Tutorial de pentest en redes inalambricas'
author: Alevsk
type: post
date: 2011-04-13T13:51:44+00:00
url: /2011/04/como-tener-internet-gratis/
categories:
  - Ethical Hacking
  - Technology
  - Tips
  - Tutorials
tags:
  - backtrack
  - Linux Debugging
  - debian
  - distros
  - hackers
  - Linux
  - Programming
  - Social Media
  - software libre
  - Tutorials
  - ubuntu

---
[![](/images/BackTrack4_Slide.png)](http://www.alevsk.com/2011/04/como-tener-internet-gratis/backtrack4_slide/)  
_Como les comentaba en un post anterior que hablaba sobre [VirtulBox][1] estoy tratando de rescatar algunos documentos que realice hace algunos años cuando era activo en los foros y aprendía de ellos, a continuación publico un tutorial que trata acerca del tema de las redes inalámbricas. 

**Me doy cuenta que al pasar todos estos años he evolucionado, por decirlo de alguna manera, pueden ver que mi redacción ya no es la misma y yo mismo tuve que modificar algunas partes del tutorial por que considere que no eran correctas :), también note que los conocimientos que tenia en aquella epoca eran nulos comparados con todo lo que estoy aprendiendo ahora.**

Este tutorial, como comentaba mas arriba, ya es viejo así que no les aseguro que les pueda servir, solamente decidí publicarlo para que no se pierda en el olvido.

Manual para obtener Internet Inalámbrico gratuito crackeando wep en módems/routers 2wire (Telmex) by Alevsk  
**Conceptos basicos:**

**MODEM:** Aparato electrónico que sirve para conectarnos a Internet

**Router:** Aparato electrónico que sirve para identificar varias computadoras en una red y así proveerles Internet 

**Tarjeta inalámbrica:** Es un dispositivo indispensable para poder usar el Internet inalámbrico el 99.9% de las laptops traen una tarjeta inalámbrica integrada

**WEP:** Algoritmo de encriptación para la contraseña de los módems 2wire, si tienes acceso físico al MODEM/Router la contraseña por defecto se encuentra entre [ ], sino, te va tocar sacarla.

**WPA:** Es otro tipo de encriptación mas segura que la WEP.

**Dirección MAC:** Media Acces Control o Control de Acceso al Medio, es una identificación como la IP, pero en este cada dispositivo tiene su propia dirección MAC determinada y configurada por el IEEE y el fabricante ( ejemp de dir MAC: **00:11:22:33:44:55** )

**IFACE:** Es el nombre de la interfaz de nuestra tarjeta wireless (eth0, eth1, etc.)

**ESSID:** Nombre de la red inalámbrica que queremos crackear.

**Distro Linux**: Se llama distro a las ediciones o publicadas de Linux, existen muchas pero las mas conocidas son ubuntu, backtrack, debian, suse, redhat, slax.

**Channel:** Es el canal por el que transmite el MODEM/Router, es como una estación de radio por asi decirlo tenemos que estar escuchando en ese canal para captar algo 🙂

**DHCP:** Protocolo de conexión de Host dinámico, este lo usan los modems/routers 2wire para que los usuario no tengamos que configurarle en la asignación de IP's a cada computadora conectada a la Red.

**RED:** Conjunto de computadoras que comparte recursos.

**ISO:** Formato de imagen de disco estos archivos se deben de quemar en un CD.

**Nero:** Programa usado para quemar archivos en un CD.

Bueno creo que esos son los más importantes, así que ya saben apréndanselos

Comenzamos.

Primero que nada tenemos que saber que tipo de tarjeta inalámbrica esta usando nuestra computadora ( esto no lo explicare, pueden descargarse un software como **Everest** o googleando al respecto ), en mi caso tengo:

**PC:**  
_Dell Inspiron 1300_

**Tarjeta:**  
_Tarjeta mini-PCI de red inalámbrica WLAN 1370 de Dell_

**Chipset**  
_BCM4318_

Es una **broacom**, muy utilizadas para hacer pruebas de penetracion en redes aunque no tanto como una alfa500 por ejemplo :), los modelos de adaptadores de red soportados son **broadcom**, **realtek**, **atheros** y algunos otros, si no tienen esas tienen que comprar o intentar usar algún chipset de esos modelos, aquí dejo una lista http://hwagm.elhacker.net/htm/tarjetas.htm

Ya que sabemos que hardware tenemos, ahora nos debemos preparar con nuestras herramientas de auditoria wireless, para este manual yo usare la distro **wifislax**, pueden descargarla de acá:

**Wifislax**  
http://download.wifislax.com:8080/wifislax-3.1.iso  
http://download.wifislax.com:8080/wifislax-3.1.iso.md5  
http://download.wifislax.com:8080/wifislax-3.0.iso  
http://download.wifislax.com:8080/wifislax-3.0.iso.md5  
http://download.wifislax.com:8080/wifislax-1.2-beta.iso  
http://download.wifislax.com:8080/wifislax-1.2-beta.iso.md5

Descargamos cualquiera y están en formato .ISO así que los quemamos en un CD con nero u otros programas. Después tenemos que iniciar con el CD de booteo (el cd wifislax que descargamos previamente), si no saben como bootear desde un CD tranquilos 🙂 http://cafemadrid.blogspot.com/2007/05/como-bootear-desde-el-cd.html (cada bios varia dependiendo el fabricante, pero casi todas tienen las mismas estructuras)

Cuando ya logremos entrar a wifislax les pide un user y un pass  
**USER: root  
PASS: toor**

Y estaremos ante una de las mejores herramientas para auditorías inalámbricas, bueno aun no cantemos suficiente victoria ya que esta es la mitad del camino apenas.

Antes que nada tenemos que tener en mente quien será nuestra victima (el vecino, un ciber, etc.) yo lo haré con mi propio MODEM/Router 2wire.

Bueno seguimos, antes que nada abrimos la consola (shell) esta ubicada cerca del botón de inicio es un pequeño recuadro negro, yo recomiendo abrir varias solapas para que no tengamos muchas consolas, escribimos **ifconfig** en una y **iwconfig** en otra y nos aparecerán varios datos

**Ifconfig** Nos muestra nuestra **direccion MAC**

———  
_Agregado: También es posible utilizar una herramienta como macchanger para ver la direccion Mac de nuestras interfaces así como falsearlas, Ej.
```Text only
macchanger -s eth0
```

Ese comando mostraría la dirección **MAC** de la interfaz **eth0**, de igual manera pueden ver la dirección de una interfaz tipo wlan[X].  
———

**Iwconfig** Nos muestra nuestra **iface** (interfaz de red) en mi caso es **eth0** pero puede variar dependiendo de cada computadora

Debe de aparecer algo mas o menos así en **iwconfig** (**eth0** es mi interfaz inalambrica)

[![](/images/wire1.png)](http://www.alevsk.com/2011/04/como-tener-internet-gratis/wire1/)

Después para hacer las cosas un poco más fácil usamos el asistente **wireless**

[![](/images/wire2.png)](http://www.alevsk.com/2011/04/como-tener-internet-gratis/wire2/)

Y escaneamos la zona en busca de nuestras victimas, nos aparece el nombre de la red **(ESSID)** y el canal por el que transmite **(CHANNEL)**.

[![](/images/wire3.png)](http://www.alevsk.com/2011/04/como-tener-internet-gratis/wire3/)

A mí me aparecen 2, la primera es la mía y la segunda la de mi vecino, vemos que **INFINITUM5074** esta transmitiendo por el canal 2, después si tienen una tarjeta **broadcom** tenemos que cargar el driver de inyección, sino hay buscan el suyo creo que hay otros drivers, pero igual si no esta el suyo pueden continuar 

[![](/images/wire4.png)](http://www.alevsk.com/2011/04/como-tener-internet-gratis/wire4/)

Regresamos a la consola, ahora tenemos que poner nuestra interfaz en modo monitor, es decir solo escuchando, pueden escribir en la solapa donde escribieron **iwconfig** o en otra nueva.

Escribimos 

```Text only
iwconfig  mode monitor
```

Es la interfaz que nos mostro el **iwconfig**, ami me mostro eth0.  
Ejemplo: 

```Text only
iwconfig eth0 mode monitor
```

Con eso ponemos nuestra tarjeta escuchando.

Después lanzamos **airodump-ng**, abran lo en otra solapa, ahora ya debemos de tener 3, la de  
**Ifconfig**, **iwconfig** y ahora la del **airodump-ng**, escribimos:

```Text only
airodump-ng -w NAME -c XX eth0
```

Donde **NAME** es el nombre del archivo en el que guardaremos lo que capturemos y **XX** es el canal por donde transmite el router del cual sacaremos la contraseña, en mi caso decía que era la 2 y la interfaz es la que ya les comente anteriormente

Entonces quedaría así: 

```Text only
airodump-ng -w captura -c 2 eth0
```

Mi archivo se llamara captura y recogerá todo lo que capte por el canal 2

[![](/images/wire5.png)](http://www.alevsk.com/2011/04/como-tener-internet-gratis/wire5/)

Ahora que ya estamos capturando.. Vamos a inyectar algo de tráfico a la red, realizamos un ataque de asociación falsa (A1) y un ataque A3 que es la (re)inyección, para eso abrimos una nueva solapa y tecleamos:

```Text only
aireplay-ng -1 0 -e NAME -a XX -h MAC_Interfaz eth0
```

Donde **NAME** es nuestra red a penetrar y **XX** es la mac del router o access point (nos la da en el airodump-ng) y **MAC_interfaz** es la mac de tu tarjeta, con esto realizamos asociación.

[![](/images/wire6.png)](http://www.alevsk.com/2011/04/como-tener-internet-gratis/wire6/)

Después escribimos

```Text only
aireplay-ng -3 -b XX -h MAC_interfaz eth0
```

**XX** tambien es la mac del router a testear y MAC_interfaz es la mac de tu tarjeta. Y comenzaran a subir los Datas que son vitales para poder crakear la contraseña xD, cuando tengan mas o menos como 50,000 viene el crackeo.

[![](/images/wire7.png)](http://www.alevsk.com/2011/04/como-tener-internet-gratis/wire7/)

Abrimos una nueva solapa y comenzamos el crackeo  
Pueden lanzar el **aircrack-ng** o el **aircrack-ptw**…

Básicamente la diferencia entre uno y otro radica en que en el ptw se ha implementado un nuevo algoritmo mejorado, el cual necesita menos paquetes para encontrar la clave.

La relación entre uno y otro puede ser ésta, por tener una referencia…  
_  
aicrack-ng wep 128bit 800.000 paquetes 

aircrack-ptw wep 128bit 50.000 paquetes

Como ven hay mucha diferencia xD

En la nueva solapa escribimos: 

```Text only
aircrack-pwt -01.cap
```

Donde **<archivo>** es el nombre que le pusieron cuando escribieron en el **airodump-ng** y le agregan -01.cap , en mi caso es así

```Text only
Aircrack-ptw captura-01.cap
```

Y comenzara, si lo hicieron bien en 30 min tienen la contraseña crackeada y si son muy buenos pueden incluso ha romperla en 3 min. como yo lo logre jejeje, ya solo resta conectare desde **windows** o **Linux** y ha usar Internet xD

Especial thanks to:

**M/Q  
Dr. House  
Robochop  
Azazel**

 [1]: http://www.alevsk.com/2011/04/tutorial-de-virtualbox/</archivo>
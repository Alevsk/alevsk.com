---
title: Tutorial de VirtualBox
author: Alevsk
type: post
date: 2011-04-07T14:47:52+00:00
url: /2011/04/tutorial-de-virtualbox/
categories:
  - Geek
  - Linux
  - Technology
  - Tips
  - Tutorials

---
_Hoy mientras buscaba algunas cosas en mis discos duros me encontre con un viejo tutorial que hice sobre el software **virtualbox**. Este tutorial lo escribi hace un par de años ya (cuando era muy activo en los foros del underground) … que buenos tiempos aquellos 🙂 y decidi ponerlo en el blog para que mas gente lo pueda leer y si les sirve pues que bien._

_Este tutorial es de cuando usaba Windows uuuu x'D


_Cualquier persona es libre de copiar, modificar o publicar este tutorial en algun otro sitio, solo no olviden de escribir tambien el link de mi web [Blog personal de Alevsk : Informática, Ciencia, tecnología y Hacking etico][1] y todo bien._

# Como utilizar VirtualBox

Hola eh realizado este pequeño tutorial donde les dire como utilizar el programa virtualbox, primero que nada…

Según la Wikipedia:  
**VirtualBox** es un software de virtualización para arquitecturas x86 que fue desarrollado originalmente por la empresa alemana innotek GmbH, pero que pasó a ser propiedad de la empresa **Sun Microsystems** en febrero de 2008 cuando ésta compró a innotek. Por medio de esta aplicación es posible instalar sistemas operativos adicionales, conocidos como “sistemas invitados", dentro de otro **sistema operativo** “anfitrión", cada uno con su propio ambiente virtual. Por ejemplo, se podrían instalar diferentes distribuciones de **Linux** en un **VirtualBox** instalado en Windows XP o viceversa.

Comenzemos  
Primero que nada nos descargamos el VirtualBox  
http://virtualbox.softonic.com/descargar#pathbar  
Despues lo instalamos, no creo que necesiten ayuda en este paso, es puro siguiente siguiente ya saben 😉

La primera vez que lo ejecutemos nos pedirá nuestro nombre y correo, no importa si son falsos los datos, póngale en no usar esta información para contactarme.

Y ya estamos ante el genial virtualbox, veremos una interfaz como esta.

[![](/images/vbox1.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Muy bien ahora para mi ejemplo, yo voy a correr debian en mi xp, si quieren pueden descargárselo de aquí… http://live.debian.net/cdimage/etch-builds/current/i386/iso-cd/debian-live-etch-i386-kde-desktop.iso

Bueno una vez que ya hayan descargado el debian, tendrán algo así, una imagen ISO.

[![](/images/vbox2.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

No es necesario quemarlo en un CD ya que VirtualBox nos permite emular el sistema directamente desde ese archivo  
Y comenzamos con la parte interesante, damos clic en nuevo y nos aparecerá el asistente

[![](/images/vbox3.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Damos clic en siguiente y nos pedira que pongamos un nombre para nuestra maquina virtual, yo le puse debian pero ustedes pueden ponerle pepe o pancho o como quieran xD, y seleccionamos Linux 2.6, esto varia dependiendo de que sistema tengan pensado correr, por ejemplo si van a usar un Windows XP ps ahí le ponen xp o Solaris o freeBSD o dependiendo de cual quieran.

[![](/images/vbox4.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Después nos pedirá que asignemos la memoria ram, pongale la mitad de la que tienen realmente, para que no haya problemas, yo tengo 2 gb asi que le dejare 1024 y siguiente.

[![](/images/vbox5.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Aquí viene la parte interesante, pero verán que no es nada difícil, ahora nos pide que creemos un disco duro virtual o usemos uno existente pero como es la primera vez le damos en NUEVO.

[![](/images/vbox6.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Nos aparecerá el Asistente para la creación de nuevo disco duro virtual, que el nombrecito no los apantalle, es muy fácil de hacer esto xD, damos en siguiente

[![](/images/vbox7.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Ahora le ponemos tamaño fijo, al fin y alcabo solo vamos a probar el sistema operativo 😉 y damos siguiente.

[![](/images/vbox8.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Ahora nos pedirá que le asignemos el tamaño al disco, yo como tengo poco HD le dejare solo 2 GB, con eso basta 😉 y también ponemos la ubicación donde queremos que se guarde el archivo, si no le ponemos se guardara en la unidad c:, clic en siguiente.

[![](/images/vbox9.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Por ultimo nos mostrara un pequeño resumen de cómo lo hemos configurado le damos finalizar y se comenzara a crear el disco duro virtual.

[![](/images/vbox10.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Después volveremos a la pantalla donde nos daba a elegir un disco duro existente o crearlo, pero ahora ya esta el que hemos configurado nosotros, le damos en siguiente.

[![](/images/vbox11.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Nos mostrara otro resumen (ya es el ultimo xD) y damos clic en finalizar.

[![](/images/vbox12.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Y si lo hicieron bien tendrán algo como esto:

[![](/images/vbox13.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Muy bien ahora solo falta una configuración mas, le damos en “configuración o settings" y nos saldrá esto:

[![](/images/vbox14.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Primero que nada, nos vamos a la pestaña que dice Avanzado, aun lado de Básico y nos aseguramos que en el boot orden este al principio CD/DVD ROM (acomodar con las flechitas).

[![](/images/vbox15.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Después nos vamos al menú de Discos Duros y marcamos la casilla que dice Habilitar el control SATA.

[![](/images/vbox16.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Ahora nos vamos a la opción que dice CD/DVD ROM marcamos la casilla de Montar la unidad de CD/DVD ROM y marcamos la opción que dice archivo de imagen ISO, recuerdan el debian que descargamos, pues ahora lo ubicamos, la otra opción de arriba es para si tenemos un sistema operativo en un disco solo metemos el CD o DVD y marcamos esa opción y VirtualBox trabajara con el.

[![](/images/vbox17.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Las demás opciones las podemos habilitar si queremos, por ejemplo sonido, USB etc., etc., por último damos clic en aceptar y volveremos a acá.

[![](/images/vbox18.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Bueno ahora ya debería funcionar, digo debería por que a veces se nos pasa configurar algo y no sirve =/, pero bueno damos en iniciar… carga todo lo que tiene que cargar y si lo hicimos bien el resultado será este 🙂

[![](/images/vbox19.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Un flamante debian listo para usarse ^^, para usar el sistema operativo, la tecla por defecto es ctrl. Derecha, es decir la que esta aun lado de las flechas de dirección en el teclado, con esa tecla podemos cambiar de usar xp, al sistema que estamos emulando, aquí les pongo algunas imágenes:

[![](/images/vbox20.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Cuando ya queramos apagar nuestra maquina virtual simplemnte vas al menu de arriba de la ventana que dice maquina y le das en apagar, te saldra un menu de opcion y pones apagar la maquina 😉

[![](/images/vbox21.png)](http://www.alevsk.com/2011/04/tutorial-de-virtualbox/vbox1/)

Bueno espero que este pequeño tutoríal sea de su agrado y aceptación ^^, que utilidad podemos darle a esto, pues infinitas xD, por ejemplo podemos instalar software malicioso (malware) para realizar investigaciones en nuestra maquina virtual y asi mantener nuestro equipo físico a salvo 🙂

Salu2

**Ahi lo tiene, creo que tengo mas tutoriales y guias que he realizado con anterioridad, me voy a dar un tiempo libre para buscarlos y publicarlos en el blog tambien.**

 [1]: http://www.alevsk.com
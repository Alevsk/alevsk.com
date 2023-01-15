---
title: Proyecto con Wiimote en la Universidad
author: Alevsk
type: post
date: 2010-08-12T19:27:50+00:00
url: /2010/08/proyecto-wii-nintendo-wiimot/
categories:
  - IT News
  - Personal
  - Programming
  - Technology
tags:
  - Personal
  - Programming
  - Tutorials
  - web

---
[![](/images/2010/08/wiimote.jpg)](http://www.alevsk.com/2010/08/proyecto-wii-nintendo-wiimot/wiimote/)

Bueno hace ya varios dias, probablemente una semana o mas que no he escrito nada en el blog por cuestiones de tiempo, y es que cuando uno entra a clases prácticamente vive en el campus hehe, bueno tengo 1 materia que probablemente es la mas interesante, es sobre desarrollo web y cualquier, donde se planea enseñar a los alumnos sobre las tecnologías webs como ajax, javascript, php, mysql, asp, y gestores de contenido, etc, etc nada que no sepa alguien que se considere un aficionado a la red jeje, se que me servira para reforzar mucho mas mis conocimientos sobre programación web 🙂

Aproposito y regresando a la temática de este post, el profesor de esa clase nos ha propuesto desarrollar un proyecto como trabajo final, algo utilizando el control (Wiimote) del Nintendo Wii, pues me he puesto a investigar y se que el lenguaje a utilizar ser C++ por las librerías que ya existen para el control.

Bueno encontre un post muy bueno sobre dicho tema y lo quiero compartir, dejando claro esta la fuente al final.

Lo interesante de la Wiimotelib es que permite que cada uno desarrolle la aplicación que desee, con los mandos de la Wii.

Por ejemplo, los fabricantes de juegos podrían incluir soporte para Wii en sus juegos de PC. Aunque esto es improbable mientras no acuerden algo con Nintendo.  
No tengo una idea clara sobre cómo le cae a Nintendo toda esta movida, ya que por un lado es publicidad gratis, y podría generar un nuevo negocio para la compañía ya que la patente del Wiimote es propiedad de estos nipones. Además también se podría avanzar bastante en el uso de su sistema, y ¡gratis!  
Porque Nintendo no paga a estos investigadores.

Por otro lado sabemos que a los fabricantes de consolas les gusta que se vendan juegos de consolas, y con estos proyectos pareciera que el rumbo es diferente. Sin embargo sabemos que Nintendo gana dinero con cada consola que vende, algo muy diferente a lo que pasa en Sony o Microsoft.

Volviendo a la Wiimotelib, la librería es bastante fácil de usar para alguien que tiene conocimientos en C#. Si no los tienes empieza a aprender ahora, no seas vago. Programar no es tan difícil como muchos dicen, y produce una gran satisfacción ver tus programas funcionando.

Yo una vez hice un programa en QuickBasic, y una placa que se conectaba al puerto LPT1 (el de la impresora ¡no! Ese es el USB digo el de las impresoras de antes)

Al presionar una tecla se encendía una lámpara, al presionar otra se apagaba. ¡Magia!

Luego le puse un Timer que la encendía y apagaba cada cierto tiempo. En definitiva, flipe como 4 años con eso.

Así que recomiendo empezar a programar, para el que no lo hace ya, y sobre todo recomiendo estas librerías, ya que se pueden hacer muchas cosas muy divertidas. Programar es mucho más que trabajar con bases de datos.

Con Wiimotelib se pueden hacer cosas como esta



[**Wii Drum High**][1] es un simulador de Bateria que deja boquiabierto a cualquier usuario de Guitar Hero ¡Incluso utiliza la **Wii Balance Board**!

El programa es gratuito, Su código fuente es abierto.

Para utilizarlo hace falta

  * Los mandos de la Wii, claro
  * Que tu ordenador tenga receptor Bluetooth
  * Windows Vista, o XP con [Framework 3.5][2] instalado

Para conectar los mandos al ordenador utilizamos [BlueSoleil][3], que detecta los mandos como “_Human Interface Device_"

Si tienes los mandos y una portátil medianamente nueva probablemente tengas todo lo necesario.  Ya que las portátiles suelen traer Bluetooth.

¡Cuéntanos tu experiencia si lo pruebas!

<div id="dnn_ctr370_VFBArticles_rptBlocks_ctl02_divLinks">
  Enlaces
<div>
    Descargar  [Wii Drum High](http://hezhao.net/project/wii-drum-high.html)
</div>
<div>
    Web Oficial  [Wiimotelib](http://blogs.msdn.com/coding4fun/archive/2007/03/14/1879033.aspx)
</div>
<div>
    Más proyectos con  [Wiimotelib](http://www.brianpeek.com/blog/pages/net-based-wiimote-applications.aspx)
</div>
<div>
    Descargar  [BlueSoleil](http://www.bluesoleil.com/download/index.asp?topic=bluesoleil6x)
</div>
<div>
    Descargar  [Framework 3.5](http://www.microsoft.com/downloads/details.aspx?displaylang=es&FamilyID=333325fd-ae52-4e35-b531-508d977d32a6)
</div>
</div>
<div>
  Fuente: [http://www.neoteo.com/wii-drum-high-usando-el-wiimote-con-windows-14241.neo](http://www.neoteo.com/wii-drum-high-usando-el-wiimote-con-windows-14241.neo)
</div>

 [1]: http://hezhao.net/project/wii-drum-high.html
 [2]: http://www.microsoft.com/downloads/details.aspx?displaylang=es&FamilyID=333325fd-ae52-4e35-b531-508d977d32a6
 [3]: http://www.bluesoleil.com/download/index.asp?topic=bluesoleil6x
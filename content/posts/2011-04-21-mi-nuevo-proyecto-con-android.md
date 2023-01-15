---
title: Mi nuevo proyecto con Android
author: Alevsk
type: post
date: 2011-04-21T17:19:22+00:00
url: /2011/04/mi-nuevo-proyecto-con-android/
categories:
  - C y C++
  - Java
  - Personal
  - Programming
  - Technology
tags:
  - android

---
[![](/images/android1.jpg)](http://www.alevsk.com/2011/04/mi-nuevo-proyecto-con-android/android1/)

Se podrían decir que ayer a las 8 de la noche comenzaron mis vacaciones jeje, fue la hora en que me desocupe del trabajo y de varias cosas que tenia pendiente, sin embargo aun me queda mucho trabajo de la universidad por hacer x'D (bonitas vacaciones -.-“), pero bueno no nos lamentemos xD.

Les quiero mostrar un proyecto (uno de tantos jaja) en el que estoy trabajando y ya casi termino, se trata de una calculadora científica desarrollada para la plataforma de **android**. para los que piensen que realizar una calculadora es algo sencillo … puede ser, pero hay que tener varias cosas en cuenta, por ejemplo ¿como le haces para que tu calculadora resuelva una expresión algebraica tipo **((a+b)*((c/d)-e)^f)/g** xD? en algún post anterior les hable sobre un código que realice en [C++][1] donde tu le dabas una expresión de ese tipo y te regresaba su equivalente en orden postfijo o [notación polaca inversa][2] :D, si bien en [C++][1] necesite del uso de **pilas** y **listas** creándolas desde cero usando apuntadores x'D, migrar el código a [Java][3] fue un juego de niños x'D, claro que en Java ya existen todas esas estructuras de datos, en **C++** también pero creo el crear las listas desde 0 me sirvió mucho para dominar el uso de los apuntadores :).

A continuación les dejo una captura de como luce el software:

[![](/images/calcu_android.png)](http://www.alevsk.com/2011/04/mi-nuevo-proyecto-con-android/calcu_android/)

Cuando el proyecto este terminado (**2 semanas mas o menos**) planeamos subir nuestra aplicacion al **android market** (un lugar donde hay muchas [aplicaciones android][4], algo así como la **app store**) y ponerle un módico precio de **1 usd** 🙂 ya que el objetivo no es lucrar con este proyecto sino que la gente conozca y use esta **plataforma** para teléfonos mobiles.

No he utilizado nada del otro mundo para este proyecto, solamente cosas básicas que ya trae incluida la **api** de **android** y algunos componentes custom que tuve que realizar :), ahora lo siguiente que tengo en mente es que mi nuevo proyecto haga uso de una tecnología que cada vez es mas común en la actualidad, [gps para android][5], xD.

Aun que me gusta mucho [Java][3] yo sigo siendo un C/C++ fan x'D, lo he comprobado por mi mismo, sabiendo [C y C++][1] los demás lenguajes de programación son muy fáciles :p.

PD lo mas probable es que en mi siguiente post les haga un tutorial acerca de como instalar la **api** de **android** en eclipse y el **android manager** para que tengan su emulador y comiencen a desarrollar xD

salu2

 [1]: http://www.alevsk.com/category/c-y-c/
 [2]: http://www.alevsk.com/2011/03/c-conversion-a-notacion-polaca-inversa/
 [3]: http://www.alevsk.com/category/java/
 [4]: http://www.nosolounix.com/2011/03/mejores-aplicaciones-android.html
 [5]: http://www.nosolounix.com/2011/04/gps-para-android.html
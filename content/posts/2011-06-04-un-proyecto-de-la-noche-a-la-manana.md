---
title: Un proyecto de la noche a la mañana
author: Alevsk
type: post
date: 2011-06-04T16:58:34+00:00
url: /2011/06/un-proyecto-de-la-noche-a-la-manana/
categories:
  - Geek
  - Personal
  - Programming
  - SEO
  - Technology
  - Tips
  - Tutorials
tags:
  - Linux
  - Personal
  - Programming
  - Social Media
  - slackware
  - software libre

---
Hola lectores en esta ocasión les quiero hablar un poco acerca de los proyectos que he estado realizando en este ultimo mes :), como muchos de ustedes saldrán ya estoy en vacaciones de verano, lo que significa que tengo aun mas trabajo del que venia haciendo durante la temporada de clases.

Hace algunas semanas les había comentado sobre un proyecto de programación, una calculadora para la plataforma de android, pues hace algunos días ya termine la versión 1.0 y ya tengo la apariencia del sitio, tan solo falta subirla al **android market** (lo mas importante xD) la razón por la que no he publicado la app aun es por que google no acepta pagos de paypal asi que forzosamente tengo que hacer el pago con tarjeta de crédito :p, no obstante puedes visitar la web del proyecto para obtener un poco mas de informacion. [calculador para android][1].

[![](http://android.alevsk.com/img/bg-entrenamiento.png)][2]

Segundo, he estado trabajando en un proyecto con algunas inmobiliarias de mi ciudad, el **proyecto** consiste en desarrollar una **aplicación web** (tipo red social) que contenga una base de datos completa de propiedades y servicios cercanos (farmacias, escuelas, oxxos, etc) para que cuando usuarios quisieran comprar o rentar alguna propiedad obtuviera la mayor cantidad de información posible, para este **proyecto** utilizamos **Twig**, **PHP** y **google maps**, ha y claro es un sistema distribuido con **web service** y todo por que también se desarrollo una app (no se por que no me dejaron llevar la materia de **sistemas distribuidos** el siguiente semestre x'D).

Pueden ver una version Beta del sistema en el siguiente [:: Zona U :: Casas y Terrenos][3]

[![](/images/zonau.jpg)][4]

También estoy desarrollando una **app** llamada **BetterPhotos Easy**, pero de eso les doy mas información en el post que sigue :p.

[![](/images/iphonedeveloper.jpg)][5]

Pero ahora de lo que verdaderamente les quería hablar, un proyecto que comencé a realizar de la noche a la mañana, ya esta disponible la versión Beta 1.0 también, ha este nuevo proyecto (que realizo generalmente los fines de semana por cuestiones de tiempo) lo he nombrado [EasyLink Share][6] y es un protector de enlaces, decidí realizarlo ya que por una parte veía los servicios existentes de este tipo y pensaba, esto no es nada complicado, puedo hacerlo en unas cuantas horas, y además por que en [forobeta][7] hay varios usuarios que querían un servicio de acortador y protector de enlaces, debido a eso me puse a programar un sábado a las 2 am x'D y cuando amaneció ya estaba terminada la primera versión del **proyecto**, sigo desarrollando módulos y componentes para el proyecto siguiendo las recomendaciones de que es lo que les gustaría que tuviera el servicio a algunos amigos uploaders del foro que tengo (para este tipo de usuarios va dirigido el sistema), la aplicación esta desarrollada como la mayoría de las aplicaciones actuales deberían estarlo xD, su front end, su back end, un sistema de logs de la aplicación, sistema de usuarios, grupos y permisos, recuperación de contraseña, etc. El sistema esta desarrollado utilizando el framework [cakephp][8] + framework (ósea como un framework de un framework :)) con el que es muy fácil desarrollar aplicaciones rápidamente!

[![](/images/easylinks.jpg)][9]

**Algunas características que tiene esta primera version son:**

  * Interfaz amigable con el usuario
  * protección de enlaces con contraseña
  * algunos usuarios me pidieron un **captcha** a la hora del re direccionamiento, asi que esta implementado
  * sistema de usuario, grupos y permisos
  * sistema de blog, para hacer publicaciones hacia los usuarios
  * paginación en la lista de despliegue de links
  * la mayoría de los formularios implementan **ajax**
  * un sistema de backups de la base de datos
  * Administración de links y búsqueda de los mismos (muy útil cuando tienes miles de links!)
  * Muy cuidado respecto a la seguridad, se ha testeado en busca de las vulnerabilidades mas comunes como **sql injection**, blind sql injection, xsrf, local y remote file inclusion, http injection, path disclosure, source code disclosure, etc
  * Internacionalización de la aplicación
  * **Url's amigables** en el sistema

Algunas de las cosas nuevas que le implementare:

  * Crear un **bookmarklet** para proteger enlaces rápidamente
  * Dar de alta múltiples enlaces a la vez
  * Generador de reportes en formato **Excel**
  * **Estadísticas** de clicks en impresiones

La funcionalidad principal de un **protector de enlaces** es eliminar el referer original, así no se sabe el sitio donde originalmente se publican los enlaces, muchos servicios similares realizan el re direccionamiento por medio de **javascript**, aunque los buscadores no son capaces de leer “**javascript**" el link al que serás re direccionado ahí esta, yo realizo la redirección hasta el ultimo momento por medio de php :).

Les recomiendo que prueben la aplicación, me digan que les gusta, que no les gusta, que le agregarían o le quitarían y por ultimo soy un ser humano y no soy perfecto por lo que si encuentran algún bug en la **aplicación** les estaría profundamente agradecido de que me informaran vía la sección de [contacto][10]

salu2

 [1]: http://android.alevsk.com/
 [2]: http://android.alevsk.com/img/bg-entrenamiento.png
 [3]: http://preview.zonau.com.mx/
 [4]: /images/zonau.jpg
 [5]: /images/iphonedeveloper.jpg
 [6]: http://protector.alevsk.com/
 [7]: http://forobeta.com
 [8]: http://www.alevsk.com/?s=cakephp&x=0&y=0
 [9]: /images/easylinks.jpg
 [10]: http://www.alevsk.com/contacto
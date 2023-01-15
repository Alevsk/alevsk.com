---
title: '#Latch Plugins Contest 2015 + tutorial de instalación en #WordPress'
author: Alevsk
type: post
date: 2015-10-13T21:39:58+00:00
url: /2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/
categories:
  - Geek
  - Ethical Hacking
  - IT News
  - Personal
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - elevenpaths
  - hacking
  - latch
  - plataformas
  - Security
  - wordpress

---
Regresa el [concurso de desarrollo de plugins de seguridad con Latch](https://community.elevenpaths.com/elevenpaths/topics/latch-plugins-contest-2015) de [elevenpaths](http://elevenpaths.com), en esta segunda edición los organizadores no han escatimado en gastos y están ofreciendo los siguientes premios:

  * Primer lugar: USD 5,000
  * Segundo lugar: USD 2,000
  * Tercer lugar: USD 1,000

El concurso esta abierto del **8 de octubre de 2015 al 7 de enero de 2016**, así que a programar 🙂

Si no saben que es **Latch** ahora les digo, Latch es un servicio que nos permite implementar mecanismos de [autenticación de dos factores](https://en.wikipedia.org/wiki/Two-factor_authentication) en nuestras aplicaciones de manera muy sencilla, es decir una capa de seguridad extra.

  


<center>
<em>(Un vídeo donde creo que queda mas claro que es Latch)</em>
</center>

Por ejemplo en los portales bancarios es común que ademas de un usuario y contraseña se nos solicita un **PIN** o **TOKEN** que es mandado por mensaje a nuestro teléfono, eso significa que si un atacante logra obtener nuestros datos de acceso (usuario y contraseña) todavía necesita obtener acceso físico a nuestro teléfono para utilizar el servicio. Pues con Latch podemos implementar una arquitectura de seguridad de este tipo para nuestros sitios web.

[![zoho-two-factor-authentication1](/images/zoho-two-factor-authentication1.png)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/zoho-two-factor-authentication1/)

Lo más interesante de [Latch](https://latch.elevenpaths.com/) es que cuenta con una **API Rest** que nos permite realizar nuestras propias implementaciones, así como también varias [SDK](https://github.com/ElevenPaths) para muchisimos lenguajes de programación, les dejo las bases del concurso en el siguiente [link](https://community.elevenpaths.com/elevenpaths/topics/latch-plugins-contest-2015).

## Tutorial sobre cómo proteger nuestros sitios WordPress

Si se animan a probar **Latch**, y tienen un **blog de wordpress** su instalación es bastante sencilla, lo primero que tenemos que hacer ir al [sitio web oficial](https://latch.elevenpaths.com/) del servicio y crear una cuenta, después en el área de desarrolladores iniciamos sesión en la plataforma.

[![iniciar_sesion](/images/iniciar_sesion.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/iniciar_sesion/)

Latch cuenta con un panel de administracion bastante intuitivo para administrar nuestras aplicaciones, damos clic en el botón verde que dice “Añadir nueva aplicación"

[![nueva_app](/images/nueva_app.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/nueva_app/)

Nos pedirá que definamos un nombre, recomiendo que sea algo descriptivo, como por ejemplo “Mi blog personal", damos clic en añadir aplicación.

[![nombre_nueva_app](/images/nombre_nueva_app.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/nombre_nueva_app/)

El siguiente paso es importante, después de crear la aplicación el sistema automáticamente nos generó dos valores: 

  * ID de aplicación
  * Secreto

Estos datos guárdenlos y téngalos a la mano, pues los necesitaremos más adelante.

[![api_secret_key](/images/api_secret_key.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/api_secret_key/)

Ahora vamos a wordpress, en la sección de plugins buscamos Latch y lo instalamos, si por alguna razón no pueden instalar plugins desde el administrador entonces tienen que descargar el archivo zip, descomprimirlo y subirlo directamente a su servidor por FTP, **SFTP**, etc a la carpeta plugins de wordpress (**sitio/wp-content/plugins**)

[![wordpress_latch](/images/wordpress_latch.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/wordpress_latch/)

Una vez instalado el [plugin de latch](https://wordpress.org/plugins/latch/) en **wordpress** tenemos que configurarlo, en el menú del lado izquierdo vamos a **Ajustes > ajustes Latch**, nos aparecerá un formulario como el siguiente.

[![latch_configuration](/images/latch_configuration1.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/latch_configuration-2/)

Aquí vamos a poner el ID de aplicación y el Secreto que generamos y obtuvimos anteriormente, por ultimo guardamos los cambios. Ahora vamos a parear (sincronizar) el servicio (wordpress) de una cuenta de usuario en específico, puede ser cualquiera, por ejemplo un redactor, un administrador, un suscriptor, un colaborador, etc.  
En el menú de la izquierda vamos a **Usuarios > Tu Perfil** y buscamos el campo que dice “**Token de Latch**"

[![token_latch](/images/token_latch.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/token_latch/)

Ya casi tenemos todo listo, ahora tenemos que abrir la aplicación de Latch en nuestro teléfono Android o iOS, nos encontraremos con una pantalla como la siguiente y damos Tap en “Añadir nuevo servicio"

[![AuYBLlyLZn41M-j3KNsVXUIUOpvtrhv0Sek_hZyo5KMS](/images/AuYBLlyLZn41M-j3KNsVXUIUOpvtrhv0Sek_hZyo5KMS-169x300.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/auybllylzn41m-j3knsvxuiuopvtrhv0sek_hzyo5kms/)

Ahora damos Tap en “Generar nuevo código" y la aplicación nos mostrara un **Token** que expira en 2 mins y que tendremos que colocar en el campo **Token de Latch** para sincronizar el usuario y el servicio deseado.

[![AriRRFRtjN8tzU5r1w-rhB6Kf9Qtkp1sJrTr8NblM9RT](/images/AriRRFRtjN8tzU5r1w-rhB6Kf9Qtkp1sJrTr8NblM9RT-169x300.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/arirrfrtjn8tzu5r1w-rhb6kf9qtkp1sjrtr8nblm9rt/)

Y listo, eso es todo, así de fácil tenemos un mecanismo de autenticación de dos factores en wordpress. En la aplicación de Latch el nuevo servicio ha sido agregado y desde ahí podemos gestionar el acceso.

[![Anh3sxKYUDk6DAos8KogaGncL3_Ujmj-JWm9d5O85ZCG](/images/Anh3sxKYUDk6DAos8KogaGncL3_Ujmj-JWm9d5O85ZCG-169x300.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/anh3sxkyudk6daos8kogagncl3_ujmj-jwm9d5o85zcg/)

Para hacer algunas pruebas cerramos sesión en wordpress y regresamos a la pantalla de login.

[![wordpress_login](/images/wordpress_login.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/wordpress_login/)

Intentaremos entrar al administrador del sitio con nuestras credenciales validas (usuario y contraseña de nuestra cuenta), aunque los datos de acceso son los correctos WordPress nos muestra un error de acceso

[![login_fail](/images/login_fail.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/login_fail/)

Y en la **app** también se nos notifica de un intento de acceso no autorizado al servicio.

[![AvfXza1l9bvg7mLYxnwpEv2BDjNRr8jBKJgulqsgIE3E](/images/AvfXza1l9bvg7mLYxnwpEv2BDjNRr8jBKJgulqsgIE3E-169x300.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/avfxza1l9bvg7mlyxnwpev2bdjnrr8jbkjgulqsgie3e/)

Para poder acceder normalmente, primero en la app tenemos que desbloquear el servicio (hacemos slide para bloquear y desbloquear)

[![AuYBLlyLZn41M-j3KNsVXUIUOpvtrhv0Sek_hZyo5KM3S](/images/AuYBLlyLZn41M-j3KNsVXUIUOpvtrhv0Sek_hZyo5KM3S-169x300.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/auybllylzn41m-j3knsvxuiuopvtrhv0sek_hzyo5km3s/)

Intentamos loguearnos de nuevo en el administrador de wordpress y ahora si nos dará acceso.

[![wordpress_dashboard](/images/wordpress_dashboard.jpg)](http://www.alevsk.com/2015/10/latch-plugins-contest-2015-tutorial-de-instalacion-en-wordpress/wordpress_dashboard/)

Si quieren aprender mas acerca del funcionamiento interno de **Latch**, protocolos de comunicación seguros y temas criptograficos pueden leer su documentación en el [área de desarrolladores](https://latch.elevenpaths.com/www/)

Happy Hacking 🙂
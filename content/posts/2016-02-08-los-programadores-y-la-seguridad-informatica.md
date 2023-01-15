---
title: Los programadores y la seguridad informática
author: Alevsk
type: post
date: 2016-02-08T02:06:38+00:00
url: /2016/02/los-programadores-y-la-seguridad-informatica/
categories:
  - Geek
  - Ethical Hacking
  - IT News
  - Personal
  - Sin categoría
  - Technology
  - Tips
tags:
  - android
  - desarrollo
  - hacking
  - ios
  - owasp
  - Programming
  - software
  - software libre
  - Solutions
  - Technology

---
En esta ocasión quiero compartir con ustedes una pequeña experiencia que me sucedió en uno de los muchos grupos de programadores a los que pertenezco en la red social Facebook, esta anécdota me hizo reflexionar acerca del nivel de cultura de seguridad informática que tenemos en México y al final me hizo terminar escribiendo este post a manera de auto crítica constructiva para la misma comunidad de desarrolladores.

Son muchos y muy variados los grupos de programación que uno encuentra Facebook: **desarrolladores web**, **desarrolladores iOS / Android**, **desarrolladores C#**, **desarrolladores de videojuegos** y todo lo que uno se imagine; esta funcionalidad de Facebook (los grupos) ha pasado a sustituir los antiguos foros de discusión (como smf o phpbb) para la generación millennial ya que de alguna forma es mucho mas cómodo tener todo integrado en la misma plataforma social, pero ese no es el tema de discusión aquí.

## La Anécdota

Lo que verdaderamente me llamo la atención fue hace unos días cuando un miembro del grupo hizo una consulta acerca de cómo podía realizar una validación de correo electrónico en un sistema que estaba desarrollando, no me llamo la atención la duda, pues todos los días hay gente que pregunta y mucha otra que le responde, lo que me llamo la atención fue la respuesta que le dio una persona del grupo y sobre todo la convicción con la que escribió la misma.

<div class="wp-caption aligncenter" id="attachment_3763" style="width: 518px">
[![La imagen esta censurada por que la idea no es quemar a nadie sino más bien sacar algo bueno de todo esto.](/images/facebook_fail.jpg)](http://www.alevsk.com/2016/02/los-programadores-y-la-seguridad-informatica/facebook_fail/)
<p class="wp-caption-text" id="caption-attachment-3763">
    La imagen esta censurada por que la idea no es quemar a nadie sino más bien sacar algo bueno de todo esto.
  </p>
</div>

En cuanto termine de leer su respuesta no pude esperar para unirme a su conversación y explicarle por qué su solución era incorrecta desde el punto de vista de seguridad, lo bueno fue que no lo tomo mal y se interesó bastante en el tema.

La solución del comentario de **Facebook** va más o menos así

[![mail_fail](/images/mail_fail.jpg)](http://www.alevsk.com/2016/02/los-programadores-y-la-seguridad-informatica/mail_fail/)

## ¿Pueden ver dónde está el problema de su solución?

La solución iba bien hasta el momento en donde decide regresar el token aleatorio al navegador del usuario y realizar ahí la validación. Explicando un poco más acerca de por qué este esquema de solución era malo le mostré un escenario en donde un atacante podría crear miles de cuentas saltando su sistema de verificación.

Haciendo un pequeño ejercicio de reflexión le propuse lo siguiente:

Partimos de la siguiente premisa: el objetivo del sistema de activación por correo es validar una identidad (así como detener posibles ataques automatizados que te creen cuentas falsas y te llenen la base de datos de usuarios ficticios), para lograr esto se utiliza el concepto de **“secreto"**, un secreto es un token que debe ser compartido solamente con el usuario mediante el método que él especifico (**el correo electrónico**), enviando ese token al correo que se supone tiene acceso y es el único medio en el que pueda recibir ese secreto nos aseguramos que la cuenta que el usuario especifico existe y es válida, por lo tanto su identidad ha sido avalada por un proveedor de correo.

Ahora, en el escenario que nos plantean de realizar toda la validación del lado del cliente el problema es que realmente no estas validando nada, si el servidor le está regresando al navegador mediante Ajax el token que se supone el usuario debe escribir ¿Cuál es el punto pedirle revisar su correo? Fácilmente se podría crear un bot que registrara cuentas y las activara de forma masiva, es por eso que no es una buena solución. 

[![source-code-583537_1280](/images/source-code-583537_1280.jpg)](http://www.alevsk.com/2016/02/los-programadores-y-la-seguridad-informatica/source-code-583537_1280/)

La solución óptima seria (o al menos como se usa en la **industria de software** hoy en día): 

Al momento de crear el usuario en la base de datos debemos manejar un campo para representar el estado actual de su cuenta (activada o desactivada), y cuando el usuario reciba el token por correo este lo introduce en un formulario y es enviado para su comparación del lado del servidor (el token generado también debimos haberlo almacenado de alguna forma en el servidor) y dependiendo de si es válido o no activamos su cuenta.

Lo que me interesaba al final es dejarles en claro que todo el código y los datos (por ejemplo funciones de validación en JavaScript) que enviemos al navegador pueden ser modificados por el usuario, y por lo tanto jamás debemos confiar en esa información.

Bueno aquí termina la anécdota, satisfecho de saber que al menos ese programador siguiendo mis recomendaciones seria capas de lanzar ese componente de forma segura a producción me puse a pensar en todos los demás desarrolladores que tienen dudas pero por X o Y motivo no preguntan y siguen produciendo mas y mas código vulnerable que al final contribuye a llenar las bases de datos sobre hackeos de sitios como [https://haveibeenpwned.com](https://haveibeenpwned.com) o [http://www.zone-h.org/](http://www.zone-h.org/)

## Mi opinión

Como muchos sabrán, actualmente soy consultor de seguridad informática, sin embargo tengo una formación de desarrollador de software, antes de dedicarme a la seguridad y durante la universidad cree muchísimas plataformas web y aplicaciones móviles (y lo sigo haciendo de vez en cuando como FreeLancer xd), estoy convencido de que al realizar una **prueba de penetración** en algún sistema o aplicación, en el 95% de los casos los hackeos se hubieran evitado si el software hubiera sido diseñado con la seguridad en mente.

Desarrollar software seguro no es una tarea sencilla, nadie nunca lo dijo, pero las empresas de desarrollo y pequeñas agencias tienen la manera de mitigar este problema.

## Capacitación del personal

En mi opinión por cada equipo de desarrolladores debería de haber por lo menos una persona con nociones básicas de seguridad, “Nociones básicas" es un término muy relativo, es por eso que las empresas (lideres técnicos, Project managers, IT managers, etc.) deberían voltear a ver estándares y buenas prácticas de seguridad en el desarrollo de software y no solo eso, integrarlas en su ciclo de desarrollo.

Hay un documento que me gusta recomendar bastante.

[OWASP Top 10: los diez riesgos más críticos en aplicaciones web](https://www.owasp.org//images/5/5f/OWASP_Top_10_-_2013_Final_-_Espa%C3%B1ol.pdf)

Este documento explica **las diez vulnerabilidades más populares en las aplicaciones web** hoy en día, así como su riesgo, impacto y mitigación.

[![owasp](/images/owasp.jpg)](http://www.alevsk.com/2016/02/los-programadores-y-la-seguridad-informatica/owasp/)

Ya sea que trabajes para una empresa o seas un desarrollador FreeLancer, te aseguro que si desarrollas tu software tomando como referencia los 10 puntos de **OWASP** tu aplicación sera lo suficientemente robusta para que no venga cualquier lammer / hackerucho de tercera y vulnere tu sistema usando sus herramientas automatizadas.

Como decía mas arriba, producir software seguro es compromiso de todos, las metodologías de desarrollo ágil como **SCRUM** son buenas y funcionan, pero muchas veces el personal que las lleva acabo deja de lado el tiempo requerido para hacer un buen **diseño de software** (con la seguridad en mente, programación defensiva, etc.) o lo minimiza

Aunque lo ideal sería tener un departamento de seguridad que apoyara al departamento de desarrollo durante todo el ciclo de vida del proyecto.

Después de todo, ¿cuánto te cuesta contratar un arquitecto de seguridad? ¿Cuánto te costaría recuperarte de un hackeo (hablando de información, dinero y prestigio de la empresa)?
---
title: OWASP – Riviera Maya e introducción a Overthewire CTF
author: Alevsk
type: post
date: 2018-05-28T03:43:48+00:00
url: /2018/05/owasp-riviera-maya-2018/
categories:
  - Ethical Hacking
  - Personal
  - Talks and Events
  - Programming
  - Tutorials
tags:
  - capture the flag
  - ctf
  - hacking
  - Ethical Hacking
  - owasp

---
[![](/images/31144258_650313688647156_2900367579634874774_n.jpg)](http://www.alevsk.com/2018/05/owasp-riviera-maya-2018/31144258_650313688647156_2900367579634874774_n/)

El 20 y 21 de abril de este año se llevo a cabo la segunda edición de [OWASP – Riviera Maya](https://www.owasp.org/index.php/Riviera_Maya) en Cancún, evento de seguridad al cual tuve la fortuna de asistir y donde coincidí con varios amigos de la seguridad informática: [@hkm](https://twitter.com/_hkm), [@calderpwn](https://twitter.com/calderpwn), [@nitr0us](https://twitter.com/nitr0usmx), dex, [@tresvecesdobleu](https://twitter.com/tresvecesdobleu), [@NoxOner](http://@NoxOner ‏), [@acorazada](https://twitter.com/acorazada), [@jjtibaquira](https://twitter.com/jjtibaquira) son algunos de los que me vienen a la mente ahora mismo (una disculpa si me olvidé de alguno), en lo personal creo que esto es lo mejor de este tipo de eventos 🙂

El staff del evento ha publicado algunos videos de las charlas que podrán encontrar en el canal de youtube de [OWASP Latam](https://www.youtube.com/channel/UCEXEarSUAfgcll1uzxcNGUA)



Durante el evento tome el taller de web hacking impartido por [Eduardo Vela (sirdarckcat)](https://twitter.com/sirdarckcat), el formato era muy parecido a un [CTF](https://en.wikipedia.org/wiki/Capture_the_flag#Computer_security) en donde ibas resolviendo cada uno de los niveles explotando vulnerabilidades web especificas ([XSS](https://en.wikipedia.org/wiki/Cross-site_scripting), [SQLi](https://en.wikipedia.org/wiki/SQL_injection), [LFI](https://en.wikipedia.org/wiki/File_inclusion_vulnerability), etc). Este tipo de vulnerabilidades web han existido durante los últimos 20 años pero creo que la finalidad del taller era demostrar que siempre habra nuevas formas de seguir aprovechandolas.

Jugar **CTFs** me divierte mucho ya que siempre se aprende algo nuevo (en el pasado he publicados algunos como [#CPMX6 CTF][1]) y este no fue la excepción, al final logre completar todos los retos y Eduardo me dijo que fui el único que lo hizo 😳

[![](/images/google-ctf-1200x745.jpg)](http://www.alevsk.com/2018/05/owasp-riviera-maya-2018/google-ctf/)

Ahora que estoy dedicado el 99% del tiempo al desarrollo de software (ocasionalmente hago algún freelance que tiene que ver con Pentest o revisiones de código) lo mas cercano al hacking que hago son **CTFs** (justo ahora me estoy preparando para jugar el [Google – Capture the flag 2018][2]) y entonces pensé que hay muchísima gente interesada en este tipo de **competencias de hacking** pero no saben bien por donde empezar y decidí comenzar una nueva serie de tutoriales donde resolveremos un CTF paso a paso 🙂

Me di a la tarea de investigar varios de los CTFs que hay en Internet (básicos, intermedios, avanzados, imposibles, etc…) y creo que el mejor para principiantes se encuentra en [OverTheWire][3], la idea es que resolveremos el CTF llamado [Natas][4] donde aprenderemos lo básico de **web y mobile hacking** y terminando esta serie (son 33 niveles) nos moveremos a algo un poco mas intermedio/avanzado donde tengamos que hacer **binary exploitation**.

Bueno, pues comenzamos….

# Natas CTF

Este CTF, a diferencia de otros como los jeopardy que te dejan jugar los niveles en el orden que tu decidas, te forzá a resolver el nivel actual antes de pasar al siguiente, entonces debemos comenzar por [Natas0](http://overthewire.org/wargames/natas/natas0.html)

```bash
Username: natas0  
Password: natas0  
URL: http://natas0.natas.labs.overthewire.org
```

Vamos a la URL que nos indican las instrucciones, introducimos las credenciales que nos da el reto y veremos una pantalla como la siguiente:

[![](/images/Screen-Shot-2018-05-15-at-10.47.13-PM-1200x318.png)](http://www.alevsk.com/2018/05/owasp-riviera-maya-2018/screen-shot-2018-05-15-at-10-47-13-pm/)

Nos dice que el password se encuentre en esta misma pagina sin embargo no vemos nada que haga referencia a la contraseña.

Esta es la primera lección para los principiantes de los CTFs, lo primero que tenemos que hacer en la mayoría de los casos es ver el código fuente de las paginas.

[![](/images/Screen-Shot-2018-05-15-at-10.47.53-PM-1200x619.png)](http://www.alevsk.com/2018/05/owasp-riviera-maya-2018/screen-shot-2018-05-15-at-10-47-53-pm/)

La contraseña para natas1 es **gtVrDuiDfck831PqWsLEZy5gyDz1clto**, felicidades ahora podemos continuar con el nivel 1, tratare de ir publicando los siguientes artículos cada 2 o 3 días así que estén pendientes.

Happy hacking 🙂

 [1]: https://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/
 [2]: https://security.googleblog.com/2018/05/google-ctf-2018-is-here.html
 [3]: http://overthewire.org/wargames/
 [4]: http://overthewire.org/wargames/natas/
---
title: Servidores de Riot Games se ven afectados por ataques DDOS
author: Alevsk
type: post
date: 2014-06-15T00:56:32+00:00
url: /2014/06/servidores-de-riot-games-se-ven-afectados-por-ataques-ddos/
categories:
  - Geek
  - Gaming
  - IT News
tags:
  - DDOS
  - hackers
  - Gaming
  - Personal
  - Programming
  - Solutions
  - web

---
**League of legends** es víctima de **ataques de denegación de servicio** aparentemente adjudicado al grupo **hacker** ruso **pro dota2**. varios servicios de riot están siendo afectados por estos **ataques DDos** desde ayer por la tarde, lo cual afecta a los servidores y pagina web en las regiones: LAS,NA,BR,LAN, los atacantes publicaron un comunicado en el foro de [league of legends de reddit](http://www.reddit.com/r/leagueoflegends) explicando cuales eran sus intenciones.

Por su parte, un ingeniero de soporte de Riot Games en un comunicado (antes de que los foros estuvieran offline) público el siguiente mensaje:

[![lol_ddos_1](/images/lol_ddos_1.png)](http://www.alevsk.com/2014/06/servidores-de-riot-games-se-ven-afectados-por-ataques-ddos/lol_ddos_1/)

De acuerdo a lo que he investigado, esta vez la vulnerabilidad fue explotada en los servidores de chat del juego usando herramientas de Chat Spam Flood, fue debido a eso que ayer por la noche ningún usuario tenía acceso al chat del cliente en los servidores LAS, NA, BR y LAN. Haciendo algunas pruebas en el pasado note que league of legends no validaba el número de dispositivos que iniciaban sesión en el servidor con una misma cuenta, seguramente alguien se colgó de esta vulnerabilidad y con el uso de una botnet realizo un DDOS, esa es mi primera hipótesis.

Pero continuemos, no falto mucho para que (como ya es costumbre) salieran los lammos en busca de los reflectores, durante el incidente se crearon fanpages en Facebook y cuentas en twitter de personas adjudicándose el ataque

[![lol_ddos_1](/images/lol_ddos_11.png)](http://www.alevsk.com/2014/06/servidores-de-riot-games-se-ven-afectados-por-ataques-ddos/lol_ddos_1-2/)

_Supuesta cuenta de twitter en donde un lammer brasileño se jacta de que el servidor esta offline_

[![lol_ddos_1](/images/lol_ddos_12.png)](http://www.alevsk.com/2014/06/servidores-de-riot-games-se-ven-afectados-por-ataques-ddos/lol_ddos_1-3/)

_Página de Facebook del supuesto grupo que realizo el ataque (página con 10 minutos de creación, avatar de Amon de la leyenda de Korra?? Enserio?)_

No es la primera vez que Riot Games recibe este tipo de ataques, y estoy seguro que no será el último, parchar una vulnerabilidad de este tipo te puede llevar algo de tiempo (los que han trabajado en diseño y aplicación de **infraestructura tecnológica** entenderán :)), no puedes mitigar el problema aplicando una tecnología así nada más, se debe de hacer un análisis antes de ver como impactara en lo que ya tienes, porque claro, lo último que quieres es que tú mismo vayas a romper algo en tus sistemas ;).

Lo que si es cierto es que mientras el tiempo pasa la comunidad se desespera más y más, y Riot Games pierde dinero $$$ :S.

También es cierto es que Riot también dio el comunicado de que emprenderá acciones legales contra quien resulte responsable, como fue el caso del grupo [Derp hacking group que emprendió una campaña de ataque de denegación de servicios contra usuarios de twitch tv](http://www.pcgamesn.com/leagueoflegends/ddos-attacks-against-league-legends-and-dota-2-twitch-streamer-end-gunpoint-arrest) que realizaban stream de league of legends

[![lol_ddos_1](/images/lol_ddos_13.png)](http://www.alevsk.com/2014/06/servidores-de-riot-games-se-ven-afectados-por-ataques-ddos/lol_ddos_1-4/)

salu2
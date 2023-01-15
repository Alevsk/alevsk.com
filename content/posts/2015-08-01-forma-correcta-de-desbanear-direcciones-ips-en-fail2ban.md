---
title: Desbanear IPs en fail2ban de forma correcta
author: Alevsk
type: post
date: 2015-08-01T19:21:51+00:00
url: /2015/08/forma-correcta-de-desbanear-direcciones-ips-en-fail2ban/
categories:
  - Linux
  - Technology
  - Tips
  - Tutorials
tags:
  - debian
  - fail2ban
  - software libre
  - Solutions
  - sysadmin
  - Technology
  - Tutorials

---
Este post es más un recordatorio para mí pero sigue siendo un buen material de consulta para sysadmins.

[Fail2ban][1] es una herramienta bastante popular entre administradores de sistemas ya que nos permite añadir una capa de seguridad extra a nuestro servidor, viene con algunas reglas de seguridad pre configuradas para proteger servicios como ssh y apache, sin embargo es lo suficientemente flexible y fácil de utilizar para que nosotros creemos y agreguemos todas las que necesitemos, pero bueno este tutorial no es acerca de cómo crear esas reglas sino de cómo desbanear ciertas IPs que hayamos baneado por equivocación.

# En el mejor de los casos

**fail2ban** utiliza la utilidad [iptables](https://en.wikipedia.org/wiki/Iptables), lo primero que haremos será encontrar que tipo de restricción se le aplico a la ip baneada

```bash
# iptables -L -n | less
```

[![2](/images/2.jpg)](http://www.alevsk.com/2015/08/forma-correcta-de-desbanear-direcciones-ips-en-fail2ban/2-2/)

Como podemos ver, la ip afectada es **187.240.213.48** y está dentro del **JAIL** fail2ban-ssh o simplemente **ssh** (quiten le la parte de fail2ban-*), fail2ban utiliza un sistema de **JAILS** (jaulas / prisiones / cárceles) bastante interesante con el cual podemos agrupar ips en grupos y aplicar ciertas reglas a todas ellas al mismo tiempo, les dejo más documentación al respecto: [control de jails en fail2ban](http://www.fail2ban.org/wiki/index.php/Commands#JAIL_CONTROL)

Si queremos saber el nombre de todas las JAILS que está corriendo fail2ban actualmente lo haremos con el comando

```bash
# fail2ban-client status
```

[![4](/images/4.jpg)](http://www.alevsk.com/2015/08/forma-correcta-de-desbanear-direcciones-ips-en-fail2ban/attachment/4/)

Este comando nos sirve para corroborar el nombre de la **JAIL** que vamos a manipular, podemos observar que tenemos muchas más ademas de **ssh**, por ejemplo **apache**, **apache-myadmin**, **apache-overflows**, etc … continuamos.

Ahora que conocemos en detalle la IP y la JAIL vamos a remover la restricción utilizando:

```bash
# fail2ban-client get ssh actionunban 187.240.213.48
```

Para versiones más nuevas de **fail2ban**, digamos 0.9.x seria:

```bash
# fail2ban-client set ssh unbanip 187.240.213.48
```

Y listo, con esto nos aseguramos de remover las restricciones solo a una dirección IP en específico 🙂

Podemos revisar si efectivamente la IP fue removida con el comando:

```bash
# iptables -L -n | grep '187.240.213.48'
```

Si el comando no nos regresa nada significa que no pude encontrar una coincidencia de '187.240.213.48' en el output del iptables y por lo tanto la IP ya no está baneada.

# En el peor de los casos

Sin embargo, si la consola les muestra algo como esto:

[![6](/images/6.jpg)](http://www.alevsk.com/2015/08/forma-correcta-de-desbanear-direcciones-ips-en-fail2ban/attachment/6/)

Y tienen la mala suerte de estar trabajando con un **fail2ban version 0.8.6** como yo, significa que la **IP** no pudo ser desbaneada, haciendo un poco de investigación se trata de un bug muy <del datetime="2015-08-01T18:30:47+00:00">nefasto</del> popular en esta versión, intentamos remover la restricción de nuevo, esta vez utilizando el debug

```bash
# fail2ban-client -vvv get ssh actionunban 187.240.213.48
```

[![error](/images/error.jpg)](http://www.alevsk.com/2015/08/forma-correcta-de-desbanear-direcciones-ips-en-fail2ban/error/)

Ahí observamos que la falla está en los comandos que se aplican, podemos solucionar esto de dos formas, la primera es actualizando el servicio y la segunda es removiendo la dirección IP de forma manual que fue lo que yo hice, no es tan complicado 🙂

```bash
# IP=187.240.213.48  
# cat /var/log/fail2ban.log | grep -v $IP > /tmp/fail2ban.tmp  
# cp /tmp/fail2ban.tmp /var/log/fail2ban.log  
# iptables -D fail2ban-ssh -s $IP -j DROP
```

Revisamos de nuevo si efectivamente la IP fue removida

```bash
# iptables -L -n | grep '187.240.213.48'
```

Y esta vez no debería de mostrarnos nada.

salu2

 [1]: http://www.fail2ban.org/wiki/index.php/Main_Page
---
title: Ettercap potente herramienta de auditorias Lan
author: Alevsk
type: post
date: 2010-07-04T17:02:14+00:00
url: /2010/07/ettercap-potente-herramienta-de-auditorias-lan/
image:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/ettercap.jpg
slider_thumbnail:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/thumb-lan.jpg
categories:
  - Ethical Hacking
  - Linux
  - Networking
  - Tutorials
tags:
  - backtrack
  - campus party
  - Linux Debugging
  - debian
  - distros
  - grep
  - grub
  - Linux
  - Programming
  - shell
  - slackware
  - software libre
  - Technology
  - Tutorials
  - ubuntu

---
[![](/images/robot_bt.jpg)](http://www.alevsk.com/2010/07/ettercap-potente-herramienta-de-auditorias-lan/robot_bt/)

Bueno quiero hacer algo de post informativos, primero que nada veamos el concepto de la wikipedia:

**Ettercap** es un interceptor/[sniffer][1]/registrador para LANs con [switch][2]. Soporta direcciones activas y pasivas de varios protocolos (incluso aquellos cifrados, como [SSH][3] y [HTTPS][4]). También hace posible la inyección de datos en una conexión establecida y filtrado al vuelo aun manteniendo la conexión sincronizada gracias a su poder para establecer un [Ataque Man-in-the-middle][5]([Spoofing][6]). Muchos modos de sniffing fueron implementados para darnos un conjunto de herramientas poderoso y completo de sniffing.

<!--more-->
<span>Analicemos:</span> Ettercap es una aplicación que existe tanto para sistemas windows como linux y su función principal es la de analizar la información que pasa en una red lan, valiéndonos de conocidas técnicas como lo es el man in the middle, anteriormente había publicado un vídeo tutorial de demostración de dicha técnica, pueden verlo [aqui][7], seguimos.

<span>Entre las funciones mas destacadas se encuentran:</span>
<span>Compatibilidad con SSH1:</span> puede interceptar users y passwords incluso en conexiones “seguras" con SSH. (ya saben, cuando nos conectamos a un servidor usando el putty que trae soporte para ssh o cosas asi)

<span>Compatibilidad con HTTPS:</span> intercepta conexiones mediante http SSL (supuestamente seguras) incluso si se establecen a través de un proxy.

<span>Intercepta tráfico remoto mediante un túnel GRE:</span> si la conexión se establece mediante un túnel GRE con un router Cisco, puede interceptarla y crear un ataque “Man in the Middle".

<span>“Man in the Middle"</span> contra túneles PPTP (_Point-to-Point Tunneling Protocol_).  
(Personalmente mi técnica favorita :D)

También se le pueden agregar algunos plugins extras además de los que ya trae como por ejemplo:

<span>Colector de contraseñas en:</span> [Telnet][8], [FTP][9], [POP][10], [Rlogin][11], [SSH1][12], [ICQ][13], [SMB][14], [MySQL][15], [HTTP][16], [NNTP][17], [X11][18], [Napster][19], [IRC][20], [RIP][21], [BGP][22], [SOCKS 5][23], [IMAP 4][24], [VNC][25], [LDAP][26], [NFS][27], [SNMP][28], [Half-Life][29], [Quake3][30], [MSN][31], [YMSG][32].

<span>Filtrado y sustitución de paquetes.</span>
<span>OS fingerprint:</span> es decir, detección del sistema operativo remoto.  
(Algo parecido a lo que hace el nmap -O)

<span>Mata conexiones.</span> (Leease DOS xD)

<span>Escáner de LAN:</span> hosts, puertos abiertos, servicios…  
(hay algo mas que decir de esto :P)

<span>Busca otros envenenamientos en la misma red.</span>  
Este plugin es muy bueno por que nos muestra si hay alguien mas que esta intentando jugar con la red en la que nosotros jugamos

<span>Port Stealing (robo de puertos): </span>es un nuevo método para el sniff en redes con switch, sin envenenamiento ARP".

Ettercap nos propone dos modos, el por defecto (unified sniff) o el bridget sniff, unos siendo interactivo y el otro no.

Una vez que empieza a rastrear el tráfico, obtendrás un listado de todas las conexiones activas, junto a una serie de atributos acerca de su estado (active, idle, killed, etc.). El asterisco indica que una contraseña fue recogida en esa conexión. (Esta info fue obtenida de la página oficial del Ettercap y nos da una idea de lo potente que es esta herramienta).

<span>Instalación<br/> </span>

Si lo queremos instalar mediante las fuentes primero tenemos que estar seguros que tenemos la libreria, la podemos instalar mediante el gestor de paquetes asi:

```Text only
#apt-get install libpcre3-dev  libpcap0.8-dev libnet0 libnet1-dev libssl-dev ncurses-bin ncurses5-dev

```
<span>Nota: Súper importante tener todas esas librerías instaladas de otra manera ettercap no funcionara correctamente, hagan lo que tengan que hacer pero instalen las, si tienen dudas pregunten 🙂</span> <span>en especial la librería ncurses5-dev que es la mas difícil de encontrar</span>

Ahora descargamos el ettercap 0.7.3 de [http://ettercap.sourceforge.net/](http://ettercap.sourceforge.net/) y lo descomprimimos

Cambien se puede instalar el ettercap mediante el gestor de paquetes pero no es recomendable puesto que no trae todos los plugins, yo recomiendo descargarlo de la web oficial y compilarlo

Aca una versión ya lista que encontré:  
Versión compilada completa [http://antraxactive.com/ettercap-ng-0.7.3_0.7.3-1_i386.deb](http://antraxactive.com/ettercap-ng-0.7.3_0.7.3-1_i386.deb)

Ya que hemos descargado y descomprimimos tan solo nos vemos hasta esa carpeta (directorio) con la consola y escribimos.

```Text only
#  ./configure --enable-plugins --enable-debug

```

Si todo salio bien debe aparecer esto en la consola

```verilog
==================================================

Install  directory: /usr/local
Libraries :
LIBPCAP ................ default
LIBNET  ................. default
LIBSSL ................. default
NCURSES  ................ default
GTK+ ................... yes
Functionalities  :
Debug mode ............. yes
Plugin support ......... yes
Passive  DNS ............ yes
Perl regex in filters .. yes
Iconv UTF-8  support .... yes
==================================================
```

Luego seguimos con un make, make install o checkinstall y ya tendremos instalado nuestro flamante ettercap listo para ejecutarse y con todos los plugins listo para putear redes :p

Para comenzar a usarlo tenemos que ser roots y escribir asi en la shell

```Text only
# ettercap  -C

```

Para el modo consola que particularmente es el que mas me gusta

<span>Tambièn esta el modo texto y el modo GUI osea con interfaz gráfica el cual podemos acceder así:</span>
```Text only
# ettercap -T

```

Modo texto

```Text only
ettercap -G

```

Modo GUI

**Configurar ettercap para el correcto uso de SSL**

Tenemos que hacer unas configuraciones previas para que que podamos intervenir las comunicaciones seguras SSL, hacer de intermediario y poder ver la informacion cifrada cuando comienze el sniffeo, para ello abrimos con nuestro editor favorito el archivo /usr/local/etc y en caso de que usemos iptables (casi seguro) tendremos que ir a la línea donde dice

```Text only
redir_command_on  ="iptables -t nat -A PREROUTING -i %iface -p tcp --dport %port -j  REDIRECT --to-port %rport"

```

cambiar eso por esto:

```Text only
redir_command_on  = "iptables -t nat -A PREROUTING -i %iface -p tcp --dport %port -j  REDIRECT --to-port %rport"

```

De esta manera las conexiones SSL sera interceptadas correctamente 😉

**Vean a ettercap en accion**  


salu2

 [1]: http://es.wikipedia.org/wiki/Sniffer "Sniffer"
 [2]: http://es.wikipedia.org/wiki/Switch "Switch"
 [3]: http://es.wikipedia.org/wiki/SSH "SSH"
 [4]: http://es.wikipedia.org/wiki/HTTPS "HTTPS"
 [5]: http://es.wikipedia.org/wiki/Ataque_Man-in-the-middle "Ataque Man-in-the-middle"
 [6]: http://es.wikipedia.org/wiki/Spoofing "Spoofing"
 [7]: http://alevsk-zone.blogspot.com/2009/06/dns-spoofing-technique-by-alevsk.html
 [8]: http://es.wikipedia.org/wiki/Telnet "Telnet"
 [9]: http://es.wikipedia.org/wiki/File_Transfer_Protocol "File  Transfer Protocol"
 [10]: http://es.wikipedia.org/wiki/POP "POP"
 [11]: http://es.wikipedia.org/wiki/Rlogin "Rlogin"
 [12]: http://es.wikipedia.org/w/index.php?title=SSH1&action=edit&redlink=1 "SSH1 (aún no redactado)"
 [13]: http://es.wikipedia.org/wiki/ICQ "ICQ"
 [14]: http://es.wikipedia.org/wiki/SMB "SMB"
 [15]: http://es.wikipedia.org/wiki/MySQL "MySQL"
 [16]: http://es.wikipedia.org/wiki/HTTP "HTTP"
 [17]: http://es.wikipedia.org/wiki/NNTP "NNTP"
 [18]: http://es.wikipedia.org/wiki/X11 "X11"
 [19]: http://es.wikipedia.org/wiki/Napster "Napster"
 [20]: http://es.wikipedia.org/wiki/IRC "IRC"
 [21]: http://es.wikipedia.org/wiki/RIP "RIP"
 [22]: http://es.wikipedia.org/wiki/BGP "BGP"
 [23]: http://es.wikipedia.org/w/index.php?title=SOCKS_5&action=edit&redlink=1 "SOCKS 5 (aún no redactado)"
 [24]: http://es.wikipedia.org/w/index.php?title=IMAP_4&action=edit&redlink=1 "IMAP 4 (aún no redactado)"
 [25]: http://es.wikipedia.org/wiki/VNC "VNC"
 [26]: http://es.wikipedia.org/wiki/LDAP "LDAP"
 [27]: http://es.wikipedia.org/wiki/NFS "NFS"
 [28]: http://es.wikipedia.org/wiki/SNMP "SNMP"
 [29]: http://es.wikipedia.org/wiki/Half-Life "Half-Life"
 [30]: http://es.wikipedia.org/w/index.php?title=Quake3&action=edit&redlink=1 "Quake3 (aún no redactado)"
 [31]: http://es.wikipedia.org/wiki/MSN "MSN"
 [32]: http://es.wikipedia.org/wiki/YMSG "YMSG"
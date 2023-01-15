---
title: MySQL.com vulnerado y los passwords publicados
author: Alevsk
type: post
date: 2011-03-28T04:22:58+00:00
url: /2011/03/mysql-com-hackeado/
categories:
  - Ethical Hacking
  - Linux
  - IT News
  - Technology
tags:
  - backtrack
  - debian
  - distros
  - hackers
  - Linux
  - Programming
  - slackware

---
[![](/images/data_base.jpg)](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-3/data_base/)

**MYSQL.com** (el sitio oficial del gestor de base de datos **MySQL**) ha sido vulnerado por una conocida como [**blind SQL injection**][1] o inyección de codigo sql a ciegas. Un anuncio ha sido publicado hoy **27 de marzo de 2011** donde se explica (**full disclosure**) como es que los **crackers** lograron dumpear parte de la estructura de la base de datos. 

<div class="demobox" style="height:120px;">
  Vulnerable Target : http://mysql.com/customers/view/index.html?id=1170<br/> Host IP : 213.136.52.29<br/> Web Server : Apache/2.2.15 (Fedora)<br/> Powered-by : PHP/5.2.13<br/> Injection Type : MySQL Blind<br/> Current DB : web
</div>

Al parecer los atacantes lograron explotar la vulnerabilidad en la aplicación de clientes que maneja el portal y de esta forma tener acceso a la base de datos interna, tablas, contraseñas, nombres de usuario.

Se recomienda que si tienes una cuenta en el portal de **MySQL.com** cambies inmediatamente la contraseña (especialmente si es la que usas en todos los demás sitios jeje).

La manera en que los administradores de seguridad se dieron cuenta del problema fue debido a que los **crackers** publicaron una lista de usuarios y contraseñas en diversos foros del underground informático, y claro algunas personas comenzaron a usar las cuentas de usuario para sacar provecho. 

echando un vistazo a la lista de usuarios y contraseñas la verdad que su complejidad deja mucho que desear, por ejemplo, había una contraseña de 4 digitos de un director director ejecutivo de una importante empresa mundial x'D.

La gente de MySQL todavía no han dicho nada acerca de este ataque, pero en cuanto sepa mas sobre esto lo posteo.

Los hackers rumanos TinKode y Ne0h publicaron un volcado de credenciales robadas de **MySQL.com, MySQL.fr, MySQL.de, MySQL.it y www-jp.mysql.com** en **paste.bin**. Entre los datos se incluye la pobre contraseña de 4 dígitos que Robin Schumacher, director de gestión de productos, utilizaba en su cuenta de **WordPress** para **blogs.mysql.com**.

Pueden leer el full disclosure [aqui][2]

salu2

 [1]: http://es.wikipedia.org/wiki/Blind_SQL_injection
 [2]: http://seclists.org/fulldisclosure/2011/Mar/309?utm_source=twitterfeed&utm_medium=twitter
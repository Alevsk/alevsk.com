---
title: Configuracion de host virtuales en MAC
author: Alevsk
type: post
date: 2011-04-29T04:18:05+00:00
url: /2011/04/configuracion-de-host-virtuales-en-mac/
categories:
  - Mac
  - Technology
  - Tips
  - Tutorials
tags:
  - backtrack
  - campus party
  - Linux Debugging
  - debian
  - distros
  - Linux
  - mac
  - Programming
  - Solutions
  - Tutorials
  - ubuntu

---
Hola lectores les comento que hace un par de dias comenze a usar una mac book pro :p y poco a poco he ido descubriendo todos sus secretos, tengo pensado en mas o menos una semana realizar un post titulo “**Experiencia de usuario Windows/Linux hacia MAC**" ya que es muy diferente la experiencia de usar **MAC** de un usuario que tiene unos años usando linux (como en mi caso) a un usuario que viene del Sistema Operativo Windows :), existe un avismo entre esos 2 sistemas operativos.

Pero bueno, les comento que estoy trabajando en algunos proyectos de desarrollo web y la primera cosa que tuve que hacer fue darme a la tarea de configurar un servidor web en **MAC** asi como configurar host virtuales para los distintos sitios en los que hiba a trabajar.

**¿Por que trabajar con host virtuales?**  
La principal razon es por que estoy trabajando con aplicaciones web que manejan **URL's amigables**, por todo ese tema del **SEO**, y pues forzosamente la aplicación tiene que estar en raíz.

Una vez con su [servidor apache activado][1], el servicio de PHP corriendo y MYSQL instalado, para configurar los **virtual host** o **host virtuales** en **MAC** lo que tenemos que hacer es lo siguiente:

Abrimos la consola (Terminal), pueden hacer clic en la lupa de spotlight (esto del spotlight me gusto mucho) y escribir “Terminal" y la primera opción que les de es esa, hacer click.

[![](/images/terminal.jpg)](http://www.alevsk.com/2011/04/configuracion-de-host-virtuales-en-mac/terminal/)

Escribimos el siguiente comando (/Applications/TextEdit.app/Contents/MacOS/TextEdit es como si escribieran el **gedit** o **kate** en linux, dependiendo si usan gnome o kde, aunque tambien pueden usar vim y abrir el archivo directo desde la **shell**)

```Text only
sudo /Applications/TextEdit.app/Contents/MacOS/TextEdit /private/etc/apache2/extra/httpd-vhosts.conf

```
[![](/images/httpd-vhosts.jpg)](http://www.alevsk.com/2011/04/configuracion-de-host-virtuales-en-mac/httpd-vhosts/)

Se van hasta abajo del archivo y encontraran unas lineas parecidas a estas:

```Text only

   DocumentRoot "/Library/WebServer/Documents"
   ServerName localhost


```

Entonces justo debajo de donde se cierra ****, copian y pegan otro bloque con los datos de su host virtual, por ejemplo yo creare 2 nuevos, el archivo se debería de ver de la siguiente forma.

```Text only

   DocumentRoot "/Library/WebServer/Documents"
   ServerName localhost



   DocumentRoot "/Users/alevsk/Sites/zonau"
   ServerName zonau.localhost



   DocumentRoot "/Users/alevsk/Sites/fastfoo"
   ServerName dae.localhost


```

Guardan y cierran su archivo, despues de nuevo en la **consola** tenemos que modificar el archivo **host** y agregar los nombres de nuestros host virtuales, en Linux este archivo se localiza en /etc/hosts, pero en **MAC** se encuentra en /private/etc/hosts, escriban en la **shell**

```Text only
sudo /Applications/TextEdit.app/Contents/MacOS/TextEdit /private/etc/hosts

```
[![](/images/hosts.jpg)](http://www.alevsk.com/2011/04/configuracion-de-host-virtuales-en-mac/hosts/)

casi llegando hasta abajo del archivo veran que hay una linea que dice **fe80::1%lo0 localhost**, justo debajo escriban el nombre de sus host virtuales, se debería de ver de la siguiente manera (mis host eran zonau y dae):

```Text only
fe80::1%lo0	localhost
127.0.0.1	zonau.localhost		localhost
127.0.0.1	dae.localhost		localhost

```

Ya con esto deberia de funcionar, pero como yo tengo que trabajar con las URL's amigables de una vez configuramos el **mod_rewrite** en **MAC**, para utilizar [cakePHP][2] por ejemplo, de nuevo guardamos todo lo que hayamos editado y regresamos a la consola y escribimos el siguiente comando:

```Text only
sudo /Applications/TextEdit.app/Contents/MacOS/TextEdit /etc/apache2/users/alevsk.conf

```
[![](/images/alevsk-conf.jpg)](http://www.alevsk.com/2011/04/configuracion-de-host-virtuales-en-mac/alevsk-conf/)

Donde dice **alevsk.conf** ustedes sustituyan lo por el nombre de su usuario para editar su archivo de configuración, por default la linea que dice **AllowOverride** tiene **none** asi que cambienlo a **all** y les deberia de quedar algo asi:

```Text only

	Options Indexes MultiViews FollowSymlinks
	AllowOverride all
	Order allow,deny
	Allow from all


```

El **AllowOverride all** nos permitira hacer uso de configuraciones que especifiquemos en los archivos **.htaccess**, guardamos y cerramos el archivo, despues de eso escribimos el siguiente comando para editar el archivo **httpd.conf**

```Text only
sudo /Applications/TextEdit.app/Contents/MacOS/TextEdit /private/etc/apache2/httpd.conf

```

Buscamos la linea donde se carga el modulo **rewrite** y vemos que por default viene comentado con un # así que lo removemos.

```Text only
#LoadModule rewrite_module libexec/apache2/mod_rewrite.so

```

Una vez removido el # la linea debería quedar así:

```Text only
LoadModule rewrite_module libexec/apache2/mod_rewrite.so

```

Después debemos habilitar el uso de host virtuales, buscamos la siguiente linea

```Tera Term macro
# Virtual hosts
#Include /private/etc/apache2/extra/httpd-vhosts.conf

```

Y des comentamos la linea donde tiene include, quedando de la siguiente forma:

```Tera Term macro
# Virtual hosts
Include /private/etc/apache2/extra/httpd-vhosts.conf

```

Tambien buscamos mas abajo el bloque donde este:

[![](/images/httpd.jpg)](http://www.alevsk.com/2011/04/configuracion-de-host-virtuales-en-mac/httpd/)
```Text only

    Options FollowSymLinks
    AllowOverride none
    Order deny,allow
    Deny from all


```

Y de la misma manera sustituimos el **none** por **all** quedando asi:

```Text only

    Options FollowSymLinks
    AllowOverride All
    Order deny,allow
    Deny from all


```

Por ultimo solo queda reiniciar el servidor.

```Text only
sudo apachectl restart

```

Después de eso si todo salió bien accedan a un navegador y escriban por ejemplo http://zonau.localhost/ y debería de cargar su sitio, y como esta en la raíz del **host** virtual (el **path** que especificaron anteriormente) las URL's amigables deberían de funcionar, cabe decir que con el uso de **virtual hosts** la estructura de nuestro servidor web queda mas ordenada :).

**Si tiene alguna duda por favor comenten y responderé a la brevedad posible.**

 [1]: http://www.alevsk.com/2011/04/configurar-servidor-web-mac-snow-leopard/
 [2]: http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-1/
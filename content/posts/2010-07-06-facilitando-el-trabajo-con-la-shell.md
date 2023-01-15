---
title: Facilitando el trabajo con la shell
author: Alevsk
type: post
date: 2010-07-06T21:23:30+00:00
url: /2010/07/facilitando-el-trabajo-con-la-shell/
image:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/optimizar.jpg
slider_thumbnail:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/thumb-ssh.jpg
categories:
  - Linux
  - Technology
  - Tutorials
tags:
  - filezilla
  - find
  - firebug
  - grep
  - linea de comandos
  - Linux
  - optimizar
  - putty
  - shell
  - trabajo
  - ubuntu
  - vim

---
<p style="text-align: left;">
  Últimamente en el trabajo tengo que corregir errores de diseño que vienen desde el código fuente en programación web, para hacer eso de la manera tradicional pues con filezilla accedemos por FTP y seria cuestión de comenzar a buscar los archivos necesarios, pero existen algunos tips, trucos o hacks (como lo quieran llamar) a continuación pondré algunos de los que yo uso para agilizar mi trabajo de detección de errores de código (así lo llamo yo :p)
</p>
<!--more-->
![](https://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/firebug.jpg)  
Utilizar firebug para detectar errores de diseño que nos den problemas o hasta incluso podemos modificar la web como si trabajáramos en el verdadero código fuente para cuando ya quede como nos guste solo cuestión de copy/paste

<p style="text-align: left;">
  Una vez que ya identificamos algunos problemas con Firebug, es mas facil encontrar por ejemplo una hoja de estilos, pero si nuestros problemas no son solo de diseño sino de programacion ahi podemos usar el segundo truco.<br/> ![](https://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/ssh.jpg)
</p>
<p style="text-align: left;">
  Una sesion SSH, con una session de Secure Shell podemos ahorrarnos muchisimo trabajo y problemas futuros ya que podemos crear rapidamente backups, encontrar archivos, frases, e incluso modificar los archivos directamente, todo desde un solo lugar 🙂
</p>
<p style="text-align: left;">
  Si usan windows una excelente herramienta es [Putty](None) y si usan alguna distro de Linux es casi seguro que ya viene precargado, abran una terminal y escriban:
</p>

```bash
alevsk@Aosnet:~$ ssh qondaaficionados.com
```

<p style="text-align: left;">
  Por ejemplo, el servidor responderá pidiendo la contraseña de usuario, de cual usuario?, pues en este caso mi usuario es alevsk, pero que pasa si intento conectarme a un servidor del cual no existe un usuario alevsk, muy facil:
</p>

```bash
alevsk@Aosnet:~$ ssh usuario@qondaaficionados.com
```  
La @ significa AT que quiere decir “de" o “pertenece a" pero eso es otra historia 🙂  
Una vez que ya accedimos al servidor donde esta alojada nuestra web o nuestro proyecto es mucho mas fácil por que es como si trabajáramos directamente en el servidor, mucho mas rápido y todo eso, una vez que ya identificamos los errores del lado del cliente con firebug ahora es el turno de usar la shell, ayudándonos de algunos comandos que nos facilitaran la vida por ejemplo  
**si queremos localizar un archivo:**

\[bash\]\[alevsk@282794-web1 ~\]$ find -name "index.php"[/bash]

<p style="text-align: left;">
  por defecto busca recursivamente es decir en los directorios que contenga el directorio donde estamos actualmente.
</p>
<p style="text-align: left;">
  Si queremos localizar una frase o texto en especifico (muy común ya que los errores no siempre sabemos en que archivo se encuentran) así:
</p>

\[bash\]\[alevsk@282794-web1 ~\]$ grep "Frase a buscar" DIRECTORIO -Rn[/bash]

<p style="text-align: left;">
  Los parámetros -R y -n son -R para recursividad como explique mas arriba y -n para que nos muestre la linea de coincidencia facilitando aun mas el trabajo.<br/> ![](https://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/vim.jpg)<br/> Ok ya casi lo tenemos solucionado, ya rastreamos y encontramos el mal jeje ahora falta corregirlo, en este punto podemos acceder por ftp y descargar el archivo pero para que si desde la shell lo podemos hacer con [Vim](http://www.vim.org/) :).
</p>
<p style="text-align: left;">
  Para abrir un archivo es muy fácil
</p>

\[bash\]\[alevsk@282794-web1 ~\]$ vim RUTA/RUTA/index.php[/bash]

<p style="text-align: left;">
  por ejemplo, ruta es el árbol de directorios para encontrar el archivo, obviamente si estamos posicionados en el mismo directorio nada mas seria index.php o el archivo que queramos.
</p>
<p style="text-align: left;">
  Al principio vim puede ser confuso e incluso enredoso pero solo es cuestión de encontrarle la belleza a este editor :), para comenzar a editar el archivo presionaremos la letra <strong>i</strong> y nos podemos ir desplazando con las flechas del teclado, después de editar lo que haya que editar pulsamos <strong>ESC</strong> (la tecla escape) para salir del modo de edición, despues de eso para empezar a pasar comandos al editor presionamos <strong>:</strong> (2 puntos), seguido de los parámetros los mas usuales y que yo uso son
</p>
<ul style="text-align: left;">
<li>
    :w < Guardar el archivo
  </li>
<li>
    :w! < Forzar guardado de archivo
  </li>
<li>
    :wq < guardar y salir con confirmación
  </li>
<li>
    :wq! < Guardar y salir sin confirmación, es el mas rápido y el que uso yo después de editar
  </li>
</ul>
<p style="text-align: left;">
  Bueno espero les haya gustado el post, estos son solo algunos tips y trucos que uno va agarrando con la experiencia jeje, pueden investigar mas afondo de [firebug](https://addons.mozilla.org/es-ES/firefox/addon/1843/), [vim](http://www.vim.org/) y [putty](http://www.putty.org/) como herramientas para facilitarse el trabajo.
</p>
---
title: 'Teoria: Local File Inclusion'
author: Alevsk
type: post
date: 2010-11-10T01:00:11+00:00
url: /2010/11/teoria-local-file-inclusion/
categories:
  - Geek
  - Ethical Hacking
  - Programming
  - Technology
  - Tutorials
tags:
  - backtrack
  - debian
  - distros
  - hackers
  - Linux
  - shell
  - slackware
  - software libre
  - Tutorials
  - ubuntu
  - web

---
<p style="text-align: center;">
![Local FIle Inclusion](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/etiquetas.jpg)
</p>

Bueno hace ya bastante rato que no me meto a temas de **seguridad informatica**, mi **laptop** se descompuso y entonces tube que recuperar mis archivos, ahi me encontre unos ejemplo que habia hecho hace ya tiempo sobre un Local File Inclusion, algo asi como un Wargame jeje, y dije bueno aqui no sirve para nada mejor lo subo a un server.

Este articulo va orientado  a los usuarios ++ novatos que recien se inician en la seguridad informatica y el **Hacking etico**.

LFI, **Local File Inclusion** o inclusión local de archivos, es un tipo de vulnerabilidad que se encuentra en paginas mal programadas en lenguaje **PHP**(de hecho el LFile y Rfile inclusion solo afecta al PHP), un usuario malicioso puede utilizar este bug para obtener archivos locales del servidor por ejemplo archivos de conexion a bases de datos, **scrips** PHP privados, el archivos **passwd** (que nunca me ha servido para nada x'D) y en general cosas que no tendria por que obtener.

Comunmente el codigo vulnerable en PHP seria el siguiente

```Tera Term macro
include($_GET['page']);

```

La pagina incluye en si misma el parametro que le hayamos pasado a la variable “page" sin hacer validacion de nada, podiendo de esta manera incluir cualquier archivo que queramos como ya comente mas arriba, por ejemplo:

http://mipaginaweb.com/index.php?pagina=../../../var/log/apache/error.log  
[http://mipaginaweb.com/index.php?pagina=wp-config.php][1]  
http://mipaginaweb.com/index.php?pagina=../../../etc/passwd

Hay varias maneras de solucionar el Local File Inclusion, algunos lo que hacen es agregarle una extencion al parametros que recibe la variable (osea el archivo a incluir)

```Text only
require $_GET['pagina'] . '.inc.php');

```

Al parecer con esto ya quedaria solucionado por que solo se cargarian los **archivos** que tuvieran “.inc.php" en su nombre, sin embargo es posible terminar una cadena añadiendo un caracter nulo **(0×00)** (solo funciona con **magic\_quotes\_gpc** desactivado en un server) de la siguiente manera:

[  
http://mipaginaweb.com/index.php?pagina=../../../etc/passwd%00][2]

Debido al exito no obtenido una de las maneras que nos quedan para evitar el **Local FIle Inclusion** seria aceptar solo ciertos caracteres:

```verilog
if(isset($_GET['pagina']))
{
    $pagina = preg_replace('/[^a-z^A-Z]*/', '', $_GET['pagina']);
    require $_GET['pagina'] '.inc.php';
}
else
{
   die('Nada sucede');
}

```

Ahora esta de mas que decir que para vulnerar un **servidor** es casi imposible hacer uso de una sola tecnica, por ejemplo para hacer un LFile Inclusion satisfactorio primero tendriamos que haber subido una **shell** al servidor por algun **uploader** que tambien fuera vulnerable (esto generalmente se hace por que el uploader solo valida que la extencion del archivo sea .php pero si nos permite subir la shell ya sea en formato .jpg,etc, etc o tambien subir una imagen con codigo php) entonces despues se hace uso del Local File Inclusion que cargara el archivo y leera el codigo php 🙂

Sin embargo hay veces que no es posible subir archivos al servidor por que no tiene **uploader** 🙁 entonces tenemos que hacer uso de la infeccion de archivos particularmente de los **ficheros/archivos** logs de Apache añadiendo alguna **shell, backdoor, exploi**t o que se yo dentro de un archivo legitimo del server que como acabo de decir serian los logs de Apache, pero eso queda para otro post ;D

Y como les prometi al inicio del post aqui esta un ejemplo de Local File Inclusion hecho en **PHP**, chequen los paths que les arroja y el numero de directorios para sacar el archivo passwd 🙂

<div class="demobox">
[![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/demo.png)](http://alevsk.frexa.com.ar/local_file_inclusion/)
</div>

_**Lectura Obligatoria:**_

_La información de este post en especifico asi como los otros que traten sobre hacking, es con fines únicamente de informar y de que el lector aprenda de las amenazas que existen en la red, no es para andar haciendo cosas maliciosas, www.alevsk.com así como el administrador @Alevsk no se responsabiliza del mal uso que se pueda llegar a hacer con estos estudios de hacking ético … nuevamente los exhorto a ver el hacking desde un punto de vista ético, de aprendizaje y mas que nada como una disciplina muy interesante 🙂 Happy hacking_

salu2

PD Disculpen mi mala ortografía no tengo mi laptop ahorita y no tengo el plugin de correccion ortografica de Firefox instalado :p

 [1]: http://mipaginaweb.com/index.php?pagina=wp-config.ph
 [2]: http://mipaginaweb.com/index.php?pagina=../../../etc/passwd%00
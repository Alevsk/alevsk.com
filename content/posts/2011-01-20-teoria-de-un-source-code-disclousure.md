---
title: Teoria de un source code disclousure
author: Alevsk
type: post
date: 2011-01-20T21:23:51+00:00
url: /2011/01/teoria-de-un-source-code-disclousure/
categories:
  - Ethical Hacking
  - Personal
  - Technology
  - Tutorials
tags:
  - backtrack
  - Linux
  - Programming
  - Social Media
  - shell
  - slackware
  - Tutorials
  - web

---
[![](/images/etiquetas.jpg)](http://www.alevsk.com/2011/01/teoria-de-un-source-code-disclousure/etiquetas/)

En un post anterior vimos la teoría que hay detras de un Local File Inclusion, que es una técnica de intrusión que ya casi no se usa hoy en dia, un lector me recomendó hacer un post donde intervenga la parte del upload de la shell (como subir una php shell), buscando entre mis curiosidad encontré un video que hice hace mucho (pero mucho jeje) tiempo y que creo que es un buen ejemplo.

Esta vez he escrito un post sobre seguridad, particularmente seguridad web sobre **http**, donde se explota una vulnerabilidad muy conocida llamada **SCD** (source code disclosure), antes de comenzar aclaro que este tipo de técnicas no requieren grandes conocimientos sobre seguridad informática, tal vez conocimientos básicos de php y de la estructura de directorios, pero no es algo que se tenga que considerar de extrema dificultad, es decir cualquiera podría vulnerar usando este bug de programación.

El SCD es una vulnerabilidad que nos permite ver el código fuente de archivos del servidor por un manejo incorrecto del comando **$GET[]** y **readfile()**, solo basta con ver la estructura de directorios y comenzar a escalar los niveles para leer otros archivos.

### ¿Que cosas importantes podemos obtener?

Los ejemplos mas comunes son leer el archivo **/etc/passwd** que utiliza Linux para la gestión de usuarios (que a mi en lo particular nunca me ha servido para nada), sin embargo yo prefería (tiempo pasado jeje) apuntar a siempre a los archivos de conexion de las bases de datos por ejemplo **wp-config.php** (wordpress), **configuration.php** (joomla), **config.inc.php** de phpmyadmin, por dar solo algunos ejemplos.

Para aprender mas sobre esta vulnerabilidad pueden leer este paper donde abordan a fondo el tema [http://www.secureyes.net/downloads/Source\_Code\_Disclosure\_over\_HTTP.pdf][1]

ya comprendida la naturaleza de la vulnerabilidad pueden checar este codigo que es vulnerable a SCD

```GDScript
$filename = $_GET['file'];

if(ini_get('zlib.output_compression'))
  ini_set('zlib.output_compression', 'Off');

$file_extension = strtolower(substr(strrchr($filename,"."),1));

if( $filename == "" )
{
  echo "ERROR: download file NOT SPECIFIED.";
  exit;
} elseif ( ! file_exists( $filename ) )
{
  echo "ERROR: File not found.";
  exit;
};
switch( $file_extension )
{
  case "pdf": $ctype="application/pdf"; break;
  case "exe": $ctype="application/octet-stream"; break;
  case "zip": $ctype="application/zip"; break;
  case "doc": $ctype="application/msword"; break;
  case "xls": $ctype="application/vnd.ms-excel"; break;
  case "ppt": $ctype="application/vnd.ms-powerpoint"; break;
  case "gif": $ctype="image/gif"; break;
  case "png": $ctype="image/png"; break;
  case "jpeg":
  case "jpg": $ctype="image/jpg"; break;
  default: $ctype="application/force-download";
}
header("Pragma: public");
header("Expires: 0");
header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
header("Cache-Control: private",false); // required for certain browsers
header("Content-Type: $ctype");

header("Content-Disposition: attachment; filename=\"".basename($filename)."\";" );
header("Content-Transfer-Encoding: binary");
header("Content-Length: ".filesize($filename));
readfile("$filename");
exit();

```

Como podemos ver el problema es que los parámetros que le pasan por GET son incluidos sin realizarle una limpieza antes (por decir asi, quitarlo las posibles /.. etc), para corregir ese problema es bastante sencillo, se me ocurre utilizar str_replace para eliminar las / o algo asi.

Bueno este es el video que mencionaba al inicio para que vean la practica.

<p style="text-align: center;">
</p>

 [1]: http://www.secureyes.net/downloads/Source_Code_Disclosure_over_HTTP.pdf
---
title: 'Solución del #CTF CPMX9 de Blog de Alevsk'
author: Alevsk
type: post
date: 2018-06-11T03:10:24+00:00
url: /2018/06/solucion-del-ctf-cpmx9-de-blog-de-alevsk/
categories:
  - Ethical Hacking
  - Linux
  - Mac
  - IT News
  - Talks and Events
  - Programming
  - Technology
  - Tutorials
tags:
  - capture the flag
  - ctf
  - hackers
  - hacking
  - Ethical Hacking
  - Linux
  - Programming

---
[![](/images/campus-party-parepedro.jpg)](http://www.alevsk.com/2018/06/solucion-del-ctf-cpmx9-de-blog-de-alevsk/campus-party-parepedro/)

Hola, como muchos saben, este blog esta registrado como comunidad tecnológica en [Campus Party](https://campuse.ro/events/campus-party-mexico-2018), cada año gente del estado de Michoacán nos organizamos para asistir al evento, jugar, divertirnos, aprender y sobre todo pasar un buen rato 🙂

Ser comunidad de CPMX tiene algunas ventajas por ejemplo obtener códigos de descuento y entradas gratuitas para rifar entre los miembros de la comunidad pero este año realice una dinámica diferente, hace mas o menos 1 semana anuncie en redes sociales (Facebook y Twitter) un pequeño [reto CTF](https://github.com/Alevsk/CTF-CPMX9) en donde poder ganar una entrada no fuera cuestión de suerte. Muchas gracias a todos los que participaron y felicidades a los ganadores.

[![](/images/Screen-Shot-2018-06-10-at-4.16.46-PM.png)](http://www.alevsk.com/2018/06/solucion-del-ctf-cpmx9-de-blog-de-alevsk/screen-shot-2018-06-10-at-4-16-46-pm/)

A continuación dejo la solución de cada uno de los retos por si hay gente que se quedo con dudas 🙂

## 0x01 – 8.8.8.8 or 1.1.1.1?

> A Dan Kaminsky le gusta ( ͡° ͜ ʖ ͡°) www.alevsk.com

Este reto es bastante sencillo si sabes un poco de cultura general de como funciona Internet. 8.8.8.8, 1.1.1.1 y [Dan Kaminsky](https://en.wikipedia.org/wiki/Dan_Kaminsky) son claras referencias al sistema [DNS](https://es.wikipedia.org/wiki/Sistema_de_nombres_de_dominio).

En este tipo de retos es muy común que la información se encuentre escondida en el [record TXT](https://en.wikipedia.org/wiki/TXT_record), pero también existen muchos otros tipos de [DNS records](https://en.wikipedia.org/wiki/List_of_DNS_record_types). Vamos a utilizar la herramienta [nslookup](https://en.wikipedia.org/wiki/Nslookup) y con los siguientes comandos podemos listar los records TXT de cualquier dominio.

```bash
$ nslookup  
> set q=TXT  
> alevsk.com
```

[![](/images/Screen-Shot-2018-06-10-at-4.47.30-PM-1002x800.png)](http://www.alevsk.com/2018/06/solucion-del-ctf-cpmx9-de-blog-de-alevsk/screen-shot-2018-06-10-at-4-47-30-pm/)

La bandera de este reto es: **ctf_flag{3550dd06-aec9-4841-96cb-dbfb093c6991}**

## 0x02 – Cipher

Cipher es probablemente el reto mas complicado de este CTF, las instrucciones del reto nos muestran el siguiente texto cifrado.

> h8s, s, l2e0 4o,h w8orwgx ochg0 h8s,n h8g0g s, r2 he0rsrm .owyx l2e hoyg h8g .4eg 5s44 _ h8g ,h20l grz,n l2e !oyg e5 sr l2e0 .gz orz .g4sg1g !8ohg1g0 l2e !orh h2 .g4sg1gx l2e hoyg h8g 0gz 5s44 _ l2e ,hol sr !2rzg04orz orz s ,82! l2e 82! zgg5 h8g 0o..sh\_824g m2g,x h8g c4om s, whcjc4om{dzz9bk}v\_pbdi\_i}v3\_op33_c3p39d.owvwpu

En la mayoría de los retos básicos de criptografía encontramos dos tipos de cifrados:

  * [Cifrado César (desplazamiento)](https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar)
  * [Cifrado por sustitución](https://es.wikipedia.org/wiki/Cifrado_por_sustituci%C3%B3n)

Podemos intentar resolver esto con alguna herramienta automática como [Rot13 Online](https://www.rot13.com/) o [Caesar Cipher](https://www.dcode.fr/caesar-cipher) pero no hay resultados. No queda otra cosa mas que empezar a hacer un analisis del texto y aplicar distintos ataques criptograficos 🙂

Utilizamos uno de mis lenguajes de programación favoritos, python, para comenzar a recolectar estadísticas interesantes del texto.

Comenzamos separando el texto cifrado por espacios y contando el numero de veces que se repiten las palabras

```python
from collections import Counter  
import re

encrypted = "h8s, s, l2e0 4o,h w8orwgx ochg0 h8s,n h8g0g s, r2 he0rsrm .owyx l2e hoyg h8g .4eg 5s44 _ h8g ,h20l grz,n l2e !oyg e5 sr l2e0 .gz orz .g4sg1g !8ohg1g0 l2e !orh h2 .g4sg1gx l2e hoyg h8g 0gz 5s44 _ l2e ,hol sr !2rzg04orz orz s ,82! l2e 82! zgg5 h8g 0o..sh\_824g m2g,x h8g c4om s, whcjc4om{dzz9bk}v\_pbdi\_i}v3\_op33_c3p39d.owvwpu"

words = encrypted.split()  
word_counts = Counter(words)  
print(word_counts)
```

```code
{  
'l2e': 6,  
'h8g': 5,  
's,': 3,  
'5s44': 2,  
'orz': 2,  
'hoyg': 2,  
'_': 2,  
'l2e0': 2,  
'sr': 2,  
'zgg5': 1,  
'grz,n': 1,  
'!orh': 1,  
'whcjc4om{dzz9bk}v\_pbdi\_i}v3\_op33\_c3p39d.owvwpu': 1,  
'0o..sh_824g': 1,  
',h20l': 1,  
'!8ohg1g0': 1,  
',hol': 1,  
'.owyx': 1,  
'h8s,': 1,  
'4o,h': 1,  
'h8s,n': 1,  
'!2rzg04orz': 1,  
'.4eg': 1,  
'c4om': 1,  
',82!': 1,  
'.g4sg1g': 1,  
'e5': 1,  
'w8orwgx': 1,  
'0gz': 1,  
'r2': 1,  
'he0rsrm': 1,  
'.g4sg1gx': 1,  
'82!': 1,  
'h8g0g': 1,  
'h2': 1,  
'm2g,x': 1,  
's': 1,  
'!oyg': 1,  
'ochg0': 1,  
'.gz': 1  
}
```

La palabra que se repite mas veces es **l2e** (6 veces), pero también vemos **l2e0** (2 veces) que es una variación de la palabra anterior, algo similar ocurre con **h8g** y **h8g0g** y algunas otras más.

La complejidad de este reto disminuye notoriamente ya que sabemos lo que estamos buscando en el texto, la bandera 🙂 y sabemos cual es el formato que deben seguir las mismas.

> ctf_flag{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}

En una cadena de texto lo suficientemente larga debemos encontrar un símbolo que se repita siguiendo el mismo patrón que el de la bandera si no estuviera encriptada, es decir:

> * = (simbolo de guion)
> 
> (8 simbolos)\*(4 simbolos)\*(4 simbolos)\*(4 simbolos)\*(12 simbolos)

La palabra mas larga que arrojo nuestro análisis es **whcjc4om{dzz9bk}v\_pbdi\_i}v3\_op33\_c3p39d.owvwpu**, probamos “alineando" el formato de la bandera en esa palabra para ver si cumple con el patrón:

```bash
whcjc4om{dzz9bk}v\_pbdi\_i}v3\_op33\_c3p39d.owvwpu  
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

Tenemos una coincidencia 🙂 acomodamos el resto de la bandera y comenzamos a crear un diccionario con los caracteres a sustituir en el texto y podremos empezar a romper el cifrado (encontrar el alfabeto que fue usado para la sustitución)

```bash
whcjc4om{dzz9bk}v\_pbdi\_i}v3\_op33\_c3p39d.owvwpu  
ctf_flag{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}
```

Agregamos el diccionario a nuestro script y hacemos la sustitución.

```python
encrypted = "h8s, s, l2e0 4o,h w8orwgx ochg0 h8s,n h8g0g s, r2 he0rsrm .owyx l2e hoyg h8g .4eg 5s44 _ h8g ,h20l grz,n l2e !oyg e5 sr l2e0 .gz orz .g4sg1g !8ohg1g0 l2e !orh h2 .g4sg1gx l2e hoyg h8g 0gz 5s44 _ l2e ,hol sr !2rzg04orz orz s ,82! l2e 82! zgg5 h8g 0o..sh\_824g m2g,x h8g c4om s, whcjc4om{dzz9bk}v\_pbdi\_i}v3\_op33_c3p39d.owvwpu"  
decrypted = ""  
replace = {  
'w': 'c',  
'h': 't',  
'c': 'f',  
'j': '_',  
'4': 'l',  
'o': 'a',  
'm': 'g',  
'_': '-',  
'u': '}'  
}

for c in encrypted:  
if c in replace:  
decrypted += replace[c]  
else:  
decrypted += c

print(decrypted)
```

Vemos que la palabra flag se encuentra en otras partes del texto y no solo en la bandera, lo que sugiere que el texto esta escrito en ingles

> t8s, s, l2e0 la,t c8arcgx aftg0 t8s,n t8g0g s, r2 te0rsrg .acyx l2e tayg t8g .leg 5sll – t8g ,t20l grz,n l2e !ayg e5 sr l2e0 .gz arz .glsg1g !8atg1g0 l2e !art t2 .glsg1gx l2e tayg t8g 0gz 5sll – l2e ,tal sr !2rzg0larz arz s ,82! l2e 82! zgg5 t8g 0a..st-82lg g2g,x t8g flag s, ctf_flag{dzz9bk}v-pbdi-i}v3-ap33-f3p39d.acvcp}

Todavía tenemos otras 2 palabras, **l2e** y **h8g**, que se repiten bastante en el texto, si encontramos cual es su equivalente nuestro texto sera todavía mas legible. Investigando un poco encontré un articulo bastante interesante [The Most Common Three Letter Words](http://grammar.yourdictionary.com/word-lists/common-three-letter-words.html) (Las palabras mas comunes de 3 letras)

Hacia al final del texto podemos leer algo que dice:

> t8g flag s, ctf_flag{dzz9bk}v-pbdi-i}v3-ap33-f3p39d.acvcp}

si **t8g** puede ser **the** (que se encuentra en la lista de palabras populares) y **s,** es **is** la frase final seria

> the flag is ctf_flag{dzz9bk}v-pbdi-i}v3-ap33-f3p39d.acvcp}

Parece que nos vamos acercando, probamos agregando estas letras a nuestro diccionario.

```bash
replace = {  
'w': 'c',  
'h': 't',  
'c': 'f',  
'j': '_',  
'4': 'l',  
'o': 'a',  
'm': 'g',  
'_': '-',  
'u': '}',  
'8': 'h',  
'g': 'e',  
's': 'i',  
',': 's',  
}
```

> this is l2e0 last charcex afte0 thisn the0e is r2 te0rirg .acyx l2e taye the .lee 5ill – the st20l erzsn l2e !aye e5 ir l2e0 .ez arz .elie1e !hate1e0 l2e !art t2 .elie1ex l2e taye the 0ez 5ill – l2e stal ir !2rze0larz arz i sh2! l2e h2! zee5 the 0a..it-h2le g2esx the flag is ctf_flag{dzz9bk}v-pbdi-i}v3-ap33-f3p39d.acvcp}

Mas palabras salen a la luz:

afte**** … **** es r

**l2e0** se vuelve **l2er**, por lo tanto en la frase **this is l2er last charcex**, l2er es remplazado por **your** y el texto tiene aun mas sentido 🙂 !!!

cha**r**ce … r es n (chance)

> this is your last chancex after thisn there is no turning

Tenemos suficiente texto legible para realizar una búsqueda en google y darnos cuenta que el texto es una frase famosa de la película [The Matrix](https://en.wikipedia.org/wiki/The_Matrix)
[![](/images/Screen-Shot-2018-06-10-at-9.00.04-PM-1200x666.png)](http://www.alevsk.com/2018/06/solucion-del-ctf-cpmx9-de-blog-de-alevsk/screen-shot-2018-06-10-at-9-00-04-pm/)

Completamos el resto del diccionario con las letras que nos hacen falta.

[![](/images/Screen-Shot-2018-06-10-at-9.13.01-PM-1085x800.png)](http://www.alevsk.com/2018/06/solucion-del-ctf-cpmx9-de-blog-de-alevsk/screen-shot-2018-06-10-at-9-13-01-pm/)

> Nota: en este punto de la solución me di cuenta que cometí un error al momento de diseñar el reto y no se puede avanzar mas, gracias a [@unmanarc](https://twitter.com/unmanarc) por reportar el problema

Por lo tanto la bandera de este reto es **ctf_flag{ddd9bk}v-pbdi-i}v3-ap33-f3p39dbacvcp}**

## 0x03 – A new security policy standard

> Si encuentras una vulnerabilidad en www.alevsk.com deberías reportarla utilizando los canales adecuados 🙂

Tanto el nombre del reto como la descripción nos da una pista acerca de que debemos investigar sobre nuevos estándares en políticas de seguridad, algunas personas se confundieron en este reto pues creían que tenían que encontrar vulnerabilidades en esta pagina, pero la solución es mas sencilla que eso.

[security.txt](https://securitytxt.org/) es un estándar propuesto (similar a robots.txt) para que los sitios web puedan anunciar sus políticas de seguridad y consiste en publicar un archivo de texto en el directorio **.well-known** donde comuniquemos información importante como por ejemplo la direccion de contacto en la que los hackers pueden reportar las vulnerabilidades encontradas de nuestro sitio web, en este caso [https://www.alevsk.com/.well-known/security.txt](https://www.alevsk.com/.well-known/security.txt)

```bash
# If you would like to report a security issue  
# you may report it to me on www.alevsk.com  
# ctf_flag{1999251d-df25-4d4a-846b-d4267f471b23}  
Contact: lenin@alevsk.com  
Encryption: https://pgp.mit.edu/pks/lookup?op=get&search=0xFF4F600D674B6DED
```

La bandera de este reto es: **ctf_flag{1999251d-df25-4d4a-846b-d4267f471b23}**

## 0x04 – Foogle

> Neo: Why do my eyes hurt? Morpheus: You've never used them before.
> 
> [Descargar imagen](https://www.dropbox.com/s/4j5kf0o4k0wryff/foogle.png?dl=0)

Este reto involucra [esteganografía](https://es.wikipedia.org/wiki/Esteganograf%C3%ADa) y es muy fácil de resolver, descargamos la imagen que nos indican las instrucciones y comenzamos a realizar el análisis, lo mas sencillo y lo primero que intentamos es ver si la imagen contiene en sus bytes alguna cadena de caracteres que tenga sentido.

Podemos utilizar la herramienta [hexdump](https://en.wikipedia.org/wiki/Hex_dump) para hacer esto.

```bash
$ hexdump -C foogle.png

00000000 89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 |.PNG……..IHDR|  
00000010 00 00 04 34 00 00 02 60 08 06 00 00 00 75 21 33 |…4…\`…..u!3|  
00000020 a1 00 00 01 7c 69 43 43 50 49 43 43 20 50 72 6f |….|iCCPICC Pro|  
00000030 66 69 6c 65 00 00 28 91 63 60 60 2a 49 2c 28 c8 |file..(.c“*I,(.|  
….  
….  
….  
000be000 7b 3a e3 0d e3 7e e2 66 21 44 35 e4 e6 ce 49 93 |{:…~.f!D5…I.|  
000be010 6e 35 05 78 c2 39 98 9c ae db e4 fd 69 9f 8b 31 |n5.x.9……i..1|  
000be020 94 4e ca e5 4d c1 c5 ba 13 c0 eb 99 ff 07 7b ee |.N..M………{.|  
000be030 41 67 d0 72 4a 54 00 00 00 00 49 45 4e 44 ae 42 |Ag.rJT….IEND.B|  
000be040 60 82 59 33 52 6d 58 32 5a 73 59 57 64 37 59 6a |\`.Y3RmX2ZsYWd7Yj|  
000be050 4d 77 4f 57 55 77 4e 57 4d 74 5a 6a 49 79 4e 43 |MwOWUwNWMtZjIyNC|  
000be060 30 30 4e 44 4d 33 4c 57 46 6a 5a 44 6b 74 59 57 |00NDM3LWFjZDktYW|  
000be070 52 68 5a 54 6b 35 4e 6a 45 30 4d 6d 56 6b 66 51 |RhZTk5NjE0MmVkfQ|  
000be080 3d 3d |==|  
000be082
```

También podemos utilizar el comando **strings**.

```bash
$ strings foogle.png
```

[![](/images/Screen-Shot-2018-06-10-at-5.30.17-PM-1007x800.png)](http://www.alevsk.com/2018/06/solucion-del-ctf-cpmx9-de-blog-de-alevsk/screen-shot-2018-06-10-at-5-30-17-pm/)

Al final del archivo hay una cadena de caracteres muy peculiar, parece que es un mensaje codificado en [base64](https://es.wikipedia.org/wiki/Base64), tomamos el string y lo decodificamos con alguna herramienta como [https://www.base64decode.org/](https://www.base64decode.org/)
[![](/images/Screen-Shot-2018-06-10-at-5.34.21-PM-937x800.png)](http://www.alevsk.com/2018/06/solucion-del-ctf-cpmx9-de-blog-de-alevsk/screen-shot-2018-06-10-at-5-34-21-pm/)

La bandera de este reto es **ctf_flag{b309e05c-f224-4437-acd9-adae996142ed}**

## 0x05 – Information leak

> Información critica ha sido leakeada en los archivos de este repositorio x.x

Como la descripción nos indica, tenemos que revisar los archivos del repositorio donde esta hospedado el [CTF](https://github.com/Alevsk/CTF-CPMX9/), y no solo eso, tambien tenemos que revisar el historial de commits, vemos que en uno de los [commits](https://github.com/Alevsk/CTF-CPMX9/commit/81558f380a18fdb3f6f08d376fb82b128929d41f) un archivo llamado **0x05_secret.txt** fue publicado en el repositorio.

[![](/images/Screen-Shot-2018-06-10-at-5.51.41-PM-1200x299.png)](http://www.alevsk.com/2018/06/solucion-del-ctf-cpmx9-de-blog-de-alevsk/screen-shot-2018-06-10-at-5-51-41-pm/)

La bandera de este reto es **ctf_flag{163f0835-8fc0-4fd0-b96b-dcd724cbe200}**

## 0x06 – We can fix it!

> Otro participante trato de robar la bandera de este reto pero sin querer la daño, ¿Puedes repararla? [Descargar imagen](https://www.dropbox.com/s/o9dq5udc6t3dchf/qr_code.png?dl=0)

Este reto nos presentaba un [codigo QR](https://es.wikipedia.org/wiki/C%C3%B3digo_QR) “dañado" (los bordes de la imagen han sido recortados), por lo que si tratamos de leerlo nos dará un error

[![](/images/qr_code.png)](http://www.alevsk.com/2018/06/solucion-del-ctf-cpmx9-de-blog-de-alevsk/qr_code/)

Pero nada que un poco de photoshop no pueda arreglar 🙂

[![](/images/good_frame.png)](http://www.alevsk.com/2018/06/solucion-del-ctf-cpmx9-de-blog-de-alevsk/good_frame/)

La bandera de este reto es **ctf_flag{d55bd4f6-bff1-45b4-836e-7df1839e7d70}**

Espero se hayan divertido mucho y aprendido algo nuevo al participar en este reto.

Happy hacking 🙂
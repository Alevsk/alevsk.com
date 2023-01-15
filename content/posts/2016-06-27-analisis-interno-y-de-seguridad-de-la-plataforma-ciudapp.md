---
title: 'Análisis interno y de seguridad de la plataforma #CiudApp'
author: Alevsk
type: post
date: 2016-06-27T15:44:00+00:00
url: /2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/
categories:
  - Android
  - Ethical Hacking
  - Linux
  - Personal
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - android
  - app
  - Government
  - hackers
  - Linux
  - Personal
  - Programming
  - Social Media
  - reversing
  - Solutions
  - Technology
  - Tutorials

---
[![26757261694_a0273fdcb6_z](/images/26757261694_a0273fdcb6_z.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/26757261694_a0273fdcb6_z/)

El 30 de mayo de este año (2016) Enrique Alfaro, presidente de Guadalajara, anunció durante la sesión de Campus Night la nueva aplicación de administración y gestión de información relevante para los ciudadanía: **CiudApp**.

Entre muchas otras cosas, la aplicación permite a los ciudadanos estar informados de las noticias más relevantes de la administración (por eso del trending de los gobiernos abiertos), realizar reportes incluyendo geolocalización y solicitar o proponer servicios al gobierno. 

A raíz del lanzamiento de la aplicación ha surgido bastante debate y comentarios en Internet en torno a la misma, incluso leí un artículo muy interesante en donde le hacían un [análisis de usabilidad](https://medium.com/ux-ui-design/an%C3%A1lisis-heur%C3%ADstico-de-usabilidad-en-ciudapp-c847b6f5d264#.zab2arhcn) a la aplicación, pienso que está bien ya que en nuestro querido México, en el pasado hemos tenido casos polémicos como el de [la app de los 115 millones de pesos](http://www.proceso.com.mx/336107/diputados-pagaran-115-millones-por-una-app-que-se-cotiza-en-500-mil-pesos) y es natural que la gente que sabe del tema (desarrolladores, ux designers, community managers, etc.) emitan su opinión acerca de un producto tecnológico “generado" por el gobierno.

Regresando a lo anterior, después de leer el análisis heurístico de usabilidad de la aplicación me pregunte a mí mismo ¿Quién está detrás del desarrollo de la aplicación?, ¿Y si le hacemos un análisis interno a la app? Podemos hacer algunas pruebas de seguridad también, vamos a “destripar" la aplicación para entender como está construida y ver cómo fue desarrollada, todo esto con la premisa de que no vamos a romper ni a explotar / vulnerar / hackear nada 🙂 y pues manos a la obra.

## Instalando la aplicación en genymotion

Lo primero que vamos a hacer es descargar el apk de la aplicación (Si, el análisis lo vamos a hacer sobre un dispositivo con Android), el link de la app CiudApp en la playstore es [https://play.google.com/store/apps/details?id=com.radmas.iyc.guadalajara.mex](https://play.google.com/store/apps/details?id=com.radmas.iyc.guadalajara.mex) y hay miles de sitios web que te permiten descargar el apk utilizando la url de la tienda, solo busquen algún en google y descarguen el archivo, cuando hayan terminado tendrán un archivo llamado más o menos así **Ciudapp\_Guadalajara\_v3.0.146_apkpure.com.apk**.

Después de eso vamos a instalar la aplicación en genymotion, si no saben lo que es pueden investigar y descargarlo de acá [https://www.genymotion.com/](https://www.genymotion.com/) y probablemente escriba un tutorial en el futuro acerca de cómo instalarlo y configurarlo.

[![android](/images/android.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/android/)

Ejecutamos nuestro dispositivo virtual de con Android y vamos a proceder a instalar el **apk de la aplicacion** mediante **adb** con el comando:

```bash  
adb install Ciudapp\_Guadalajara\_v3.0.146_apkpure.com.apk  
```

[![adb](/images/adb.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/adb/)

Una vez termine el proceso de instalación tendremos la app en nuestro dispositivo virtual.

[![installed](/images/installed.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/installed/)

Bueno, ya tenemos la aplicación preparada, vamos a dejar esto por un momento y vamos a regresar a la carpeta en donde descargamos nuestra apk, ahora vamos a utilizar 3 herramientas, apktool, dex2jar y Jd (Jar Decompiler) para entender un poco más como está construida la app.

## Obteniendo los assets de la aplicación

Vamos a utilizar apktool para de compilar la app y leer así algunos archivos importantes como el AndroidManifest.xml, strings.xml y cualquier otro archivo que nos pueda decir algo acerca de la app o sus desarrolladores.

```bash  
apktool.bat d "C:\Users\Alevskey\Documents\Pentest\mobile\ciudapp\Ciudapp Guadalajara\_v3.0.146\_apkpure.com.apk"
```

[![d](/images/d.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/d/)
[![apktool_d_folder](/images/apktool_d_folder.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/apktool_d_folder/)

Entre los permisos que nos solicita la aplicación tenemos cosas típicas como acceso a la cámara, acceso al GPS, escribir y leer en almacenamiento externo, acceso a internet, etc., permisos que uno esperaría de una aplicación como esta.

```xml
<manifest package="com.radmas.iyc.guadalajara.mex" platformbuildversioncode="23" platformbuildversionname="6.0-2166767" xmlns:android="http://schemas.android.com/apk/res/android">
<uses-permission android:name="android.permission.WRITE\_EXTERNAL\_STORAGE"></uses-permission>
<uses-permission android:name="android.permission.READ\_EXTERNAL\_STORAGE"></uses-permission>
<uses-permission android:name="android.permission.INTERNET"></uses-permission>
<uses-permission android:name="com.google.android.providers.gsf.permission.READ_GSERVICES"></uses-permission>
<uses-permission android:name="android.permission.ACCESS\_COARSE\_LOCATION"></uses-permission>
<uses-permission android:name="android.permission.ACCESS\_FINE\_LOCATION"></uses-permission>
<uses-permission android:name="android.permission.ACCESS\_NETWORK\_STATE"></uses-permission>
<uses-permission android:name="android.permission.CAMERA"></uses-permission>
<permission android:name="com.radmas.iyc.guadalajara.mex.permission.MAPS_RECEIVE" android:protectionlevel="signature"></permission>
<uses-permission android:name="com.radmas.iyc.guadalajara.mex.permission.MAPS_RECEIVE"></uses-permission>
<uses-feature android:glesversion="0x20000" android:required="true"></uses-feature>
<permission android:name="com.radmas.iyc.guadalajara.mex.permission.C2D_MESSAGE" android:protectionlevel="signature"></permission>
<uses-permission android:name="com.radmas.iyc.guadalajara.mex.permission.C2D_MESSAGE"></uses-permission>
<uses-permission android:name="com.google.android.c2dm.permission.RECEIVE"></uses-permission>
<uses-permission android:name="android.permission.WAKE_LOCK"></uses-permission>
<uses-permission android:name="com.radmas.iyc.guadalajara.mex.permission.GPSTRACKER"></uses-permission> //Show custom dialgo above Statusbar  
<uses-permission android:name="android.permission.SYSTEM\_OVERLAY\_WINDOW"></uses-permission>
```

Lo que me llamo la atención desde un inicio, y una de las razones por las que quería hacer este ejercicio, fue encontrar que empresa fue la desarrolladora de la app, revisando más a fondo el archivo vemos que muchos de los packages empiezan con **com.radmas.iyc.guadalajara.mex**, haciendo una búsqueda en google de [radmas.com](http://radmas.com/) encontramos lo que parece ser una agencia española (pueden revisar su información en [who.is](https://who.is/)) de desarrollo de software especializada en diseño, marketing, creación de aplicaciones móviles y páginas web.

[![radmas](/images/radmas.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/radmas/)

Si son desarrolladores de Android pueden identificar rápidamente otras cosas interesantes como los activities de la aplicación, uno que otro broadcast receiver, algunos servicios, intents, public api keys, etc.

También me llamo la atención que la aplicación tiene internacionalización, aunque la app parece un poco genérica, está bien hecha en ese aspecto

[![idiomas](/images/idiomas.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/idiomas/)

Con la utilidad **File Locator Lite** también encontramos algunos archivos interesantes como:

app.json

```xml
{  
"server_url":"https://api.mejoratuciudad.org",  
"base_uri":"",  
"jurisdiction_id":"mx.guadalajara",  
"api_key":"12",  
"name":"Ciudapp Guadalajara",  
"promo_text": "Echa un vistazo a 'Ciudapp Guadalajara', la mejor aplicación móvil de atención ciudadana https://play.google.com/store/apps/details?id=com.radmas.iyc.guadalajara.mex",  
"promo_web": "https://play.google.com/store/apps/details?id=com.radmas.iyc.guadalajara.mex",  
"email": "info@mejoratuciudad.org",  
"languages": [{"key":"Español","value":"es"},  
{"key":"Inglés","value":"en"}],  
"share_url": "http://intranet.mejoratuciudad.org/mail/request/"  
}
```

arrays.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string-array name="enviroments">
<item>http://api-canary.mejoratuciudad.org</item>
<item>http://api-developer.mejoratuciudad.org</item>
<item>http://api.mejoratuciudad.org</item>
<item>http://open010.valvaro.lan</item>
<item>http://open010.vivan.lan</item>
<item>http://open010.vnacho.lan</item>
<item>http://open010.vfernando.lan</item>
<item>http://open010.vwalter.lan</item>
<item>http://open010.vemilio.lan</item>
</string-array>
</resources>
```

De acuerdo a lo que vemos la app se comunica con varios servicios web hospedados en [mejoratuciudad.org](http://www.mejoratuciudad.org/), investigando un poco sabemos que la empresa anterior mencionada (**radmas.com**) también es dueña de este producto, y según sus propias palabras:

> Mejora Tu Ciudad (MTC) es una plataforma de comunicación entre los ciudadanos y el ayuntamiento, que se enmarca dentro de las soluciones Smart City y que se basa en los tres pilares fundamentales de Open Government:
> 
> Participación, colaboración y transparencia

Al menos con esto estoy un poco más tranquilo sabiendo que el gobierno de Guadalajara contrato una empresa especializada para el desarrollo de la aplicación y no a un par de becarios para programar la app XD.

[![mejoratuciudad](/images/mejoratuciudad.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/mejoratuciudad/)



## Del DEX al JAR y del JAR al código fuente

Antes de avanzar al siguiente paso hay algo más que podemos hacer, es sabido que los **archivos apk**, son en realidad **archivos rar**, entnces tomamos nuestro **Ciudapp Guadalajara\_v3.0.146\_apkpure.com.apk** lo renombramos a **Ciudapp Guadalajara\_v3.0.146\_apkpure.com.rar** y lo descomprimimos obteniendo algo como lo siguiente:

[![dex2jar](/images/dex2jar.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/dex2jar/)

El contenido de la carpeta es muy parecido a lo que generamos cuando utilizamos apktool sin embargo si tratan de abrir algún **archivo xml** aquí, como por ejemplo el **AndroidManifest.xml** lo unico que obtendrán serán 0s y 1s, pero tenemos algo interesante, el archivo **classes.dex**.

Podemos utilizar [dex2jar](https://sourceforge.net/projects/dex2jar/) con el siguiente comando para generar un archivo jar (Javar Archive)

```bash
dex2jar.bat "C:\Users\Alevskey\Documents\Pentest\mobile\ciudapp\Ciudapp Guadalajara\_v3.0.146\_apkpure.com\classes.dex"
```

Obtendremos un archivo **classes_dex2jar.jar** que podemos abrir en el Java decompiler, tan solo abrimos la aplicación y seleccionamos el archivo jar.

[![jd](/images/jd.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/jd/)

Muchos de los paquetes que vemos ahí son librerías de terceros y conforme indagamos más y más podemos ver que la aplicación utiliza librerías de facebook, google, librerías para animaciones, reyclerviews personalizados, analytics, Bitly, crash analytics, etc.

[![jd2](/images/jd2.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/jd2/)

Para agilizar la búsqueda podemos seleccionar **File > Save All Sources** y elegimos una carpeta en donde guardaremos el archivo Zip generado que después descomprimimos y analizamos, nuevamente utilizando **File Locator Lite**

[![app_decompiled](/images/app_decompiled.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/app_decompiled/)

Algunas búsquedas nos arrojan cosas interesantes, como por ejemplo credenciales en texto plano XD

[![password](/images/password-1.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/password-2/)
[![passwords2](/images/passwords2.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/passwords2/)
[![username](/images/username.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/username/)

Con las credenciales obtenidas fue posible acceder a lo que parece un portal administrativo de estacionamientos de una tercer empresa llamada [urbiotica](http://www.urbiotica.com/) en [http://services.urbiotica.net/](http://services.urbiotica.net/)
[![urbiotica](/images/urbiotica.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/urbiotica/)

Podemos ver, al parecer, en tiempo real el status de los cajones de un estacionamiento en algún lugar de España, la pregunta aquí es: ¿Que hacían esas credenciales hardcodeadas en la app?, navegando la aplicación no veo por ningún lado algo que haga referencia a estacionamientos sin embargo haciendo otra búsqueda con la palabra **park** obtenemos referencias en muchos otros archivos.

[![park](/images/park.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/park/)

Sin embargo no pude lanzar ningún activity o servicio relacionado al **Parking** desde **adb shell** ya que no estaban registradas en el **AndroidManifest.xml**.

Opino que esas credenciales son quizás de algún desarrollo anterior, el código fuente fue re utilizado y las credenciales fueron olvidadas ahí y ahora están siendo distribuidas masivamente XD, en fin la pantalla administrativa del sistema de estacionamientos luce de esta forma, tiene sentido que haya otra empresa más involucrada en este proyecto, sobre todo si es está enfocada en tecnologías para Smart cities.

[![park2](/images/park2.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/park2/)

## Revisando los archivos de la aplicación

Regresamos a nuestro emulador y ahora vamos a abrir una shell de windows y ejecutamos el comando:

```bash
adb shell
```

El comando anterior nos entregara una consola para poder navegar el dispositivo donde instalamos la app, conociendo un poco sobre Internals y arquitectura general de Android sabemos que la información de una app se almacena en la ruta **/data/data/package.de.la.app**, en este caso **/data/data/com.radmas.iyc.guadalajara.mex/**

[![shared_pref](/images/shared_pref.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/shared_pref/)

Aquí encontramos otros archivos que podrían contener más cosas interesantes y que a su vez nos podrían enseñar un poco más cómo funciona la aplicación, comenzamos por ver que hay dentro de la carpeta **shared_prefs**, si no saben lo que es pueden investigar más al respecto acá [https://developer.android.com/training/basics/data-storage/shared-preferences.html](https://developer.android.com/training/basics/data-storage/shared-preferences.html) pero en resumen es un método de almacenamiento persistente que nos ofrece el sistema operativo, la información es almacenada en archivos XML y es generalmente utilizado para guardar configuraciones de la aplicación.

[![shared_prefs2](/images/shared_prefs2.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/shared_prefs2/)

Quizás el archivo más interesante es **JURISDICTION_LOADED.xml** que contiene:

```xml
<?xml version='1.0′ encoding='utf-8′ standalone='yes' ?>
<map>
<string name="mx.guadalajara">mx.guadalajara</string>
</map>
```

Y del cual vamos a hablar en la siguiente etapa. Después de que se loguen en la app pueden ver que nuevos archivos de preferencias compartidas son creados, estos contienen información relacionada con su cuenta, facebook, etc, etc.

[![shared_prefs3](/images/shared_prefs3.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/shared_prefs3/)

En la carpeta **/data/data/com.radmas.iyc.guadalajara.mex/databases/** encontramos dos **bases de datos sqlite**, procedemos a descargarlas para ver qué es lo que contienen usando los siguientes comandos.

```bash
adb pull /data/data/com.radmas.iyc.guadalajara.mex/databases/DBImproveYourCity C:\Users\Alevskey\Documents\Pentest\mobile\ciudapp\databases

adb pull /data/data/com.radmas.iyc.guadalajara.mex/databases/DBImproveYourCity-journal C:\Users\Alevskey\Documents\Pentest\mobile\ciudapp\databases
```

Y después podemos abrirlas utilizando cualquier visor de sqlite como por ejemplo [SQLiteBrowser](http://sqlitebrowser.org/), tutorial para [descargar e instalar](https://www.guru99.com/download-install-sqlite.html)
[![db2](/images/db2.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/db2/)

En la tabla request es donde podemos ver los reportes “cacheados" por la aplicación en nuestro teléfono, podemos observar el id del reporte (service\_request\_id), el id de la cuenta de la persona que hizo el reporte (account_id), la calle, coordenadas, url de imagenes, descripcion, status, fecha, etc.

[![db4](/images/db4.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/db4/)
[![db5](/images/db5.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/db5/)
[![db6](/images/db6.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/db6/)

En general cumplen con las buenas prácticas de almacenamiento de información, no almacenan datos sensible en lugares inseguros como la SD externa y en su lugar lo hacen en bases de datos **SQLite** y **shared preferences** que es donde solo la aplicación tiene privilegios de lectura y escritura.

## Entendiendo las comunicaciones

Ahora viene una de las partes más divertidas de este tipo de ejercicios, saber cómo y con quien se comunica la aplicación, que es lo que envía y que es lo que recibe, etc. Pero antes, si están haciendo este ejercicio mientras leen mi artículo se darán cuenta que la app maneja un concepto muy interesante llamado **Jurisdicciones** o **Jurisdiction**, después de analizar el código fuente y visualizar en mi mente el flujo de información, jurisdiction es un identificador que le dice a la app que información cargar de acuerdo a una región especifica, por default la app al iniciar hace un request a [https://api.mejoratuciudad.org/applications/12.json](https://api.mejoratuciudad.org/applications/12.json) y obtiene como resultado

```xml
{  
"name": "Guadalajara",  
"active": true,  
"default\_jurisdiction\_id": "mx.guadalajara"  
}
```

Pueden jugar con el numero al final de la url y de esta manera nos damos cuenta que esta aplicación (o al menos el backend y los servicios web) son escalables y han sido implementados en muchas otras ciudades y países (¿Posiblemente otros clientes de radmas?), por ejemplo [https://api.mejoratuciudad.org/applications/5.json](https://api.mejoratuciudad.org/applications/5.json) nos arroja:

```xml
{  
"name": "Cuenta conmigo",  
"active": true,  
"default\_jurisdiction\_id": "org.sevilla"  
}
```  
[https://api.mejoratuciudad.org/applications/4.json](https://api.mejoratuciudad.org/applications/4.json)  
```xml
{  
"name": "Greencities",  
"active": true,  
"default\_jurisdiction\_id": "eu.greencities.malaga"  
}
```

Revisando rápidamente con una herramienta para automatizar el proceso podemos ver que actualmente existen 16 jurisdicciones diferentes (al menos en ese servidor), podemos encontrar muchísimas ciudades más del estado de Jalisco así como ciudades de otros países, eso nos dice que la aplicación está siendo implementada en muchos más lugares 🙂

[![burp](/images/burp.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/burp/)

El mismo ID de jurisdicción es utilizado para obtener las noticias, reportes y servicios relacionados de una región en específico.

Continuamos, como sabemos la aplicación se comunica con servicios web hospedados con el proveedor **[https://api.mejoratuciudad.org/](https://api.mejoratuciudad.org/)**, si vamos a esa URL podremos ver una bonita api REST muy bien documentada 🙂

[![rest](/images/rest.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/rest/)

Esto es muy bueno ya que los desarrolladores ya no estamos limitados a solo utilizar la aplicación, ahora podemos crear nuestras propias aplicaciones utilizando la api ya existente :)! hay otros servicios web muy interesantes como:

  * [https://api.mejoratuciudad.org/news.json?jurisdiction_id=mx.guadalajara](https://api.mejoratuciudad.org/news.json?jurisdiction_id=mx.guadalajara): Nos trae una lista de noticias
  * [https://api.mejoratuciudad.org/services.json?jurisdiction_id=mx.guadalajara](https://api.mejoratuciudad.org/services.json?jurisdiction_id=mx.guadalajara): Nos trae una lista de servicios
  * [https://api.mejoratuciudad.org/alerts.json?jurisdiction_id=mx.guadalajara](https://api.mejoratuciudad.org/alerts.json?jurisdiction_id=mx.guadalajara): Nos trae una lista de alertas

Como mencionaba anteriormente, tal solo cambien el valor de la jurisdicción por alguno de los otros y obtendrán la información de las otras plataformas. Para obtener un poco mas de información general de la aplicación, ejecutamos fierce sobre **mejoratuciudad.org** para tratar de obtener una lista de posibles subdominios

```bash
fierce -dns mejoratuciudad.org -wordlist /root/tools/SecLists/Discovery/DNS/subdomains-top1mil-110000.txt -threads 10
```

[![fierce](/images/fierce.jpg)](http://www.alevsk.com/2016/06/analisis-interno-y-de-seguridad-de-la-plataforma-ciudapp/fierce/)

La lista completa: 

> ftp.mejoratuciudad.org  
> www.mejoratuciudad.org  
> intranet.mejoratuciudad.org  
> api.mejoratuciudad.org  
> m.mejoratuciudad.org  
> apps.mejoratuciudad.org  
> blog.mejoratuciudad.org  
> demo.mejoratuciudad.org  
> lab.mejoratuciudad.org  
> doc.mejoratuciudad.org  
> developer.mejoratuciudad.org  
> pandora.mejoratuciudad.org  
> hera.mejoratuciudad.org  
> WWW.mejoratuciudad.org  
> landing.mejoratuciudad.org  
> privacy.mejoratuciudad.org  
> electra.mejoratuciudad.org  
> pi-canary.mejoratuciudad.org  
> api-developer.mejoratuciudad.org

En este punto el servidor me dio ban (probablemente por mis peticiones automatizadas, pero nada que no se solucione con una VPN), y ya no continué haciendo más pruebas, pero no sin antes darme cuenta de que al parecer su servidor no está hardenizado, cualquier petición a su api devolvía un error 403 revelando la versión del servidor web y su sistema operativo.

```xml
<html>
<head>
<title>403 Forbidden</title>
</head>
<body bgcolor="white">
<center>
<h1>403 Forbidden</h1>
</center>
<hr/>
<center>nginx/1.4.6 (Ubuntu)</center>
</body>
</html>
```

Y si le corremos un scan con **nmap** a los puertos más conocidos obtenemos.

```bash
PORT STATE SERVICE VERSION  
22/tcp open ssh OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.7 (Ubuntu Linux; protocol 2.0)  
80/tcp open http nginx 1.4.6 (Ubuntu)  
111/tcp open rpcbind 2-4 (RPC #100000)  
443/tcp open ssl/http nginx 1.4.6 (Ubuntu)  
5666/tcp open tcpwrapped  
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Por buenas prácticas de seguridad esa información no debería ser revelada, y es bastante sencillo corregir eso (literalmente es modificar una línea en el archivo de configuración de nginx).

Con la ayuda de Burp Suite es posible analizar los request y eso nos arroja aún más información de cómo se comunica la app, aunque teniendo la [documentación de su api][1] a la mano ya no es tan necesario.

## Para terminar, que es lo que aprendimos hoy

  * En el desarrollo de este proyecto estuvieron involucradas al menos 3 partes: El [gobierno de Guadalajara][2], la empresa [Radmas][3] y [Urbiotica][4] (dejando de lado el posible caso de que en realidad ellos no tienen nada que ver y solo las credenciales de uno de sus clientes fueron leakeadas en la app, eso sería muy mala suerte)
  * Al menos la app de Android (que fue la que analice) fue desarrollada de forma nativa
  * Hacen buen uso de las funcionalidades para almacenar información, guardan la información sensible utilizando shared preference y bases de datos sqlite
  * El almacenamiento de imágenes lo hacen en la nube de aws
  * La app tiene credenciales hardcodeadas (posiblemente de un proyecto anterior del cual re utilizaron el código) y que al día de hoy funcionan
  * La app utiliza el servicio de **mejoratuciudad.org** que al parecer es un producto de **radmas.com** y podemos decir que es un software / plataforma / tecnologia especializada para hacer implementaciones en **smart cities**
  * Los servidores de mejoratuciudad.org no están hardenizados
  * Los servidores de mejoratuciudad.org cuentan con algún tipo de IDS/IPS que bloquea a usuarios después de X número de peticiones automatizadas.
  * La plataforma no implementa esos controles puesto que solo utilice una VPN para cambiar mi IP y ya pude seguir interactuando con la app sin problemas.
  * Debido al concepto de Jurisdicciones sabemos que la app está siendo implementada en muchas otras ciudades de México y el mundo (16 clientes para ser exactos según los servidores de **mejoratuciudad.org**)
  * Los servicios web no parecen vulnerables a algún tipo de ataque popular como SQL injection, xss, RCE, etc. Muy bien por Radmas 🙂 )
  * El código fuente de la aplicacion no fue ofuscado

Happy hacking … salu2

 [1]: http://api.mejoratuciudad.org/doc
 [2]: http://portal.guadalajara.gob.mx/
 [3]: http://radmas.com/
 [4]: http://www.urbiotica.net</manifest>
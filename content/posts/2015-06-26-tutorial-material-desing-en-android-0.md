---
title: 'Tutorial Material Design en Android #0'
author: Alevsk
type: post
date: 2015-06-26T23:54:00+00:00
url: /2015/06/tutorial-material-desing-en-android-0/
categories:
  - Android
  - Programming
  - Tutorials
tags:
  - android
  - material design
  - Programming
  - Solutions
  - Tutorials

---
## Crear un nuevo proyecto de Android Material Design

Hola lectores, esta es la introducción a una serie de tutoriales sobre **desarrollo de aplicaciones android** utilizando **material design** que tengo planeado hacer, antes que nada, si quieren saber bien que es el material design lo pueden ver desde el sitio oficial de google [aqui](http://www.google.com/design/spec/material-design/introduction.html), en resumidas cuentas una app hecha con este estilo se ve de esta forma.

[![howitowkrs](/images/howitowkrs.png)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-0/howitowkrs/)

Y eso precisamente es lo que vamos a crear :), así que manos a la obra, si no tienes Android Studio descárgalo [aca](https://developer.android.com/sdk/index.html), después de instalarlo asegúrate de tenerlo completamente actualizado.

En Android Studio, crearemos un nuevo proyecto, para eso nos vamos a:

**File > New > New Project** 

Nos aparecerá una ventana como la siguiente, aquí nos pedirán datos como el nombre de la app, el nombre de la compañía y el nombre del package

[![create_new_project](/images/create_new_project.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-0/create_new_project/)

En la siguiente pantalla vamos a elegir la versión mínima de SDK **api 14: Android 4.0 (IceCreamSandwich)** si, es posible hacer material design en apis anteriores a la 21! 🙂

Después en la siguiente pantalla vamos a elegir una aplicación totalmente en blanco (Add no Activity) esto es porque algunos de los “templates" disponibles utilizan mucho código y técnicas que actualmente son obsoletas,

[![activity_type](/images/activity_type.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-0/activity_type/)

La idea es que nosotros creemos todo desde cero. Por ultimo damos clic en **Finish** y estamos listos para comenzar a escribir código.  
Si no estas familiarizado con la interfaz de Android Studio ahora es un buen momento para hacerlo, primero que nada vale la pena mencionar que Android Studio utiliza gradle para sincronizar y mantener las dependencias de los proyectos, si estas interesado en esto deberías revisar el archivo **build.gradle** en el apartado de **Gradle Scripts** donde veras un poco mas acerca de lo que hablo :).

Por otra parte, vamos a revisar el contenido del archivo manifest (App > Manifest > AndroidManifest.xml)

```xml
<manifest package="com.alevsk.materialdesignapp" xmlns:android="http://schemas.android.com/apk/res/android">
<application android:allowbackup="true" android:icon="@mipmap/ic_launcher" android:label="@string/app_name" android:theme="@style/AppTheme">
</application>
</manifest>
```

Vemos que el theme actual de la aplicación está definido en los archivos de estilos (style.xml), por lo que ahora vamos a revisar que contiene ese.

[![styles](/images/styles.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-0/styles/)

```xml
<resources>
<!--– Base application theme. –-->
<style name="AppTheme" parent="Theme.AppCompat.Light.DarkActionBar">  
<!– Customize your theme here. –>  
</style>
</resources>
```

Localizamos el AppTheme y vamos a cambiar el valor de su parámetro parent de **Theme.AppCompat.Light.DarkActionBar** a **AppTheme.Base**, justo debajo vamos a agregar el nuevo estilo con el siguiente código que si utilizara **Theme.AppCompat.Light.DarkActionBar**

```xml
<style name="AppTheme.Base" parent="Theme.AppCompat.Light.DarkActionBar">
</style>
```

Quedando el archivo completo de la siguiente forma:

```xml
<resources>
<!--– Base application theme. –-->
<style name="AppTheme" parent="AppTheme.Base">  
<!– Customize your theme here. –>  
</style>
<style name="AppTheme.Base" parent="Theme.AppCompat.Light.DarkActionBar">
</style>
</resources>
```

Ahora, ya que nuestro objetivo es dar soporte material a las apps, ya sea lollipop (api >= 21) como pre lollipop (api < 21) debemos crear un nuevo archivo styles.xml, para eso en la carpeta values hacemos clic derecho, después **New > Value Resource** file y nos aparecerá una ventana como la siguiente:

[![new_styles](/images/new_styles.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-0/new_styles/)

Donde en **file name** ponemos **styles.xml**, después en **available qualifiers** nos vamos hasta abajo y seleccionamos versión, en el campo de texto que aparece escribimos 21, esto quiere decir que ese archivo se aplicara a los dispositivos Android que corran utilizando la api 21, ¿entienden a donde va esto? es posible escribir archivos de estilos diferentes para cada versión de la api, 14, 15, 16, 17 … 22 etc y hacer que nuestra api se vea diferente :), por lo pronto solo escribiremos xml para la api 21.

En el archivo **styles.xml** para la api 21 escribimos el siguiente xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<!--– Base application theme. –-->
<style name="AppTheme" parent="AppTheme.Base">  
<!– Customize your theme here. –>  
</style>
</resources>
```

En el archivo styles.xml para la api 21 no es necesario que definamos el estilo del tema **AppTheme.Base** puesto que ya lo definimos en el otro archivo de **styles.xml** y Android es lo suficientemente inteligente como para saber eso :), lo que vamos a hacer mas adelante sera definir algunas reglas de estilos y colores en cada archivo (ya no themes completos) para la personalizacion por versiones.

Lo que sigue, vamos a comenzar a crear **activities**, para eso en la carpeta de **Java**, clic derecho, después **New > Activity > Blank Activity**

[![new_activity](/images/new_activity.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-0/new_activity/)

Como es la primera Activity podemos dejar los datos por default, explico rapidamente:

  * **Activity Name**: el nombre de tu clase
  * **Layout Name**: el nombre del archivo xml que servirá como la vista de tu actividad
  * **Title Name**: el título de tu actividad (el que aparece en el ActionBar / ToolBar)
  * **Menu Resource Name**: el nombre del archivo xml que tendrá los items para poblar el ToolBar de tu actividad

Damos clic en Finish.

Android Studio nos habrá creado dos nuevos archivos, **MainActivity.java** y **activity_main.xml**

[![activity](/images/activity.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-0/activity/)

Si corremos la app y por alguna razón crashea es conveniente revisar el log de errores, me sucedió la primera vez que Android Studio no podía determinar cual era la activity por default para lanzar la app, y eso era debido a que en el archivo **AndroidManifest.xml** no estaba definido … por alguna extraña razón XD.

```xml
<activity android:label="@string/title\_activity\_main" android:name=".MainActivity">
<intent-filter>
<action android:name="android.intent.action.MAIN"></action>
<category android:name="android.intent.category.LAUNCHER"></category>
</intent-filter>
</activity>
```

El intent-filter con sus definiciones es lo que se necesitaba agregar para solucionar el problema y correr la app :), si ejecutamos la app en un teléfono o emulador con Android 4.x o 5.x tendremos algo como lo siguiente.

[![app](/images/app.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-0/app/)

¿Nada impresionante verdad? En el siguiente tutorial aprenderemos a [definir los colores de la aplicación](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-1/) y comenzaremos a crear algunos elementos nuevos en la interfaz. salu2
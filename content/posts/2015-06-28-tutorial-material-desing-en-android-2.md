---
title: 'Tutorial Material Design en Android #2'
author: Alevsk
type: post
date: 2015-06-28T06:30:08+00:00
url: /2015/06/tutorial-material-desing-en-android-2/
categories:
  - Android
  - Programming
  - Technology
  - Tutorials
tags:
  - android
  - material design
  - Programming
  - Solutions
  - Technology
  - Tutorials

---
## Definir la ToolBar

Esta es la tercera parte del tutorial **desarrollo de apps** para **Android** utilizando **Material Design**, ahora aprenderemos acerca de como definir la **ToolBar** de nuestra aplicación, para hacerlo seguiremos 5 sencillos pasos:

  * En el archivo **styles.xml** utilizaremos **Theme.AppCompat.Light.NoActionBar**
  * Definiremos un archivo **app_bar.xml** para nuestra ToolBar
  * Incluiremos ese archivo con la directiva **include** en nuestro **main_activity.xml** (la vista de nuestra Activity)
  * En nuestra actividad principal **MainActivity.java** vamos a crear una instancia de la **ToolBar** para poder manipularla
  * Por ultimo nos aseguraremos de incluir soporte para dispositivos pre lollipop (api < 21)

[![toolbars](/images/toolbars.png)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-2/toolbars/)

Antes que nada, como en las ediciones anteriores les recomiendo que se empapen un poco de la teoría de las ToolBars en el siguiente [link](http://www.google.com.mx/design/spec/layout/structure.html#structure-ui-regions), ya que **Material Design** no es solo escribir código y ya, tenemos que apegarnos a ciertos lineamientos que se explican muy bien en la documentación oficial y pues manos a la obra, o manos al código mejor dicho XD.

En nuestro proyecto vamos a nuestro archivo styles.xml que está en app > res > values > styles.xml y remplazamos **Theme.AppCompat.Light.DarkActionBar** por **Theme.AppCompat.Light.NoActionBar** quedando el código de la siguiente manera:

[![noactionbar](/images/noactionbar.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-2/noactionbar/)

Esto lo hacemos para indicar que no vamos a utilizar la **ToolBar** por defecto que **Android** maneja, en cambio elegimos no incluir ninguna (al menos no desde el theme que utilizamos), si corremos nuestra aplicación justo ahora tendremos algo como esto.

[![app_no_toolbar](/images/app_no_toolbar.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-2/app_no_toolbar/)

Sin **Toolbar**, ¿qué feo se ve no?, ahora solucionaremos eso de la siguiente forma, en la carpeta layout de nuestro proyecto (**app > res > layout**) vamos a crear un nuevo archivo xml, ya saben, botón derecho **New > Layout resource file** y le ponemos de nombre **app_bar.xml**, puede ser cualquier otro nombre pero por convención utilizaremos ese, también en el campo de Root element utilizaremos ToolBar como se muestra en la siguiente imagen.

[![new_toolbar](/images/new_toolbar.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-2/new_toolbar/)

Vemos el contenido del archivo recién creado y notamos que Android Studio nos marca un error en el elemento Toolbar XD, el código que les debió haber generado automáticamente es el siguiente:

```xml
<?xml version="1.0" encoding="utf-8"?>
<toolbar android:layout\_height="match\_parent" android:layout\_width="match\_parent" xmlns:android="http://schemas.android.com/apk/res/android">
</toolbar>
```

El error, de nuevo, es debido a la versión mínima de api soportada por nuestra aplicación, si no mal recuerdo al crear nuestro proyecto elegimos la api 14 y el control Toolbar es para api 21 por lo que para solucionar esto remplazaremos el código por el siguiente:

```xml
<?xml version="1.0" encoding="utf-8"?>
<android.support.v7.widget.toolbar android:layout\_height="match\_parent" android:layout\_width="match\_parent" xmlns:android="http://schemas.android.com/apk/res/android">
</android.support.v7.widget.toolbar>
```

Y el error desaparecerá 🙂 les dejo mas documentación sobre esta maravillosa librería para dar soporte [android.support.v7.app](https://developer.android.com/tools/support-library/setup.html)

Lo que siguen, en nuestro archivo main\_activity.xml vamos a incluir el app\_bar.xml que acabamos de crear, para eso lo abrimos y utilizamos la directiva include de la siguiente forma.

```xml
<relativelayout android:layout\_height="match\_parent" android:layout\_width="match\_parent" tools:context="com.alevsk.materialdesignapp.MainActivity" xmlns:android="http://schemas.android.com/apk/res/android" xmlns:tools="http://schemas.android.com/tools">
<include android:id="@+id/app\_bar" layout="@layout/app\_bar"></include>
<textview android:layout\_height="wrap\_content" android:layout\_width="wrap_content" android:text="@string/hello\_world"></textview>
</relativelayout>
```

Ok, ahora nos vamos a nuestro archivo **MainActivity.java** que nos toca escribir el primer código Java del proyecto, lo que haremos aquí será crear una nueva propiedad (variable privada tipo Toolbar) e instanciar la de nuestra vista XML en el método **onCreate**

```java
public class MainActivity extends ActionBarActivity {

private Toolbar toolbar;

@Override  
protected void onCreate(Bundle savedInstanceState) {  
super.onCreate(savedInstanceState);  
setContentView(R.layout.activity_main);

toolbar = (Toolbar) findViewById(R.id.app_bar);  
setSupportActionBar(toolbar);  
}
```

Cuando agregamos la variable tipo **Toolbar** un error muy común que he observado es el tipo de librería que importa el proyecto, asegúrense que este importando **import android.support.v7.widget.Toolbar;** de otra manera el proyecto te marcara errores al momento de compilar la apk.

¿Que acabamos de hacer?, ahora lo explico, creamos una nueva variable Toolbar, después creamos la instancia tomando como referencia la que definimos anteriormente en nuestro main_activity.xml y al final utilizamos el método setSupportActionBar para indicarle a Android que vamos a utilizar nuestra propia Toolbar, procedemos a correr la app y vemos lo que pasa.

[![app_custom_toolbar](/images/app_custom_toolbar.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-2/app_custom_toolbar/)

:S horrible ¿cierto? veamos que paso aquí y cómo solucionarlo. Cuando definimos nuestra propia Toolbar tenemos que asegurarnos de definir también el ancho y el alto del elemento, ¿recuerdan el link a la documentación oficial que les deje al inicio?, ahora es un buen momento para revisarla, también tenemos que definir el orden en el que se dibujaran los elementos en la pantalla, para eso en main_activity.xml vamos a utilizar una propiedad llamada **layout_below** en el elemento **TextView** para indicar que queremos que aparezca debajo de nuestra **Toolbar**

```xml
<relativelayout android:layout\_height="match\_parent" android:layout\_width="match\_parent" tools:context="com.alevsk.materialdesignapp.MainActivity" xmlns:android="http://schemas.android.com/apk/res/android" xmlns:tools="http://schemas.android.com/tools">
<include android:id="@+id/app_bar" layout="@layout/app_bar"></include>
<textview android:layout\_below="@+id/app\_bar" android:layout\_height="wrap\_content" android:layout\_width="wrap\_content" android:text="@string/hello_world"></textview>
</relativelayout>
```

También definimos el color de fondo en nuestro archivo app\_bar.xml y cambiamos su altura de match\_parent a wrap_content.

```xml
<?xml version="1.0" encoding="utf-8"?>
<android.support.v7.widget.toolbar android:background="@color/primaryColor" android:layout\_height="wrap\_content" android:layout\_width="match\_parent" xmlns:android="http://schemas.android.com/apk/res/android">
</android.support.v7.widget.toolbar>
```

Guardamos los cambios y corremos la app de nuevo.

[![app_custom_toolbar2](/images/app_custom_toolbar2.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-2/app_custom_toolbar2/)

Listo, mucho mejor 🙂 , pareciera que no avanzamos nada en este tercer tutorial, sin embargo tenemos ya una **Toolbar** personalizada funcional y esto nos servirá para lo que sigue que será agregar algunos iconos! salu2
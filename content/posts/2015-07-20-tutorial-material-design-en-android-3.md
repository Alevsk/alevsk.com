---
title: 'Tutorial Material Design en Android #3'
author: Alevsk
type: post
date: 2015-07-20T04:01:07+00:00
url: /2015/07/tutorial-material-design-en-android-3/
categories:
  - Android
  - Personal
  - Programming
  - Snippets
  - Technology
  - Tips
  - Tutorials
tags:
  - android
  - material design
  - Social Media
  - software libre
  - Solutions
  - Technology

---
## Agregando iconos (actions) al ToolBar

Hola lectores programadores :), continuamos con la serie de tutoriales de **Material Design en Android**, siguiendo con los post anteriores ahora toca agregar algunos elementos a nuestra [Toolbar personalizada][1], pero primero nos encargaremos de un pequeño “bug estético", actualmente nuestra app luce así y si hacemos tap en el icono superior derecho (3 puntos) veremos que la letra del popupMenu es apenas visible. Corrijamos eso.  
[![popupmenu_bug](/images/popupmenu_bug.jpg)](http://www.alevsk.com/2015/07/tutorial-material-design-en-android-3/popupmenu_bug/)

Nos vamos a nuestros ya conocidos archivos **styles.xml**

  * /app/src/main/res/values/styles.xml
  * /app/src/main/res/values-21/styles.xml (api 21)

Y vamos a agregar un nuevo item con nombre **popupTheme**, quedando de la siguiente forma

**values/style.xml**  
```xml
<resources>
<!--– Base application theme. –-->
<style name="AppTheme" parent="AppTheme.Base">  
<!– Customize your theme here. –>  
</style>
<style name="AppTheme.Base" parent="Theme.AppCompat.Light.NoActionBar">  
<item name="colorPrimary">@color/primaryColor</item>  
<item name="colorPrimaryDark">@color/primaryColorDark</item>  
<item name="colorAccent">@color/colorAccent</item>  
<item name="popupTheme">@style/Base.ThemeOverlay.AppCompat.Dark</item>  
</style>
</resources>
```

**values-21/style.xml (api 21)**  
```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<!--– Base application theme. –-->
<style name="AppTheme" parent="AppTheme.Base">  
<item name="android:colorPrimary">@color/primaryColor</item>  
<item name="android:colorPrimaryDark">@color/primaryColorDark</item>  
<item name="android:textColorPrimary">@color/textColorPrimary</item>  
<item name="android:colorAccent">@color/colorAccent</item>  
<item name="android:popupTheme">@style/Base.ThemeOverlay.AppCompat.Dark</item>  
</style>
</resources>
```

Guardamos y corremos la aplicación de nuevo y ahora veremos algo como lo siguiente, ¿Mucho mejor cierto?

[![popupmenu_dark](/images/popupmenu_dark.jpg)](http://www.alevsk.com/2015/07/tutorial-material-design-en-android-3/popupmenu_dark/)

Es posible personalizar aún mas este elemento del **ToolBar**, estos son algunos de los atributos que podemos utilizar

  * popupMenuStyle
  * textColorPrimary
  * popupAnimationStyle>
  * popupBackground

Se puede personalizar prácticamente cualquier aspecto del menú, por ejemplo:

[![popupmenu_custom2](/images/popupmenu_custom2.jpg)](http://www.alevsk.com/2015/07/tutorial-material-design-en-android-3/popupmenu_custom2/)

Les dejo de tarea hacer su propio menú custom 🙂 y bueno ahora que tenemos resuelta esa parte del **popupMenu** toca agregar los iconos, en nuestro proyecto de Android Studio, en la carpeta res (resources) dentro del apartado de menú encontramos un archivo llamado **menu_main.xml** (si por algún motivo no está entonces deberán crearlo **/res/menu/menu_main.xml**).

Como en todos los tutoriales les dejo la documentación oficial sobre los lineamientos sobre los iconos, sus dimensiones y formas [aqui](http://www.google.com.mx/design/spec/style/icons.html#) y [aca](http://www.google.com.mx/design/spec/layout/metrics-keylines.html#).

Por default nuestro menú solo tiene 1 elemento como podemos ver en el siguiente código

```xml
<menu tools:context="com.alevsk.materialdesignapp.MainActivity" xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:tools="http://schemas.android.com/tools">
<item android:id="@+id/action_settings" android:orderincategory="100" android:title="@string/action_settings" app:showasaction="never"></item>
</menu>
```

El elemento item tiene algunos atributos, por ejemplo app:showAsAction puede tomar tres valores:

  * never: No mostrara el icono
  * ifRoom: Si hay espacio mostrara el icono
  * always: Siempre mostrara el icono

**android:title** es el atributo donde definimos el nombre de la acción (si por ejemplo deciden no mostrar un icono o mostrarlo solo si hay espacio, por default el título de la acción será el que definan con este atributo).

Por el momento vamos a definir 3 acciones (conforme avance esto los remplazaremos), quedando el código del archivo menu_main.xml de la siguiente manera.

```xml
<menu tools:context="com.alevsk.materialdesignapp.MainActivity" xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:tools="http://schemas.android.com/tools">
<item android:icon="@drawable/abc\_ic\_search\_api\_mtrl_alpha" android:id="@+id/action_search" android:orderincategory="1" android:title="Busqueda" app:showasaction="always"></item>
<item android:icon="@drawable/abc\_ic\_menu\_copy\_mtrl\_am\_alpha" android:id="@+id/action_copy" android:orderincategory="2" android:title="Copiar" app:showasaction="always"></item>
<item android:icon="@drawable/abc\_ic\_menu\_selectall\_mtrl_alpha" android:id="@+id/action_selectall" android:orderincategory="3" android:title="Seleccionar todo" app:showasaction="always"></item>
</menu>
```

Corremos la app y veremos algo como esto

[![toolbar_icons](/images/toolbar_icons.jpg)](http://www.alevsk.com/2015/07/tutorial-material-design-en-android-3/toolbar_icons/)

¿Los iconos no son muy visibles verdad?, podemos arreglar esto rápidamente, el tema por default de nuestra aplicación es texto oscuro sobre fondos claros, esa es la razón por la que los iconos tienen un color oscuro, sin embargo podemos modificar nuestro archivo **app_bar.xml** e indicar que queremos que esa parte especifica de la app (ToolBar) utilice el tema de textos claros sobre fondos oscuros, así que editamos **/app/src/main/res/layout/app_bar.xml** y definimos el tema Holo como se muestra a continuación.

```xml
<?xml version="1.0" encoding="utf-8"?>
<android.support.v7.widget.toolbar android:background="@color/primaryColor" android:layout\_height="wrap\_content" android:layout\_width="match\_parent" app:theme="@style/Theme.AppCompat.NoActionBar" xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">
</android.support.v7.widget.toolbar>
```

[![toolbar_icons3](/images/toolbar_icons3.jpg)](http://www.alevsk.com/2015/07/tutorial-material-design-en-android-3/toolbar_icons3/)

Eso es todo por ahora, en el siguiente tutorial vamos a definir de que va a tratar nuestra app y aprenderemos a implementar desde cero unos de los elementos más poderosos de **Android**, el **NavigationDrawer** 🙂 salu2

 [1]: http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-2/
---
title: 'Tutorial Material Design en Android #4'
author: Alevsk
type: post
date: 2015-11-08T23:14:10+00:00
url: /2015/11/tutorial-material-design-en-android-4/
categories:
  - Android
  - Geek
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - android
  - hackers
  - Java
  - material design
  - Programming
  - software libre
  - Solutions
  - Technology
  - Tutorials

---
## Crear un Navigation Drawer para Android

Después de una pequeña pausa retomamos la serie de **tutoriales de Material Design en Android**, en el tutorial anterior aprendimos [como agregar iconos (actions) a nuestra Toolbar](https://www.alevsk.com/2015/07/tutorial-material-design-en-android-3/), así que lo que sigue ahora es aprender cómo implementar el **Navigation Drawer**.

El **Navigation Drawer en Android** es un panel que podemos utilizar en nuestra app y que por lo general contiene un menú para movernos o “navegar" por las distintas secciones en la aplicación, la principal ventaja es que puede permanecer oculta la mayor parte del tiempo y desplegarse solo cuando el usuario lo necesite, de esa manera “economizamos" el espacio en la pantalla del teléfono, como en los tutoriales anteriores, si quieren aprender un poco más sobre la teoría siempre pueden consultar la documentación oficial de google [Navigation Drawer](http://www.google.com.mx/design/spec/patterns/navigation-drawer.html)
[![patterns_navdrawer_settings1](/images/patterns_navdrawer_settings1-169x300.png)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/patterns_navdrawer_settings1/)

También vale la pena mencionar que hay básicamente 3 estilos de **Navigation Drawer**:

  * Navigation Drawer por debajo de la Toolbar oscurenciendola
  * Navigation Drawer por debajo de la Toolbar sin oscurecerla
  * Navigation Drawer por encima de la Toolbar

El estilo que queramos lograr dependerá de cómo escribamos el **xml** en nuestras **views**, y un poco de Java también

<div style="clear:both;overflow:auto;">
[![playstore_style](/images/playstore_style.gif)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/playstore_style/)[![drawer_bellow](/images/drawer_bellow.gif)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/drawer_bellow/)[![drawer_over_toolbar](/images/drawer_over_toolbar.gif)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/drawer_over_toolbar/)
</div>

Pues manos a la obra, o mejor dicho al código, vamos a nuestro archivo **activity_main.xml** y deberíamos de tener algo así.

[![activity_main](/images/activity_main-500x227.jpg)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/activity_main/)

Vamos a modificar un poco nuestro **código xml** y agregaremos un par de elementos llamados [DrawerLayout](http://developer.android.com/reference/android/support/v4/widget/DrawerLayout.html), [FrameLayout](http://developer.android.com/reference/android/widget/FrameLayout.html) y **NavigationDrawer**, viendo la siguiente imagen quedara más claro lo que vamos a hacer en nuestra activity.

[![drawer_layout_demon](/images/drawer_layout_demon.png)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/drawer_layout_demon/)

Vamos a crear un elemento **android.support.v4.widget.DrawerLayout** y vamos a meter todo nuestro código existente dentro de esa etiqueta.

```xml
<android.support.v4.widget.drawerlayout android:id="@+id/drawer_layout" android:layout\_height="match\_parent" android:layout\_width="match\_parent" xmlns:android="http://schemas.android.com/apk/res/android" xmlns:tools="http://schemas.android.com/tools">
<relativelayout android:layout\_height="match\_parent" android:layout\_width="match\_parent" tools:context="com.alevsk.materialdesignapp.MainActivity">
<include android:id="@+id/app_bar" layout="@layout/app_bar"></include>
<textview android:layout\_below="@+id/app\_bar" android:layout\_height="wrap\_content" android:layout\_width="wrap\_content" android:text="@string/hello_world"></textview>
</relativelayout>
</android.support.v4.widget.drawerlayout>
```

Lo siguiente es crear un [Fragment](http://developer.android.com/reference/android/app/Fragment.html) y lo que hago normalmente para tener mi código más organizado es crear un nuevo Package en el proyecto llamado fragments y ahí empiezo a crearlos, para eso en su **com.alevsk.materialdesignapp > botón secundario > new > Package** y le ponen el nombre que deseen, yo le puse **fragments** para que sea descriptivo, después de eso procedemos a crear la nueva clase como se muestra en la siguiente imagen.

[![fragments](/images/fragments.jpg)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/fragments/)

Nos aparecerá el siguiente cuadro de dialogo donde tendremos que elegir el nombre del nuevo menú **NavigationDrawer** (fragmento), le ponemos **NavigationDrawerFragment** o como ustedes quieran pero que sea descriptivo hacia el hecho de que será el menú de nuestra aplicación, asegúrense de marcar la opción de crear el **layout xml** y podemos desmarcar las dos opciones de abajo, el código que nos genere **Android studio** será más limpio y nosotros implementaremos los métodos que necesitamos desde 0, para terminar damos clic en el botón de **Finish**.

[![navigationdrawerfragment](/images/navigationdrawerfragment.jpg)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/navigationdrawerfragment/)

Android Studio nos habrá generado dos archivos, **NavigationDrawerFragment.java** y **fragment\_navigation\_drawer.xml**

[![1](/images/1.jpg)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/attachment/1/)
[![2](/images/21.jpg)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/2-3/)

En nuestro **fragment\_navigation\_drawer.xml** vamos a modificar el elemento principal de Fragment a RelativeLayout quedando el código de la siguiente manera

```xml
<relativelayout android:layout\_height="match\_parent" android:layout\_width="match\_parent" tools:context="com.alevsk.materialdesignapp.fragments.NavigationDrawerFragment" xmlns:android="http://schemas.android.com/apk/res/android" xmlns:tools="http://schemas.android.com/tools">
<!--– TODO: Update blank fragment layout –-->
<textview android:layout\_height="match\_parent" android:layout\_width="match\_parent" android:text="@string/hello\_blank\_fragment"></textview>
</relativelayout>
```

Hicimos este cambio ya que más adelante necesitaremos agregar elementos extras como un [RecyclerView](http://developer.android.com/reference/android/support/v7/widget/RecyclerView.html), a continuación vamos al archivo **activity_main.xml** y vamos a agregar nuestro **NavigationDrawer** usando un elemento **fragment** de la siguiente forma.

```xml
<fragment android:id="@+id/fragment\_navigation\_drawer" android:layout\_height="match\_parent" android:layout_gravity="start" android:layout_width="280dp" android:name="com.alevsk.materialdesignapp.fragments.NavigationDrawerFragment" app:layout="@layout/fragment\_navigation\_drawer" tools:layout="@layout/fragment\_navigation\_drawer"></fragment>
```

El codigo final del **activity_main.xml** es el siguiente:  
[![3](/images/3.jpg)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/attachment/3/)

Lo que sigue es crear un objeto **NavigationDrawer** en nuestro **MainActivity.java** 

```java
NavigationDrawerFragment drawerFragment = (NavigationDrawerFragment) getSupportFragmentManager().findFragmentById(R.id.fragment\_navigation\_drawer);
```

Si por alguna razón les da un error de compatibilidad asegúrense que en **NavigationDrawerFragment.java** en la sección de **import** (hasta arriba) el **Fragment** que esté utilizando sea **android.support.v4.app.Fragment**

Ya que estamos en este archivo vamos a crear de una vez un método llamado **setUp** que va a servir para inicializar los componentes de nuestro **NavigationDrawer**, también vamos a utilizar un nuevo objeto llamado [ActionBarDrawerToogle](http://developer.android.com/reference/android/support/v4/app/ActionBarDrawerToggle.html) cuya finalidad es la de manejar nuestro **DrawerLayout** y **Toolbar** de una manera más eficiente, así como encargarse de manejar el evento de abrir y cerrar el panel de navegación.

```java
public void setUp(DrawerLayout drawerLayout, Toolbar toolbar) {  
mDrawerLayout = drawerLayout;  
mToolbar = toolbar;  
mDrawerToggle = new ActionBarDrawerToggle(getActivity(),drawerLayout,toolbar, R.string.open, R.string.close) {  
@Override  
public void onDrawerClosed(View drawerView) {  
super.onDrawerClosed(drawerView);  
}

@Override  
public void onDrawerOpened(View drawerView) {  
super.onDrawerOpened(drawerView);  
}  
};  
mDrawerLayout.setDrawerListener(mDrawerToggle);  
}
```

Tip: R.string.open y R.string.close son necesarios para el constructor del **ActionBarDrawerToggle** ya que son los textos que aparecen al abrir y cerrar el panel, pueden definir esas cadenas en su archivo **strings.xml** que se encuentra en **res/values**

```xml
<string name="open">Abierto</string>
<string name="close">cerrado</string>
```

De nuevo, aquí mucho cuidado, asegúrense de que el Toolbar que estén importando sea **android.support.v7.widget.Toolbar** para efectos de compatibilidad, ya que si utilizan la clase por defecto les va a dar errores en los demás archivos.

Lo que acabamos de hacer en nuestro código es definir un nuevo ActionBarDrawerToggle, vinculamos el **DrawerLayout** y **Toolbar** que estamos recibiendo desde nuestro **MainActivity** y preparamos el listener (manejador de eventos) para cuando el usuario abra y cierre el panel de navegación.

En el MainActivity.java después de instanciar nuestro NavigationDrawer mandamos llamar el método

```java
public class MainActivity extends ActionBarActivity {

private Toolbar toolbar;

@Override  
protected void onCreate(Bundle savedInstanceState) {  
super.onCreate(savedInstanceState);  
setContentView(R.layout.activity_main);

toolbar = (Toolbar) findViewById(R.id.app_bar);  
setSupportActionBar(toolbar);

NavigationDrawerFragment drawerFragment = (NavigationDrawerFragment) getSupportFragmentManager().findFragmentById(R.id.fragment\_navigation\_drawer);  
drawerFragment.setUp((DrawerLayout)findViewById(R.id.drawer_layout),toolbar);  
}
```

La clase **NavigationDrawerFragment** quedo de la siguiente manera  
[![NavigationDrawerFragment](/images/41.jpg)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/4-2/)

En este punto, si corremos nuestra aplicación y deslizamos haciendo tap desde la izquierda podemos observar como la pantalla comienza a oscurecerse, si ponemos un poco más de atención podemos ver el texto de nuestro fragment encima de la app"**Hello Blank Fragment**“, ha funcionado! ahora solo nos queda poner un poco de estilo para hacer a aplicación más agradable a la vista.

[![navigation_drawer_feo](/images/navigation_drawer_feo-192x300.jpg)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/navigation_drawer_feo/)

En nuestro archivo **colors.xml** (se encuentra en **app/res/values/colors.xml**) podemos definir nuevos colores, por ejemplo yo he definido uno nuevo llamado graypanel

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<color name="primaryColor">#E91E63</color>
<color name="primaryColorDark">#C2185B</color>
<color name="textColorPrimary">#FFFFFF</color>
<color name="grayPanel">#EEEEEE</color>
<color name="lightGray">#d6d6d6</color>
<color name="colorAccent">#8BC34A</color>
</resources>
```

Y despues en nuestro **fragment\_navigation\_drawer.xml** definimos el color de fondo a nuestro **RelativeLayout** con **android:background="@color/grayPanel"**

```xml
<relativelayout android:background="@color/grayPanel" android:layout\_height="match\_parent" android:layout\_width="match\_parent" tools:context="com.alevsk.materialdesignapp.fragments.NavigationDrawerFragment" xmlns:android="http://schemas.android.com/apk/res/android" xmlns:tools="http://schemas.android.com/tools">
<!--– TODO: Update blank fragment layout –-->
<textview android:layout\_height="match\_parent" android:layout\_width="match\_parent" android:text="@string/hello\_blank\_fragment"></textview>
</relativelayout>
```

[![navigation_drawer_color](/images/navigation_drawer_color-192x300.jpg)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/navigation_drawer_color/)

¿Un poco mejor cierto? pero todavía le falta bastante, por ejemplo no resulta obvio para el usuario saber que la aplicación tiene un menú lateral, lo que vamos a hacer es agregar el clásico icono de menú de lado izquierdo, para eso utilizaremos un método llamado **syncState** de nuestro objeto **DrawerToggle**.

Nos vamos a nuestro archivo **NavigationDrawerFragment.java** y agregamos el siguiente código después de haber hecho el **mDrawerLayout.setDrawerListener(mDrawerToggle);**

```java
mDrawerLayout.post(new Runnable() {  
@Override  
public void run() {  
mDrawerToggle.syncState();  
}  
});
```

Corremos la app de nuevo y automáticamente nos aparecerá un icono de menú.

[![menu_icon](/images/menu_icon-500x222.jpg)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/menu_icon/)

Una vez abierto el menú de navegación rara notaran que si hacemos tap donde se supone que esta el botón de menú el panel se cierra, es bastante raro pues la aplicación no está respetando las “capas", podemos corregir ese comportamiento bajando un poco el **NavigationDrawer**.

Modificamos un poco nuestro archivo **main_activity.xml**, si se fijan bien ahora nuestro **DrawerLayout** esta debajo de nuestra **app_bar**, ambos elementos estan al mismo nivel y rodeados por un **LinearLayout** con orientación vertical.

```xml
<linearlayout android:background="@color/lightGray" android:layout\_height="match\_parent" android:layout\_width="match\_parent" android:orientation="vertical" xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:tools="http://schemas.android.com/tools">
<include android:id="@+id/app_bar" layout="@layout/app_bar"></include>
<android.support.v4.widget.drawerlayout android:id="@+id/drawer_layout" android:layout\_height="match\_parent" android:layout\_width="match\_parent">
<relativelayout android:layout\_height="match\_parent" android:layout\_width="match\_parent">
<textview android:layout\_height="match\_parent" android:layout\_width="match\_parent" android:text="@string/hello\_blank\_fragment"></textview>
</relativelayout>
<fragment android:id="@+id/fragment\_navigation\_drawer" android:layout\_height="match\_parent" android:layout_gravity="start" android:layout_width="280dp" android:name="com.alevsk.materialdesignapp.fragments.NavigationDrawerFragment" app:layout="@layout/fragment\_navigation\_drawer" tools:layout="@layout/fragment\_navigation\_drawer"></fragment>
</android.support.v4.widget.drawerlayout>
</linearlayout>
```

[![drawer_navigation](/images/drawer_navigation-425x300.jpg)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/drawer_navigation/)

Y eso es todo por ahora, así es como se programa un **NavigationDrawer** desde 0 :), en el siguiente tutorial implementaremos las opciones en nuestro menú de navegación, para eso aprenderemos a utilizar los **RecyclerViews**.

He montado un repositorio en [Github](https://github.com/Alevsk/) con el código de la aplicación que vamos desarrollando durante los tutoriales, si tienen alguna duda pueden consultarlo directamente de ahí o preguntarme en los comentarios [https://github.com/Alevsk/Material-design-en-Android](https://github.com/Alevsk/Material-design-en-Android)

salu2
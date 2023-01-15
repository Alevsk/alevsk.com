---
title: 'Tutorial Material Design en Android #5'
author: Alevsk
type: post
date: 2016-01-24T10:00:31+00:00
url: /2016/01/tutorial-material-design-en-android-5/
categories:
  - Android
  - Geek
  - Java
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - android
  - Hello World
  - material design
  - Programming
  - software libre
  - Solutions
  - Technology
  - Tutorials

---
## Crear un RecyclerView para Android

Hola lectores, ha pasado un tiempo desde que publique la última entrega del tutorial de **[Material Design en Android][1]** en donde aprendimos a [crear un Navigation Drawer][2], continuamos con los tutoriales y en esta ocasión les enseñare a crear un [RecyclerView][3].

Pero antes, ¿Que es un **RecyclerView**?, seguramente muchos lo abran visto ya en acción, este tipo de componente es cada vez más y más popular y ha venido remplazando a las antiguas ListViews, se trata de un componente que nos permite crear listas de contenedores que a su vez pueden tener dentro otros componentes (TextView, EditText, ImageView, etc.). El **RecyclerView** tiene la particularidad de haber sido diseñado con la eficiencia en mente, como su nombre lo indica los objetos que son visible en la pantalla son los que se dibujan en pantalla y una vez que desaparecen (el usuario hace scroll) estos remplazan su contenido (se reciclan) para mostrar otro tipo de información.

Imaginemos una lista de 100 contactos, en la pantalla de nuestro teléfono solo podemos renderizar 5 contactos a la vez, en lugar de renderizar los 100 desde un inicio solo vamos remplazando la información en las filas de nuestro **RecyclerView** conforme lo vamos necesitando, cabe decir que este es un proceso automático.

[![list_mail](/images/list_mail-176x300.png)](http://www.alevsk.com/2016/01/tutorial-material-design-en-android-5/list_mail/)

Pero el RecyclerView es mucho más que eso, a diferencia de su predecesor con este nuevo componente podemos crear listas con diferentes tipos de layouts

<div style="clear:both;">
</div>
[![20150415193645985](/images/20150415193645985-207x300.gif)](http://www.alevsk.com/2016/01/tutorial-material-design-en-android-5/attachment/20150415193645985/)
[![images](/images/images-168x300.jpg)](http://www.alevsk.com/2016/01/tutorial-material-design-en-android-5//images/)
[![EAF-MD3](/images/EAF-MD3-169x300.png)](http://www.alevsk.com/2016/01/tutorial-material-design-en-android-5/eaf-md3/)
<div style="clear:both;">
</div>

Retomamos nuestro proyecto, como les comentaba en la publicación pasada he subido el código realizado hasta el momento en el siguiente repositorio [https://github.com/Alevsk/Material-design-en-Android](https://github.com/Alevsk/Material-design-en-Android).

Lo primero que vamos a hacer sera agregar la dependencia a nuestro proyecto en el archivo de gradle, abrimos el archivo build.gradle que se encuentra en MaterialdesignApp (proyecto)> app > build.gradle y en la parte de abajo en el apartado de dependencias agregaremos  
_compile 'com.android.support:recyclerview-v7:+'_ quedando de la siguiente forma

```code
dependencies {  
compile fileTree(dir: 'libs', include: ['*.jar'])  
compile 'com.android.support:appcompat-v7:22.2.0'  
compile 'com.android.support:recyclerview-v7:22.2.0'  
}
```

Sincronizamos gradle para descargar las dependencias (o también podemos dar re build al proyecto) y una vez tenemos la dependencia vamos a comenzar a utilizar el componente, vamos a nuestro archivo **fragment\_navigation\_drawer.xml** (aquí vamos a crear el menú), si no recuerdan donde está el archivo se encuentra en **MaterialdesignApp > app > src > main > res > layout > fragment\_navigation\_drawer.xml**

Por el momento tenemos esto, un simple texto ¿bastante simple cierto?

[![Capture](/images/Capture-1.jpg)](http://www.alevsk.com/2016/01/tutorial-material-design-en-android-5/capture-2/)
[![drawer_navigation](/images/drawer_navigation-425x300.jpg)](http://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/drawer_navigation/)

Al final de nuestro tutorial vamos aprender a crear algo como esto :), pues manos a la obra, o mejor dicho al codigo XD

[![16170261501_9b7ce86ca7_b](/images/16170261501_9b7ce86ca7_b.jpg)](http://www.alevsk.com/2016/01/tutorial-material-design-en-android-5/16170261501_9b7ce86ca7_b/)

En nuestro archivo XML (**fragment\_navigation\_drawer.xml**) vamos a crear nuestro **RecyclerView** con el siguiente código, si se fijan elimine el **TextView** que teníamos porque ya no lo necesitamos.

```xml
<relativelayout android:background="@color/grayPanel" android:layout\_height="match\_parent" android:layout\_width="match\_parent" tools:context="com.alevsk.materialdesignapp.fragments.NavigationDrawerFragment" xmlns:android="http://schemas.android.com/apk/res/android" xmlns:tools="http://schemas.android.com/tools">
<android.support.v7.widget.recyclerview android:id="@+id/drawerList" android:layout\_height="wrap\_content" android:layout\_width="match\_parent">
</android.support.v7.widget.recyclerview>
</relativelayout>
```

Una vez añadido el componente en nuestra vista xml vamos a nuestro controller **NavigationDrawerFragment.java** (MaterialdesignApp > app > src > main > java > com.alevsk.materialdesignapp > fragments > NavigationDrawerFragment.java) y definimos una nueva variable tipo RecyclerView como propiedad de la clase

```java
public class NavigationDrawerFragment extends Fragment {

private RecyclerView mRecyclerView;  
private ActionBarDrawerToggle mDrawerToggle;  
private DrawerLayout mDrawerLayout;  
private Toolbar mToolbar;  
….  
..
```

Una vez creado nuestro RecyclerView vamos a agregar la referencia hacia su objeto xml, para eso en el método **onCreateView**, vamos a modificar un poco el código, actualmente tenemos algo como esto

[![Capture](/images/Capture-3.jpg)](http://www.alevsk.com/2016/01/tutorial-material-design-en-android-5/capture-4/)

Lo remplazamos por esto, sencillo, a estas alturas del tutorial ya deberían saber que estamos obteniendo el elemento mediante el id (layout.findViewById(R.id.drawerList)) que definimos, estamos haciendo un cast (RecyclerView) y lo estamos asignando a la variable **mRecyclerView**, por ultimo retornamos el layout (View) que es con el que trabajara la aplicacion.

```java
@Override  
public View onCreateView(LayoutInflater inflater, ViewGroup container,  
Bundle savedInstanceState) {  
// Inflate the layout for this fragment  
View layout = inflater.inflate(R.layout.fragment\_navigation\_drawer, container, false);  
mRecyclerView = (RecyclerView) layout.findViewById(R.id.drawerList);  
return layout;  
}
```

Pero no tan rápido, antes de correr nuestra aplicación nos falta crear un par de componentes más, un **Adapter** (un manejador lógico para los elementos de nuestra lista), ViewHolders y un **modelo** (representación de un elemento en la lista)

Pero antes, para tener todo más organizado, vamos a crear dos nuevos Package en nuestro proyecto, uno llamado **adapters** y otro **models**

[![Capture](/images/Capture-4.jpg)](http://www.alevsk.com/2016/01/tutorial-material-design-en-android-5/capture-5/)

Vamos a comenzar a pensar en [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) (Model View Controller), si bien no existe un estándar totalmente definido para utilizar **MVC en Android** podemos tomar el concepto y definir lo siguiente:

  * **Model:** Qué vamos a renderizar en la aplicación (objetos principales utilizados en los controladores)
  * **View:** Como lo vamos a renderizar (xml)
  * **Controller:** Eventos del ciclo de vida de las pantallas, manejar las entradas de usuario, definición de componentes de Android como el **RecyclerView**, etc.

## Creando un Modelo en Android

Teniendo lo anterior como premisa al momento de definir nuestro menú lo que necesitamos es una imagen que sirva como icono y un texto que sirva como título, procedemos a crear nuestra clase **Menu.java** en el **Package** models que definimos previamente

**Quicktip:** en nuestra clase primero definimos las propiedades de nuestro objeto (int icon, String title) y después para generar nuestros gets y sets usamos el shortcut “_alt + insert_" lo que desplegara un menú en donde elegimos **getters** and **settters** y marcamos todas las propiedades (variables) de nuestra clase.

[![Capture](/images/Capture-5.jpg)](http://www.alevsk.com/2016/01/tutorial-material-design-en-android-5/capture-6/)

```java
public class Menu {  
private int icon;  
private String title;

public int getIcon() {  
return icon;  
}

public void setIcon(int icon) {  
this.icon = icon;  
}

public String getTitle() {  
return title;  
}

public void setTitle(String title) {  
this.title = title;  
}  
}
```

## Creando un Adapter personalizado para el RecyclerView

Ahora en el **Package** adapters creamos una clase llamada MenuAdapter que extenderá o heredara sus metodos de **RecyclerView.Adapter**, el código inicialmente queda así.

```java
package com.alevsk.materialdesignapp.adapters;

import android.support.v7.widget.RecyclerView;  
import android.view.ViewGroup;

/**  
* Created by Alevskey on 23/01/2016.  
*/  
public class MenuAdapter extends RecyclerView.Adapter {  
@Override  
public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {  
return null;  
}

@Override  
public void onBindViewHolder(RecyclerView.ViewHolder holder, int position) {

}

@Override  
public int getItemCount() {  
return 0;  
}  
}
```

## Creando un ViewHolder personalizado

Ademas de eso también vamos a crear un ViewHolder, podemos definir la clase como una subclase de nuestro **MenuAdapter**, como siempre aquí tienen más documentación respecto a lo que vamos a utilizar [http://developer.android.com/reference/android/support/v7/widget/RecyclerView.ViewHolder.html](http://developer.android.com/reference/android/support/v7/widget/RecyclerView.ViewHolder.html)

Quedando el codigo final de la siguiente forma

[![Capture](/images/Capture-6.jpg)](http://www.alevsk.com/2016/01/tutorial-material-design-en-android-5/capture-7/)

Continuamos, Si leyeron la documentación acerca del comportamiento de los [Adapter](http://developer.android.com/reference/android/support/v7/widget/RecyclerView.Adapter.html) sabrán que por default manejan el tipo de objeto ViewHolder, pero nosotros acabamos de definir uno llamado MenuViewHolder que será el encargado de “contener" elementos como TextView, ImageView y todo lo que necesitemos para personalizar nuestro elemento de menú, sabiendo eso necesitamos realizar algunos cambios en nuestra clase, para empezar en la definición de nuestra clase vamos a definir (valga la redundancia) explícitamente que queremos utilizar **MenuViewHolder**

```java
public class MenuAdapter extends RecyclerView.Adapter<menuadapter.menuviewholder> {  
…  
..  
.
```

Ahora tenemos un montón de errores en la clase y esto es porque tenemos que modificar el tipo de objeto que retorna la función **onCreateViewHolder** de **RecyclerView.ViewHolder** a **MenuViewHolder**, también deberemos definir otra función llamada OnBindViewHolder, una vez realizados los cambios tenemos lo siguiente.

```java
public class MenuAdapter extends RecyclerView.Adapter<menuadapter.menuviewholder> {  
@Override  
public MenuViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {  
return null;  
}

@Override  
public void onBindViewHolder(MenuViewHolder holder, int position) {

}

@Override  
public int getItemCount() {  
return 0;  
}

class MenuViewHolder extends RecyclerView.ViewHolder {

public MenuViewHolder(View itemView) {  
super(itemView);  
}  
}  
}
```

Ahora vamos a crear la vista xml de nuestro item de Menu, en la carpeta layout creamos un archivo llamado **viewholder_menu.xml** que contendrá dos cosas, un **ImageView** y un **TextView**

```xml
<?xml version="1.0" encoding="utf-8"?>
<linearlayout android:layout\_height="match\_parent" android:layout\_width="match\_parent" android:orientation="horizontal" xmlns:android="http://schemas.android.com/apk/res/android">
<imageview android:id="@+id/listIcon" android:layout\_gravity="center\_vertical" android:layout_height="50dp" android:layout_width="50dp" android:padding="8dp" android:src="@drawable/dummy"></imageview>
<textview android:id="@+id/listText" android:layout\_gravity="center\_vertical" android:layout\_height="wrap\_content" android:layout\_width="wrap\_content" android:padding="8dp" android:text="@string/dummy_text"></textview>
</linearlayout>
```

La imagen @drawable/dummy es una imagen de ejemplo que yo utilice, ustedes pueden usar la que más les guste.

Regresamos a nuestro MenuAdapter.java y vamos a comenzar a utilizar los métodos que creamos anteriormente, primero vamos a crear un constructor para nuestro adapter, el cual recibirá un Context que nos servirá para hacer el binding de los elementos xml en nuestro ViewHolder, y una lista (de objetos Menu) que será la información con la cual llenaremos el RecyclerView después de eso vamos a realizar ese binding en el método onCreateView, tambien modificamos la función **getItemCount** para retornar el tamaño actual de la lista.

```java
private LayoutInflater mInflater;  
private List<menu> data = Collections.emptyList();

public MenuAdapter(Context context, List<menu> data) {  
mInflater = LayoutInflater.from(context);  
this.data = data;  
}

@Override  
public MenuViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {  
View view = mInflater.inflate(R.layout.viewholder_menu, parent, false);  
MenuViewHolder holder = new MenuViewHolder(view);  
return holder;  
}

@Override  
public int getItemCount() {  
return data.size();  
}
```

Ahora en la subclase MenuViewHolder vamos a definir el ImageView y TextView

```java
class MenuViewHolder extends RecyclerView.ViewHolder {  
ImageView icon;  
TextView title;  
public MenuViewHolder(View itemView) {  
super(itemView);  
title = (TextView) itemView.findViewById(R.id.listText);  
icon = (ImageView) itemView.findViewById(R.id.listIcon);  
}  
}
```

Ahora en el método onBindViewHolder es donde se realiza la acción de asignar los valores a las variables del MenuHolder (imágenes, textos, etc).

```java
public void onBindViewHolder(MenuViewHolder holder, int position) {  
holder.title.setText(data.get(position).getTitle());  
holder.icon.setImageResource(data.get(position).getIcon());  
}
```

Lo que hace nuestro método es recibir un holder, y una posición int, entonces con esa información de nuestra Lista de objetos Menu extraemos el titulo y el id de recurso de imagen que contiene el objeto Menu en la posición indicada de la lista, por ultimo hacemos set de esa información al TextView e ImageView del holder.

Venga ya falta poco, casi terminamos!!!

Me di cuenta que aún no hemos definido el tema de la app, lo he estado pensando y me gustaría enfocarla a un pequeño catálogo de anime que consuma la api opensource de [hummingbird](https://github.com/hummingbird-me/hummingbird/wiki/API-Reference), desarrollando un catálogo les poder enseñar a utilizar muchos más componentes que el ecosistema de Android nos ofrece, así como a consumir Apis e interactuar con las mismas, algo muy común en la industria de desarrollo de aplicaciones hoy en día.

Teniendo claro lo anterior las opciones de nuestro menú serán:

  * Buscar (buscador de anime)
  * Lo que estoy viendo (anime que el usuario ve actualmente)
  * Para más tarde (anime que el usuario tiene en la categoría de plan-to-watch)
  * Completado (series que el usuario ha terminado de ver)
  * Mi cuenta (información del usuario y anime favorito)

De ahí hay 3 opciones que solo pueden ser utilizados una vez el usuario haya sido autenticado en nuestra aplicación, pero eso lo dejaremos para más tarde, por ahora nos centraremos en desarrollar el menú.

Primero vamos a nuestro archivo **strings.xml** que se encuentra en **MaterialdesignApp > app > src > main > res > values > strings.xml** y ahi vamos a crear una lista de items que contendrá los elementos del menú

```xml
<string-array name="menu_list">
<item>Buscar</item>
<item>Lo que estoy viendo</item>
<item>Para mas tarde</item>
<item>Mi cuenta</item>
</string-array>
```

Buscamos en Internet algún set de iconos gratuitos y los incluimos a los recursos de nuestro proyecto en la carpeta **res > drawable** pues los necesitamos para el menu

```xml
<array name="menu_icons">
<item>@drawable/ic_search</item>
<item>@drawable/ic_eye</item>
<item>@drawable/ic_ticket</item>
<item>@drawable/ic_account</item>
</array>
```

## Cargando los datos al RecyclerView

En nuestro archivo **NavigationDrawerFragment.java** vamos a crear una nueva función llamada **getData()**, esta función será la encargada de leer la información estática que definimos en nuestro archivo strings.xml

```java
public List<menu> getData() {  
List<menu> menu = new ArrayList<menu>();  
TypedArray icons = getResources().obtainTypedArray(R.array.menu_icons);  
String[] labels = getResources().getStringArray(R.array.menu_list);

for(int i = 0; i < labels.length; i++) {  
Menu item = new Menu();  
item.setTitle(labels[i]);  
item.setIcon(icons.getResourceId(i,-1));  
menu.add(item);  
}

return menu;  
}
```

Lo que estamos haciendo en nuestra función es leer los títulos e imágenes (ids de recurso) y con ello estamos instanciando objetos Menu que a su vez agregamos a una lista que será devuelta por el método.

Finalmente en nuestra función onCreateView vamos a crear una nueva instancia de nuestro Adapter personalizado y se lo vamos a pasar al RecyclerView, también definiremos un objeto llamado **LayoutManager** para nuestro RecyclerView (asegúrate de definir el Adapter como una propiedad de tu clase)

```java
@Override  
public View onCreateView(LayoutInflater inflater, ViewGroup container,  
Bundle savedInstanceState) {  
// Inflate the layout for this fragment  
View layout = inflater.inflate(R.layout.fragment\_navigation\_drawer, container, false);  
mRecyclerView = (RecyclerView) layout.findViewById(R.id.drawerList);  
mAdapter = new MenuAdapter(getActivity(),getData());  
mRecyclerView.setAdapter(mAdapter);  
mRecyclerView.setLayoutManager(new LinearLayoutManager(getActivity()));

return layout;  
}
```

Corremos la aplicación en nuestro emulador o teléfono físico, abrimos el [NavigationDrawer][2] y vemos nuestro menú 🙂

[![recyclerview](/images/recyclerview.jpg)](http://www.alevsk.com/2016/01/tutorial-material-design-en-android-5/recyclerview/)

Eso es todo por ahora lectores, en el siguiente tutorial aprenderemos a aplicar color a los iconos utilizando **filtros** y a definir las acciones una vez que el usuario da Tap en un elemento del menú. Recuerden que el código de lo trabajado durante este tutorial lo pueden encontrar en el repositorio https://github.com/Alevsk/Material-design-en-Android  
salu2

 [1]: https://www.alevsk.com/?s=Material+Design+en+Android
 [2]: https://www.alevsk.com/2015/11/tutorial-material-design-en-android-4/
 [3]: http://developer.android.com/reference/android/support/v7/widget/RecyclerView.html</menu></menu></menu></menu></menu></menuadapter.menuviewholder></menuadapter.menuviewholder>
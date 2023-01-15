---
title: 'Tutorial Material Design en Android #1'
author: Alevsk
type: post
date: 2015-06-27T02:26:01+00:00
url: /2015/06/tutorial-material-desing-en-android-1/
categories:
  - Android
  - Programming
  - Technology
  - Tutorials
tags:
  - android
  - Java
  - material design
  - Programming
  - Solutions
  - Technology
  - Tutorials

---
## Los colores de la aplicación

En el tutorial anterior aprendimos a [Crear un nuevo proyecto de Android Material Design][1], hicimos algunas configuraciones en el archivo **AndroidManifest.xml** y creamos algunos nuevos estilos en el archivo **style.xml**.

Pues en esta ocasión vamos aprender a personalizar los colores de nuestra app, tanto del ToolBar / ActionBar como del StatusBar y los demás elementos de la interfaz gráfica. Recomiendo revisen la documentación oficial más a fondo en el siguiente [link](https://developer.android.com/training/material/theme.html#StatusBar)

Pero en resumen dice lo que explicare a continuación, básicamente tenemos 5 elementos que podemos personalizar por default:

  * colorPrimary
  * colorPrimaryDark
  * colorAccent
  * textColorPrimary
  * windowBackground
  * navigationBarColor

En la siguiente imagen podemos observar a que parte de la interfaz corresponde cada elemento 🙂

[![ThemeColors](/images/ThemeColors.png)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-1/themecolors/)

Ya se imaginan lo que sigue, les recomiendo las [paletas de colores de google](http://www.google.com.mx/design/spec/style/color.html#color-color-palette), por lo pronto elijamos la que sea y comencemos a configurar los valores en nuestra aplicación para ir viendo cómo va quedando.

Es una buena práctica separar los recursos que utilizara la aplicación en varios archivos por lo que dentro de la carpeta **values** vamos a crear un nuevo archivo **colors.xml**, si no recuerdan como crear un nuevo archivo de recursos regresen al primero tutorial donde creamos el archivo **styles.xml**.

Ya con el archivo **colors.xml** creado vamos a comenzar agregando los colores de nuestra elección, mi archivo quedo con el siguiente contenido.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<color name="primaryColor">#E91E63</color>
<color name="primaryColorDark">#C2185B</color>
<color name="colorAccent">#8BC34A</color>
</resources>
```

Y mis colores fueron: 

[![color_pallete](/images/color_pallete.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-1/color_pallete/)

Ahora en nuestro archivo **styles.xml** en donde hicimos la definición de nuestro Tema **AppTheme.Base** vamos a definir el uso de los colores que acabamos de crear 🙂 de la siguiente forma:

```xml
<resources>
<!--– Base application theme. –-->
<style name="AppTheme" parent="AppTheme.Base">  
<!– Customize your theme here. –>  
</style>
<style name="AppTheme.Base" parent="Theme.AppCompat.Light.DarkActionBar">  
<item name="colorPrimary">@color/primaryColor</item>  
<item name="colorPrimaryDark">@color/primaryColorDark</item>  
<item name="colorAccent">@color/colorAccent</item>  
</style>
</resources>
```

De la misma manera vamos a agregar esas definiciones de color de elementos en el otro archivo **styles.xml** (el que tenemos para dispositivos con api 21), quedando de la siguiente manera, noten que en estas definiciones estamos añadiendo el prefijo **android:** 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<!--– Base application theme. –-->
<style name="AppTheme" parent="AppTheme.Base">  
<item name="android:colorPrimary">@color/primaryColor</item>  
<item name="android:colorPrimaryDark">@color/primaryColorDark</item>  
<item name="android:textColorPrimary">@color/textColorPrimary</item>  
<item name="android:colorAccent">@color/colorAccent</item>  
</style>
</resources>
```

Corremos la app en nuestro emulador favorito y observamos los resultados 🙂

[![material_app](/images/material_app.jpg)](http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-1/material_app/)

En el siguiente tutorial vamos a aprender acerca del ToolBar y como personalizarla. salu2

 [1]: http://www.alevsk.com/2015/06/tutorial-material-desing-en-android-0/
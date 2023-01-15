---
title: Crear app universal para iPhone y iPad
author: Alevsk
type: post
date: 2012-07-18T01:29:10+00:00
url: /2012/07/crear-app-universal-para-iphone-y-ipad/
categories:
  - Mac
  - Tutorials
  - Tutorials-ios
tags:
  - Hello World
  - objective-c
  - Personal
  - Programming
  - Solutions
  - Technology
  - web

---
En este sencillo tutorial aprenderás a crear una app universal desde cero, las apps universales son aquellas que funcionan tanto en **iPhone** / **iPod** como en **iPad**.

Requisitos:

  * **Sistema Operativo:** Mac OSX 10.7.4
  * **IDE:** Xcode 4.2.1
  * **Conocimientos de Objective-c:** básicos, recomiendo leer esta guia de apple para tener nociones básicas sobre conceptos del lenguaje y la estructura de las apps [Your First iOS App](http://developer.apple.com/library/ios/#DOCUMENTATION/iPhone/Conceptual/iPhone101/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40007514-CH1-SW1)

Ok, lo primero que tenemos que hacer es abrir **Xcode** y crear un nuevo proyecto, nos vamos a **File** > **New** > **New Project** (como se muestra en la siguiente imagen)  
[![](/images/app-universal-1.png)](http://www.alevsk.com/2012/07/crear-app-universal-para-iphone-y-ipad/app-universal-1/)  
Nos aparecerá un menú en donde se nos pedirá elegir el tipo de aplicación que deseamos crear, elegimos **Empty Application**  
[![](/images/app-universal-2.png)](http://www.alevsk.com/2012/07/crear-app-universal-para-iphone-y-ipad/app-universal-2/)  
Aquí el proceso es bastante intuitivo, damos clic en siguiente y nos pedira un nombre para nuestra aplicación, yo le he puesto **universal**, en la opcion que dice **Device Family** asegurate de seleccionar **Universal** y de desmarcar las 3 opciones de abajo ya que en esta tutorial no las necesitamos.  
[![](/images/app-universal-3.png)](http://www.alevsk.com/2012/07/crear-app-universal-para-iphone-y-ipad/app-universal-3/)  
Nos preguntara en que lugar deseamos guardar el proyecto y listo, ahora si podemos comenzar a escribir código :).

Por default tenemos 2 archivo creados, **AppDelegate.h** y **AppDelegate.m**, lo primero que tenemos que hacer es abrir **AppDelegate.h** y añadir una nueva propiedad, un [UiViewController](http://developer.apple.com/library/ios/#documentation/uikit/reference/UIViewController_Class/Reference/Reference.html), lo hacemos con el siguiente código.

```obj-c
@property (strong, nonatomic) UIViewController * viewController;
```

Ten en cuenta que el código anterior lo debes de agregar entre @interface y @end quedando como resultado

```obj-c
@interface AppDelegate : UIResponder <uiapplicationdelegate>

@property (strong, nonatomic) UIWindow *window;  
@property (strong, nonatomic) UIViewController * viewController;

@end
```

Después tenemos que sintetizar los métodos accesores de nuestra propiedad, para ello vamos al **AppDelegate.m** y agregamos el siguiente código debajo de  
```obj-c
@synthesize window = _window;
```  
El resultado final es  
```obj-c
@synthesize window = _window;  
@synthesize viewController = _viewController;
```

Una vez hecho lo anterior ahora tenemos que crear una sub clase de UiViewController, para eso podemos dar clic derecho sobre nuestro proyecto y seleccionar **New File** o también en el menú de arriba nos vamos a File > New File, Xcode nos abrirá una ventana en donde tenemos que elegir del lado izquierdo (en la categoría de IOS  
) **Cocoa Touch** y seleccionar **UiViewController subClass** tal y como se muestra en la siguiente imagen.

[![](/images/app-universal-4.png)](http://www.alevsk.com/2012/07/crear-app-universal-para-iphone-y-ipad/app-universal-4/)

Después en la siguiente pantalla ponemos un nombre a la clase, yo he puesto **ScreenViewController**, nos aseguramos que sea una sub clase de UIViewController y por ultimo **desmarcamos** la opción de **With XIB for user interface**. Mas adelante verán el por que.

[![](/images/app-universal-5.png)](http://www.alevsk.com/2012/07/crear-app-universal-para-iphone-y-ipad/app-universal-5/)

Clic en Next después Save y listo. Ahora tenemos 2 nuevos archivos **ScreenViewController.h** y **ScreenViewController.m**, estos son los controladores de las vistas (las apps están basadas en **MVC**), ahora tenemos que crear las **View**, para eso de igual manera vamos a **File** > **New File**; del lado derecho en la categoria de **iOS** elegimos **User Interface** y seleccionamos View, como se muestra en la siguiente imagen.

[![](/images/app-universal-6.png)](http://www.alevsk.com/2012/07/crear-app-universal-para-iphone-y-ipad/app-universal-6/)

En la siguiente pantalla seleccionamos **iPhone** en la opción de **Device Family**, damos clic en Next, y pondremos como nombre de archivo el siguiente **ScreenViewController_iPhone** (el nombre tiene que ir así por convención), finalmente clic en Create.

Repetimos este ultimo paso pero ahora seleccionando iPad en la opción de Device Family y ponemos como nombre correspondiente al archivo **ScreenViewController_iPad**. Al final deberías tener los siguientes archivos en tu proyecto.

[![](/images/app-universal-7.png)](http://www.alevsk.com/2012/07/crear-app-universal-para-iphone-y-ipad/app-universal-7/)

Ahora tenemos que indicar el controlador de las vistas que acabamos de crear (los archivo XIB), para hacer eso damos clic primero en **ScreenViewController_iPhone**, seleccionamos en la categoría de los **Placeholders** el **File's Owner** y del lado derecho en el **identity inspector** nos vamos a la categoría de Custom Class y ponemos como clase **ScreenViewController**

[![](/images/app-universal-8.png)](http://www.alevsk.com/2012/07/crear-app-universal-para-iphone-y-ipad/app-universal-8/)

Después nos vamos al Connection inspector (la ultima opción de los Inspector) y “linkeamos" la view haciendo clic en el circulito de la derecha y arrastrando la línea azul (en la categoría de Outlets) con el view que esta en la categoría de Objects :), si lo hiciste bien debes de tener algo como lo siguiente.

[![](/images/app-universal-9.png)](http://www.alevsk.com/2012/07/crear-app-universal-para-iphone-y-ipad/app-universal-9/)

Hacemos exactamente lo mismo pero ahora con el archivo **ScreenViewController_iPad**

Ahora para poner algo de contenido de ejemplo creamos un **Label** centrado en cada una de las **Views** que contenga como texto el nombre del dispositivo desde donde se esta ejecutando la app, Hacemos clic en **ScreenViewController_iPhone**, elegimos **Label** de la lista de objetos (esquina inferior derecha) lo arrastramos al centro de la pantalla del dispositivo, damos doble clic y escribimos **iPhone**, exactamente lo mismo con **ScreenViewController_iPad** pero escribimos iPad en el objeto **Label**. Debemos de tener algo como esto.

[![](/images/app-universal-10.png)](http://www.alevsk.com/2012/07/crear-app-universal-para-iphone-y-ipad/app-universal-10/)

Listo hemos terminado con estos 2 archivos, ahora tenemos que regresar al **AppDelegate.m** y agregar una condicional donde se evalué el tipo de dispositivo desde donde estamos ejecutando la app y en base a eso cargar el **XIB** correspondiente, localizamos la siguiente clase en el archivo

```obj-c
– (BOOL)application:(UIApplication \*)application didFinishLaunchingWithOptions:(NSDictionary \*)launchOptions  
{  
self.window = [[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease];  
// Override point for customization after application launch.  
self.window.backgroundColor = [UIColor whiteColor];  
[self.window makeKeyAndVisible];  
return YES;  
}
```

Y agregamos las siguientes líneas justo debajo del comentario de // Override … bla bla bla

```obj-c
if ([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPhone) {  
\_viewController = [[UIViewController alloc] initWithNibName:@"ScreenViewController\_iPhone" bundle:nil];  
} else {  
\_viewController = [[UIViewController alloc] initWithNibName:@"ScreenViewController\_iPad" bundle:nil];  
}  
self.window.rootViewController = self.viewController;
```

Al final nuestra función debe de verse así.

```obj-c
– (BOOL)application:(UIApplication \*)application didFinishLaunchingWithOptions:(NSDictionary \*)launchOptions  
{  
self.window = [[[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]] autorelease];  
// Override point for customization after application launch.  
if ([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPhone) {  
\_viewController = [[[UIViewController alloc] initWithNibName:@"ScreenViewController\_iPhone" bundle:nil] autorelease];  
} else {  
\_viewController = [[[UIViewController alloc] initWithNibName:@"ScreenViewController\_iPad" bundle:nil] autorelease];  
}  
self.window.rootViewController = self.viewController;  
self.window.backgroundColor = [UIColor whiteColor];  
[self.window makeKeyAndVisible];  
return YES;  
}
```

Por ultimo corremos la app ya sea en los simuladores o en dispositivos físicos para ver los resultados :)!

[![](/images/app-universal-11.png)](http://www.alevsk.com/2012/07/crear-app-universal-para-iphone-y-ipad/app-universal-11/)

Y listo, espero haya quedado claro una de las tantas técnicas que existen para programar apps universales en iOS, esta vez solo utilizamos un Label que muestra un texto diferente dependiendo de si ejecutamos la aplicación en un iPhone o en un iPad, pero las posibilidades son infinitas y las ideas a desarrollar tan complejas como nosotros queramos :), incluso podrías programar una app que mostrara una interfaz diferente para cada día de la semana :p. Como siempre lo he dicho cualquier duda escríbanla en los comentarios y yo la responderé.

salu2

Puedes encontrar más guías y trucos sobre iPhone 5 en: [www.iPhone5ya.com][1]

 [1]: http://www.iPhone5ya.com "iphone5ya"</uiapplicationdelegate>
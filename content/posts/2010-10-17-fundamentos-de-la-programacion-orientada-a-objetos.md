---
title: Fundamentos de la programacion orientada a objetos
author: Alevsk
type: post
date: 2010-10-17T23:05:12+00:00
url: /2010/10/fundamentos-de-la-programacion-orientada-a-objetos/
categories:
  - Geek
  - Java
  - Programming
  - Technology
  - Tutorials
tags:
  - 2010
  - Hello world
  - Hello World
  - Java
  - Linux
  - Math
  - Programming
  - software libre
  - Solutions
  - Tutorials

---
Bueno hoy decidí darle una repasada a mis apuntes de Java, me costo encontrarlos :p, como una recapitulación de lo que ya había aprendido y para que no se me olvidara (bien dicen que lo que no se utiliza se olvida, extraño mi guitarra U.U) y para cambiarle un poquito también, ya como que pura programación web me empacho jeje.

Pues ¿que es la programación orientada a objetos?, es una metodología de desarrollo de software en la cual un programa es conceptual-izado como un grupo de objetos que trabajan en conjunto y esos objetos son creados a partir de clases, con esta imagen quedara mas claro, eso espero 😉

<p style="text-align: center;">
![Photobucket](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/diagrama_Poo.png)
</p>

Como las muñecas rusas, una **clase** contiene dentro **objetos** (que mas tarde son instanciados), los **objetos** a su vez contienen **métodos** (son las acciones que realiza el objeto), los **métodos** tienen **atributos**, después **declaración**, luego **expresiones** y al final **operadores** … mejor vean bien la imagen 🙂

Entonces para que quede mas claro, una clase es algo que engloba un grupo de objetos que tienen algo en común, por ejemplo “Caballo" hay diferentes tipos de caballos (Albino, Andaluz, Alter Real, Azteca, Dales) pero al final de cuentas todos son caballos, entonces podríamos decir que hay una **CLASE** _Caballo_ y que las diferentes _razas_ son sus **objetos** 🙂

Ahora veremos mas afondo los objetos, ya habíamos dicho que los objetos tienen **atributos** _(sus características que los definen individualmente)_ y **métodos** _(las acciones que realizan)_. Imaginemos que tenemos un **OBJETO** Jugador de Rugby que pertenece a una CLASE … bueno vean mejor la imagen.

<p style="text-align: center;">
![Photobucket](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/jugador_rugby.png)
</p>

Sus atributos (características) serian: peso, altura, edad, velocidad y sus métodos (las acciones que puede realizar) serian Patear, interceptar, correr, placar, lanzar, driblar, etc.

Resumiendo una clase puede tener tantos objetos como queramos, pero todos deben de tener algo en común, lean el ejemplo de los caballos mas arriba, y cada objetos tiene atributos y métodos, existen 2 tipos de cada cosa.

  * **Atributos Instancia:** Solo los tiene ese objeto en particular (una caracteristicas que solo tiene cierta raza de caballo)
  * **Atributos Clase:** los comparten todos los objetos (una caracteristica compartida por todas las razas de caballos)
  * **Métodos Instancia:** La acción que solo realiza ese objeto en particular (Una acción que solo puede realizar un cierto jugador del equipo de rugby como ser el capitán por ejemplo, solo hay un capitán)
  * **Métodos Clase:** Una acción que es compartida por todas las clases (una acción que que puede realizar cualquier jugador(Objeto) del equipo como pasar el balon
) 

Veamos algo de practica y no solo teoría 😉  
Hace tiempo hice un ejemplo del uso de **POO** básica acerca de unos robots, utilize para eso Netbeans.

Primero cree 2 clases: **_AplicacionRobot_** y **_RobotDante_**

codigo RobotDante.java

```GDScript
package robots;
class RobotDante
{
    //variables instancia, son los 3 atributos del robot
    String estatus;
    int velocidad;
    float temperatura;

    //crear primer comportamiento, primer metodo de instancia
    void comprobarTemperatura()
    {
        if(temperatura > 660)
        {
            estatus = "volviendo a casa";
            velocidad = 5;
        }
    }

    //crear segundo comportamiento, segundo método de instancia
    void mostrarAtributos()
    {
        System.out.println("Estatus: "+estatus);
        System.out.println("Velocidad: "+velocidad);
        System.out.println("Temperatura: "+temperatura);
    }
}

```

Vemos como creamos la clase RobotDante con todo y sus atributos, las variables estatus, velocidad y temperatura y también creamos 2 métodos (las acciones que puede realizar el objetos, en este caso el robot :)), el primer método es un control de temperatura (si se supone que es un robot de la nasa que explora volcanes x'D) y el segundo muestra sus atributos actuales (características del robot), después …

```Text only
package robots;
class AplicacionRobot
{
    public static void main(String[] args)
    {
       //Instanciar un nuevo objeto de la clase RobotDante, crear un nuevo robot :p
       RobotDante dante = new RobotDante();

       //darle valores a los atributos del robot(el objeto)
       dante.estatus = "Explorando ...";
       dante.velocidad = 2;
       dante.temperatura = 510;

       //llamar un metodo
       dante.mostrarAtributos();

       System.out.println("Incrementando la velocidad a 3");
       dante.velocidad = 3;

       //llamar un metodo
       dante.mostrarAtributos();

       System.out.println("Se detecto un aumento de temperatura a 670!");
       dante.temperatura = 670;

       //llamar un metodo
       dante.mostrarAtributos();

       System.out.println("Comprobando temperatura una vez mas ...");
       
       //llamar un metodo
       dante.comprobarTemperatura();
       dante.mostrarAtributos();
    }
}

```

Como java es un lenguaje totalmente enfocado a objetos siempre debemos comenzar con una clase, pero esta en particular tiene el método **main** que es por donde comenzara a ejecutarse el programa y a partir de ahí instanciar las demás clases (instanciar se escucha bonito pero no es mas que crear los objetos), creo que el código esta bien explicado, de todas maneras si sobran algunas dudas, son bienvenidas en los comentarios, así como sugerencias y criticas constructivas 😀

<div class="demobox">
[![descargar](http://www.alevsk.com/wp-content/themes/ModernStyle//images/download.png)](http://www.megaupload.com/?d=HUCCETYB)
</div>

Y por ultimo quiero hacerle una felicitación al profesor Jesús Conde [@0utkast][1] en internet por que prácticamente todo lo que se de internet lo he estado aprendiendo a travez de sus métodos de enseñanza y de sus videtutoriales, enseñando a la gente a ser autodidacta 😉

Salu2

 [1]: https://twitter.com/0utkast
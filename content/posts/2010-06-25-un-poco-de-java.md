---
title: Un poco de Java
author: Alevsk
type: post
date: 2010-06-25T04:10:47+00:00
url: /2010/06/un-poco-de-java/
image:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/java.jpg
slider_thumbnail:
  - http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/thumb-java.jpg
categories:
  - Java
  - Programming
tags:
  - Java
  - matematicas
  - Math
  - Programming

---
Bueno termine mi trabajo por hoy y quise ver una película, entonces un amigo de la escuela me hablo que si podía checar un código en java, hacia mucho que no tocaba ese lenguaje como un mes jeje, pero le dije que sip, y al ultimo termine yo también empapándome de java, es código básico pero sirve para estar al tiro jeje, aquí les dejo como quedo al ultimo.

Lo que hace es encontrar el numero de triples pitagóricos en la serie del 1 al 500, se puede modificar mas el programa para que el user ponga el rango pero así lo quise dejar ^^

Primero que nada que es la triple pitagorica, bueno se acuerdan del teorema de pitagoras, pues una triple pitagorica es la equivalencia de a<sub>2</sub> + b<sub>2</sub> = c<sub>2</sub> por ejemplo: 4<sub>2</sub> + 3<sub>2</sub> = 5<sub>2</sub>
<!--more-->
```Transact-SQL
public class Main { 

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
         int contador=0;
         int respuesta=0;
         int respuesta2=0;

         for(int a=1;a<=500;a++)
         {
            for(int b=2;b<=500;b++)
            {
                for(int c=1;c<=500;c++)
                {
                    respuesta=(a*a)+(b*b);
                    respuesta2= c*c;
                     if(respuesta==respuesta2)
                    {
                         contador++ ;
                         System.out.println(""+a+"^2 + "+b+"^2 = "+c+"^2");
                    }
              }
          }

    }
         System.out.println("El numero de triples pitagóricas fue: "+contador);

}
                }

```

salu2
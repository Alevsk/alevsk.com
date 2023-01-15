---
title: Los 5 errores mas comunes cuando se programa en C
author: Alevsk
type: post
date: 2012-06-24T19:01:59+00:00
url: /2012/06/los-10-errores-mas-comunes-cuando-se-programa-en-c/
categories:
  - C y C++
  - Programming
  - Tips

---
He hecho una recopilación de algunos de los errores mas comunes que la gente comete a la hora de **programar en C**, el **lenguaje C** aunque es muy poderoso es bastante inflexible a diferencia de otros lenguajes de tipado sencillo como PHP por ejemplo :), sin embargo son obvias las ventajas que nos aporta C frente a los demás lenguajes, podemos comenzar diciendo que C ha sido el padre de varios lenguajes :)!.

## 1.- Sintaxis de comentarios incompletos

```Text only
a = b; /* el comentario no termina
c = d; /* c = d se incluye en el comentario */

```

Por lo tanto c = d no se ejecutara

## 2.- Declaraciones accidentales / declarar booleanos accidentalmente

```Text only
f(a = b) c; /* a tomara el valor de b, en lugar de ser comparado */

```

El valor de b sera asignado a “a", en lugar de ser comparado, debido a que a != 0 entonces c se ejecutara. Otro caso similar podría ser también

```Tera Term macro
if( a =! b) c; /* esto es compilado como (a = !b) */

```

En lugar de (a != b) o (a == !b).

## 3.- Hacer mal uso de las macros en C

```verilog
#define assign(a,b) a=(char)b
assign(x,y>>8)

/* Lo anterior es compilado como */ 
x = (char) y >> 8    /* Probablemente no es lo que queríamos */

```

## 4.- Archivos de cabecera que no coinciden

Supongamos que tenemos un archivo foo.h que contiene las siguientes instrucciones

```Text only
struct foo { BOOL a};

```

Además tenemos otros 2 archivos f1.c y f2.c donde hacemos un include a ese archivo de cabecera.

```C
/* F1.c  contiene*/
#define BOOL char
#include "foo.h"

/* F2.c contiene*/
#define BOOL int
#include "foo.h"

```

f1.c y f2.c difieren acerca del atributo principal de la estructura foo.

[![](/images/3pue0v.jpg)](http://www.alevsk.com/2012/06/los-10-errores-mas-comunes-cuando-se-programa-en-c/3pue0v/)

## 5.- Valores de retorno fantasma

Suponemos que tenemos el siguiente código:

```Tera Term macro
int foo (a)
 { 
    if (a) return(1); 
 } 
/* Esta mal, ya que en algunos casos no retornara ningún valor */

```

Este es el típico caso donde no conceptualizamos todos los posibles casos y nos hace falta implementar valores de retorno.

Finalmente no esta de mas decir que con las nuevas arquitecturas de 64 bits, hay nuevas formas de cometer errores cuando programamos en C, especialmente cuando se trabaja con matrices que se acercan o superan los 2 ^ 31 elementos (aunque es bastante raro).

Existen muchos mas errores que podemos cometer, algunos son verdaderamente difíciles de ocasionar pero pueden llegar a suceder, sobre todo los que tienen que ver con el compilador xD.  
Para una lista mas detallada de errores pueden visitar el siguiente sitio [The Top 10 Ways to get screwed by the “C" programming language][1]

 [1]: http://www.andromeda.com/people/ddyer/topten.html
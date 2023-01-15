---
title: '#DailyCodingProblem: El producto de todos los elementos en el arreglo menos el elemento actual'
author: Alevsk
type: post
date: 2018-09-05T06:21:13+00:00
url: /2018/09/dailycodingproblem-el-producto-de-todos-los-elementos-en-el-arreglo-menos-el-elemento-actual/
categories:
  - Geek
  - Java
  - Personal
  - Problem Solving
  - Programming
  - Snippets
  - Technology
  - Tips
  - Tutorials
tags:
  - algoritmos
  - computer science
  - daily coding problems
  - data structures
  - problem solving
  - Programming

---
[![](/images/050718_EC_numbers_feat.jpg)](https://www.alevsk.com/2018/09/dailycodingproblem-el-producto-de-todos-los-elementos-en-el-arreglo-menos-el-elemento-actual/050718_ec_numbers_feat/)

> [https://www.dailycodingproblem.com/](https://www.dailycodingproblem.com/)
> 
> Good morning! Here's your coding interview problem for today.
> 
> This problem was asked by Uber.
> 
> Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
> 
> For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
> 
> Follow-up: what if you can't use division?

Si ignoramos la restricción este problema es muy sencillo de resolver.

  * Iteramos el arreglo y calculamos el producto total de todos los elementos: **1 x 2 x 3 x 4 x 5** = **120**
  * Iteramos nuevamente dividiendo el total entre cada uno de los elementos y guardamos esos resultados en nuevo arreglo: **120/1, 120/2, 120/3, 120/4, 120/5**

La complejidad de esta solución seria **O(2n)** o simplemente **O(n)**, pero debido a que el problema dice que no podemos usar la división las cosas se complican un poco mas.

## Solución cuadrática

Sin usar la división la solución mas obvia es una solución cuadrática, iteramos el arreglo y por cada elemento vamos a ir acumulando el producto de esos valores menos el elemento **i** actual. 

```java
int[] calculateProduct(int[] numbers) {  
int[] result = new int[numbers.length];  
// …  
// … logica para inicializar todos los valores de result en 1  
// …  
for (int i = 0; i < numbers.length; i += 1) {  
for (int j = 0; j < numbers.length; j += 1) {  
if (i != j) {  
result[j] *= numbers[i];  
}  
}  
}  
return result;  
}
```

Esta solución es muy fácil de entender pero no es para nada eficiente, **O(n<sup>2</sup>)**, en la publicación anterior ya analizábamos otra [solución cuadrática](https://www.alevsk.com/2018/09/daily-coding-problem/) y veíamos que era un problema con inputs de datos muy grandes, por ejemplo un arreglo de 1000 elementos (1 millón de operaciones).

## Solución en tiempo lineal con programación dinámica

Después de pensar un rato en este problema, haciendo algunas anotaciones y viendo la relación entre los indices y el producto parcial de cada uno de ellos llegue a la siguiente solución.

[![](/images/Screen-Shot-2018-09-05-at-12.46.38-AM.png)](https://www.alevsk.com/2018/09/dailycodingproblem-el-producto-de-todos-los-elementos-en-el-arreglo-menos-el-elemento-actual/screen-shot-2018-09-05-at-12-46-38-am/)

La primera fila son los valores del arreglo, después como si estuviéramos iterando, el valor actual es marcado en color amarillo, si pudiéramos obtener el producto acumulado de izquierda y derecha de cada uno de los elementos entonces podríamos resolver el problema multiplicándolos entre si 🙂

Ejemplo: para el obtener el resultado del **3** tendríamos que multiplicar sus valores de la izquierda que son **2** y sus valores de la derecha que son **20** dando como resultado **40**.

Vamos a recorrer el arreglo por la izquierda y por la derecha guardando el producto de sus elementos, para eso necesitaremos 2 arreglos mas, **left** y **right**, podemos hacer esos recorridos en una sola iteración, después iteramos nuevamente multiplicando los valores de izquierdo y derecho de **result[i]**.

```java
public static int[] calculateProduct(int[] numbers) {  
int[] result = new int[numbers.length];  
int[] left = new int[numbers.length];  
int[] right = new int[numbers.length];  
int totalLeft = 1;  
int totalRight = 1;  
int size = numbers.length – 1;  
for (int i = 0; i <= size; i += 1) {  
totalLeft *= numbers[i];  
totalRight *= numbers[size – i];  
left[i] = totalLeft;  
right[size – i] = totalRight;

}  
for (int i = 0; i < numbers.length; i += 1) {  
if (i == 0) {  
result[i] = right[i + 1];  
} else if (i == numbers.length – 1) {  
result[i] = left[i – 1];  
} else {  
result[i] = left[i – 1] * right[i + 1];  
}  
}  
return result;  
}
```

La complejidad en tiempo de esta solución es **O(2n)** o **O(n)**.  
La complejidad en espacio de esta solución es **O(3n)** o **O(n)**, (tomando en cuenta solamente los 3 nuevos arreglos que necesitamos, todas las demás variables son espacio constante).

Happy hacking 🙂
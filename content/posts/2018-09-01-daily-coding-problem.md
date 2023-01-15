---
title: '#DailyCodingProblem: Encontrar si dos números dentro de un arreglo suman K'
author: Alevsk
type: post
date: 2018-09-01T17:13:22+00:00
url: /2018/09/daily-coding-problem/
categories:
  - Geek
  - Java
  - Personal
  - Problem Solving
  - Programming
  - Tips
  - Tutorials
tags:
  - algorithms
  - computer science
  - daily coding problems
  - data structures
  - Java
  - problem solving

---
[![](/images/cspr_0601.png)](https://www.alevsk.com/2018/09/daily-coding-problem/cspr_0601/)

> [https://www.dailycodingproblem.com/](https://www.dailycodingproblem.com/)
> 
> Good morning! Here's your coding interview problem for today.
> 
> This problem was recently asked by Google.
> 
> Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
> 
> For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
> 
> Bonus: Can you do this in one pass?

Como el problema lo indica, debemos crear una función que reciba 2 parámetros, un arreglo de números y un numero entero **k**, debemos buscar dentro de ese arreglo si dos elementos sumados entre si son iguales al numero **k**.

La solución **naive** para este problema seria iterar sobre los elementos del arreglo y por cada uno de ellos iterar nuevamente para ver si la suma de **numbers[i]** + **numbers[j]** da como resultado el numero **k**

```java
for (int i = 0; i < numbers.length; i += 1) {  
for (int j = 0; j < numbers.length; j += 1) {  
// evitamos la comparación de un elemento consigo mismo  
if (i != j && (numbers[i] + numbers[j]) == k) {  
return true;  
}  
}  
}
```

Esta solución no es muy buena ya que por cada elemento en el arreglo vamos a iterar nuevamente los datos, resultando en una complejidad **O(n<sup>2</sup>)** donde **n** es el tamaño del arreglo, imagina un arreglo de 1000 elementos, tendríamos que realizar 1 millón de operaciones.

## Solución lineal para encontrar si dos números suman K

Vamos a iterar el arreglo, pero esta vez vamos a usar un [HashSet](https://www.geeksforgeeks.org/hashset-in-java/) para guardar información, por cada elemento:

  * Calculamos el numero que falta para completar el total **k**
  * Revisamos si el numero que nos falta existe en el **HashSet**, si es así devolvemos **true** (buscar elementos en un HashSet se hace en tiempo constante)
  * Si el numero que buscamos no existe entonces registramos el numero actual como “observado" en el **HashSet**

Si terminamos de recorrer el arreglo significa que no hay números que sumados nos den como resultado **k** y por lo tanto devolvemos **false**.

```java
public static boolean findSum(int[] numbers, int k) {  
HashSet<integer> seenNumbers = new HashSet<>();  
for (int i = 0; i < numbers.length; i += 1) {  
int missing = k – numbers[i];  
if (seenNumbers.contains(missing)) {  
return true;  
}  
seenNumbers.add(numbers[i]);  
}  
return false;  
}
```

La complejidad en tiempo de esta solución es **O(n)**, ya que el numero de operaciones a realizar depende directamente del tamaño del arreglo n.

La complejidad en espacio de esta solución también es **O(n)**, el espacio o la memoria a utilizar depende directamente de lo que reciba la función, en este caso un arreglo de n elementos, utilizamos un HashSet para almacenar máximo el mismo numero de elementos y no realizamos otras operaciones que sean significativas con la memoria.

Happy hacking 🙂</integer>
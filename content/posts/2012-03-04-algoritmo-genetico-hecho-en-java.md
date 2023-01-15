---
title: Algoritmo genético hecho en Java
author: Alevsk
type: post
date: 2012-03-04T18:42:07+00:00
url: /2012/03/algoritmo-genetico-hecho-en-java/
categories:
  - Java
  - Programming
  - Snippets
  - Technology
  - Tutorials
tags:
  - Java
  - Programming
  - Solutions
  - Technology

---
[![](/images/La-evolución-de-los-gamers.jpg)](http://www.alevsk.com/2012/03/algoritmo-genetico-hecho-en-java/la-evolucion-de-los-gamers/)  
Ha pasado bastante tiempo desde que no publico algún código mío, esta vez quiero compartir con ustedes un **algoritmo genético hecho en Java** que tuve que hacer para mi clase de **Sistemas Inteligentes** 😀 en el modulo de **computación evolutiva**, para los que no sepan que es un algoritmo genético, por [aca][1] tienen mas información.

El problema resuelto fue el problema del viajante o [TSP][2], nuestro problema consiste básicamente en que tenemos n ciudades, que están conectadas entre si, todas con todas (n*n caminos) y existen varios objetivos, en mi caso tengo que minimizar la distancia recorrida.

Los pasos de todo algoritmo genético deben de ser

  * Generar población
  * Seleccionar a los individuos mas aptos (Torneo, selección por ruleta, etc)
  * Cruzarlos ([recombinacion][3])
  * Mutación

Esto se realiza durante n generaciones y el objetivo es que cada generación los individuos sean mejores que los anteriores (aunque no siempre es así xD). Ahora les muestro un ejemplo de como es que funciona, supongamos que generamos nuestra población inicial la cual consiste en un camino que tiene que tomar el viajante, tiene como restricción que no puede repetir ciudades por las que ha pasado antes y el recorrido termina en la ciudad de la que partimos, ejemplo:

```Text only
Batemans-Bay-Outreach	Ashfield	Bateau-Bay	Bankstown	Armidale	Blackett	Bega	| Bathurst	Bidwill	| Bradbury Airds	Albury	Batemans-Bay-Outreach	120.68747174103011
```

Podemos ubicar las ciudades en un plano cartesiano y verlas como si fueran puntos, desde esa perspectiva es posible sacar la distancia total del recorrido aplicando [distancia euclidiana][4] entre los puntos.

Después de eso podemos realizar una selección, entre los métodos mas comunes están el de  [selección por ruleta][5] o el de  [selección por torneo][6], en este ultimo tan solo tenemos que ordenar la lista de caminos de menor a mayor y en mi caso elegir n * 3 individuos que representaran a los padres de la siguiente generación, ahora, en este punto es importante saber cuales tenemos que elegir ya que en probabilidad es poco posible que si cruzamos los 2 individuos mejor adaptados de la generación salga uno aun mas adaptado, por el contrario podría “des evolucionar" el hijo, es por eso que yo recomiendo, si vemos la población como si estuviera ordenada en una pila, tomar de los de arriba (los mejores adaptados) y algunos de en medio.

En este punto ya tenemos a los que serán los padres, ahora debemos de cruzarlos, existen varias técnicas de cruza como recombinación en 1 punto, recombinación en 2 puntos, corte y empalme, Recombinación uniforme y uniforme media y Recombinación de cromosomas ordenados, mas información [aqui][3].

En mi caso yo utilice recombinación en 2 puntos y después aplique un algoritmo de mi creación para corregir el camino en caso de que hubiera ciudades repetidas en el.

```ActionScript 3
minCutPoint: 6 maxCutPoint: 9

Padres:

Batemans-Bay-Outreach	Ashfield	Bateau-Bay	Bankstown	Armidale	Blackett	Bega	| Bathurst	Bidwill	| Bradbury Airds	Albury	Batemans-Bay-Outreach	120.68747174103011
Airds	Bankstown	Albury	Armidale	Ashfield	Batemans-Bay-Outreach	Bathurst	    | Bega	Bateau-Bay	| Bidwill	Bradbury	Blackett	Airds	122.0081148734119

Hijos sin verificar:
Batemans-Bay-Outreach	Ashfield	Bateau-Bay	Bankstown	Armidale	Blackett	Bega	| Bega	Bateau-Bay	| Bradbury	Airds	Albury	Batemans-Bay-Outreach	0.0
Airds	Bankstown	Albury	Armidale	Ashfield	Batemans-Bay-Outreach	Bathurst	    | Bathurst	Bidwill	| Bidwill	Bradbury	Blackett	Airds	0.0


F1Extract = | Bathurst	Bidwill	|
F2Extract = | Bega	Bateau-Bay	|

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Cruza hijo 1:

Batemans-Bay-Outreach	Ashfield	Bateau-Bay	Bankstown	Armidale	Blackett	Bega	    | Bega	Bateau-Bay	| Bradbury	Airds	Albury	Batemans-Bay-Outreach	0.0

Batemans-Bay-Outreach	Ashfield	Bateau-Bay	Bankstown	Armidale	Blackett	Bathurst	| Bega	Bateau-Bay	| Bradbury	Airds	Albury	Batemans-Bay-Outreach	0.0

Batemans-Bay-Outreach	Ashfield	Bidwill	Bankstown	Armidale	Blackett	Bathurst	    | Bega	Bateau-Bay	| Bradbury	Airds	Albury	Batemans-Bay-Outreach	0.0

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Cruza hijo 2:

Airds	Bankstown	Albury	Armidale	Ashfield	Batemans-Bay-Outreach	Bathurst  | Bathurst	Bidwill	| Bidwill	Bradbury	Blackett	Airds	0.0

Airds	Bankstown	Albury	Armidale	Ashfield	Batemans-Bay-Outreach	     Bega	| Bathurst	Bidwill	| Bidwill	Bradbury	Blackett	Airds	0.0

Airds	Bankstown	Albury	Armidale	Ashfield	Batemans-Bay-Outreach	     Bega	| Bathurst	Bidwill	| Bateau-Bay	Bradbury	Blackett	Airds	0.0
```

Aqui lo que hago es generar aleatoriamente 2 puntos de corte (minCutPoint y maxCutPoint), las ciudades entre esos 2 puntos serán los cromosomas que se insertaran en los hijos, después de eso checamos cada uno de los [alelos][7] para verificar que no esta repetido, en caso de que asi sea, remplazo la ciudad repetida por la primera ciudad no repetida del conjunto de cromosomas original del padre, lo que me asegura que siempre tendre caminos validos 🙂

Y por ultimo pero no menos importante la mutación, esta parte es bastante sencilla, genero 2 puntos aleatorios e intercambio los cromosomas de lugar, si el camino resultante es mas optimo que el original entonces el individuo evolucionara, de lo contrario se quedara igual.

Este procedimiento se realiza n generaciones, y al final esperamos tener el camino mas optimo que el viajero podría tomar.

Les dejo mi codigo fuente, espero le sirva a alguien

  * [mainInterface.java](https://github.com/Alevsk/Java-Genetic-Algorithm/blob/master/src/com/alevsk/genetico/mainInterface.java)
  * [GeneticsAlgorithm.java](https://github.com/Alevsk/Java-Genetic-Algorithm/blob/master/src/com/alevsk/genetico/GeneticsAlgorithm.java)
  * [City.java](https://github.com/Alevsk/Java-Genetic-Algorithm/blob/master/src/com/alevsk/genetico/City.java)
  * [Path.java](https://github.com/Alevsk/Java-Genetic-Algorithm/blob/master/src/com/alevsk/genetico/Path.java)

salu2

PD cualquier duda postearla en comentarios, gracias

 [1]: http://es.wikipedia.org/wiki/Algoritmo_gen%C3%A9tico
 [2]: http://en.wikipedia.org/wiki/Travelling_salesman_problem
 [3]: http://es.wikipedia.org/wiki/Sobrecruzamiento_%28computaci%C3%B3n_evolutiva%29
 [4]: http://es.wikipedia.org/wiki/Distancia_euclidiana
 [5]: http://sabia.tic.udc.es/mgestal/cv/AAGGtutorial/node10.html
 [6]: http://sabia.tic.udc.es/mgestal/cv/AAGGtutorial/node11.html
 [7]: http://es.wikipedia.org/wiki/Alelo
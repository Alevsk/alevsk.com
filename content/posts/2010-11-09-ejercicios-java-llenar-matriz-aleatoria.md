---
title: 'Ejercicios Java: Llenar Matriz aleatoriamente'
author: Alevsk
type: post
date: 2010-11-09T21:49:54+00:00
url: /2010/11/ejercicios-java-llenar-matriz-aleatoria/
categories:
  - Java
  - Programming
  - Tutorials
tags:
  - Storage
  - Hello world
  - Java
  - Programming
  - software libre
  - Tutorials

---
![Java Blog 2.0](/images/web.gif)

Este es un ejemplo hecho en Java sobre llenar una Matriz con numeros aleatorios en la que el usuario escribe un numero y el programa devuelve como respuesta sí el numero esta en la matriz y sí se encuentra, cuantas veces aparece.

Usando solo metodos (funciones) sin meternos a Programacion Orientada a Objetos y la libreria Swing, Util y IO.

Analizen el codigo y si tienen dudas comenten 🙂

```Python
import java.io.*;
import java.util.*;
import javax.swing.*;
public class matrizAleatoria {
	public static void llenarMatriz(int n)
	{
		int[][] matriz = new int[5][5];
		Random rnd = new Random();
		int columnas = matriz.length;
		int filas = matriz[0].length;
		int i = 0, coincidencias = 0;
		boolean encontro = false;
		//Llenado de la matriz
		for(i = 0; i < filas; i++)
		{
			for(int j = 0; j < columnas; j++)
			{
				matriz[i][j] = (int)(rnd.nextDouble() * 10.0);
			}
		}
		//Busqueda del numero
		for(i = 0; i < filas; i++)
		{
			for(int j = 0; j < columnas; j++)
			{
				if(n == matriz[i][j])
				{
					encontro = true;
					coincidencias++;
				}
			}
		}
		if(encontro == true)
		{
			JOptionPane.showMessageDialog(null, "EL numero "+n+" se encontro "+coincidencias+" veces", "Si se encontro el numero", JOptionPane.INFORMATION_MESSAGE);
		}
		else
		{
			JOptionPane.showMessageDialog(null, "El numero "+n+" no se encontro", "No se encontro el numero", JOptionPane.INFORMATION_MESSAGE);
		}
	}
	public static void main(String[] args)throws IOException
	{
		int n;
		n = Integer.parseInt(JOptionPane.showInputDialog("Escribe un numero que piensas que esta en la matriz"));
		llenarMatriz(n);
	}
}

```
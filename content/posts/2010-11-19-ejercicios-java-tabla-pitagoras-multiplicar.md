---
title: 'Ejercicios Java: Tabla de pitagoras'
author: Alevsk
type: post
date: 2010-11-19T14:53:15+00:00
url: /2010/11/ejercicios-java-tabla-pitagoras-multiplicar/
categories:
  - Java
  - Personal
  - Programming
  - Tutorials
tags:
  - CSS
  - Hello world
  - Hello World
  - Java
  - Javascript
  - Linux
  - Math
  - Programming
  - Social Media
  - software libre
  - Solutions
  - Tutorials

---
![](/images/css-blocks.gif)

Este es el programa que nos dejaron hacer en el tercer parcial, una aplicacion que mostrar la tabla de pitagoras y si el usuario daba un numero mostrar la tabla de ese numero nada mas.

```Python
import java.io.*;
import javax.swing.*;

public class tablasMultiplicar {
int[][] tabla = new int[10][10];
int columnas = tabla.length;
int filas = tabla[0].length;

	void llenarMatriz()
	{
		int i = 0, j = 0;
		
		//Llenar en horizontal y vertical
		for(i = 0;i < filas; i++)
		{
			tabla[0][i] = i+1;
			tabla[i][0] = i+1;
		}
		
		for(i = 1;i < filas; i++)
		{
			for(j = 1; j < columnas; j++)
			{
				tabla[i][j] = tabla[0][j] * tabla[i][0];
			}
			
		}
	}
	
	void imprimirMatriz(int n)
	{
		int i = 0, j = 0;
		String matrizArray = "";
		
		//imprimir matriz completa
		if(n == 0)
		{
			for(i = 0;i < filas; i++)
			{
				for(j = 0; j < columnas; j++)
				{
					//Para que la matriz se vea mas bonita
					if(tabla[i][j] >= 10)
					{
						matrizArray = matrizArray+"["+tabla[i][j]+"]   ";
					}
					else
					{
						matrizArray = matrizArray+"["+tabla[i][j]+"  ]   ";
					}
					
				}
				//System.out.print("\n");
				matrizArray = matrizArray+"\n\n";
			}
			JOptionPane.showMessageDialog(null, matrizArray, "Toda la tabla de multiplicar", JOptionPane.INFORMATION_MESSAGE);
		}
		else
		
		//Imprimir solo una tabla de multiplicar
		if(n > 0 && n <= 10)
		{
			for(i = 0;i < filas; i++)
			{
				//matrizArray = matrizArray+"["+tabla[n-1][i]+"]";
				matrizArray = matrizArray+(n)+" * "+(i+1)+"    = "+tabla[n-1][i]+"\n";
			}
			JOptionPane.showMessageDialog(null, matrizArray, "Tabla del numero: "+n, JOptionPane.INFORMATION_MESSAGE);
		}
		else
		{
			JOptionPane.showMessageDialog(null, "Ese numero esta fuera de rango de 1 - 0", "#FAIL", JOptionPane.INFORMATION_MESSAGE);
		}
	}
	

	public static void main(String[] args) throws IOException
	{
		int n;
		String opc = "";
		tablasMultiplicar matriz = new tablasMultiplicar();
		matriz.llenarMatriz();
		
		JOptionPane.showMessageDialog(null, "Programa que muestra la tabla de pitagoras", "Programa Chido", JOptionPane.INFORMATION_MESSAGE);
		
		do
		{
			opc = JOptionPane.showInputDialog("0 = Mostrar toda la tabla\nEscribe un numero 1-10 para consultar esa tabla nada mas\nEscribre SALIR para terminar el programa");
			opc = opc.toUpperCase();
			if(opc.equals("SALIR"))
			{
				JOptionPane.showMessageDialog(null, "Gracias por usar el programa", "Gracias!", JOptionPane.INFORMATION_MESSAGE);
				break;
			}
			
			n = Integer.parseInt(opc);
			matriz.imprimirMatriz(n);
			
		}while(!opc.equals("salir"));		
	}

}

```

salu2
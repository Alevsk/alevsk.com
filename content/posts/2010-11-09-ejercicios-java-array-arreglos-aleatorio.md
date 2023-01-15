---
title: 'Ejercicios Java: Juego encontrar el numero en un array'
author: Alevsk
type: post
date: 2010-11-09T22:12:42+00:00
url: /2010/11/ejercicios-java-array-arreglos-aleatorio/
categories:
  - Java
  - Personal
  - Programming
  - Tutorials
tags:
  - Hello world
  - Hello World
  - Java
  - Personal
  - Programming
  - Tutorials
  - web

---
![Arreglos Java](/images/array_banner.jpg)

El juego funciona de la siguiente manera: se genera un array con 10 numeros aleatorios y el usuarios tiene que adivinar uno de esos numeros en maximo 3 intentos.

Es otro ejercicio que nos dejaron en Java hace tiempo, igual lo subo por si ha alguien le sirve y si surge alguna duda favor de comentar 🙂  
_  
Nota: Estoy viendo que al parsear el codigo con el plugin del wordpress, se agrega codigo extra que puede generar errores al compilar, pero confio en que los programadores de Java lo arreglaran y lo haran funcionar 🙂_

```Python
import java.io.*;
import java.util.*;
import javax.swing.*;

public class adivinaElNumero {
//variables de clase
int[] numeros = new int[10];
Random rnd = new Random();
int opc = 0;
boolean volvioMenu = false;
boolean descubrioNumero = false;
static final int OPORTUNIDADES = 3;
BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
	void llenarArray()
	{
		for(int i = 0; i < numeros.length; i++)
		{
			numeros[i] = (int)(rnd.nextDouble() * 50.0);
		}
	}
	void elegir()
	{
		int n = 0,j = 0,i = 0,cont = 1;
		String numsArray = "";
		do
		{
			if(volvioMenu == true)
			{
				opc = Integer.parseInt(JOptionPane.showInputDialog("==[Menu]==\n [1]Jugar [2]Ver instrucciones [3]Salir"));
			}

			switch(opc)
			{
				case 1:
					JOptionPane.showMessageDialog(null, "Ok, el array ha sido llenado aleatoriamente\ncon numeros del 1 - 50 tienes 3 intentos para adivinar uno de esos numeros", "Jugando", JOptionPane.INFORMATION_MESSAGE);
					for(j = 1; j <= OPORTUNIDADES; j++ )
					{
						n = Integer.parseInt(JOptionPane.showInputDialog(null,"Escribe un numero ... esta es tu "+j+" oportunidad"));
						for(i = 0; i < numeros.length; i++)
						{

							if(n == numeros[i])
							{
								descubrioNumero = true;
								break;
							}
							if(cont <= numeros.length)
							{
								numsArray = numsArray+"["+numeros[i]+"]";
								cont++;
							}
						}

						if(descubrioNumero == true)
						{
							break;
						}
					}

					if(descubrioNumero == true)
					{
						JOptionPane.showMessageDialog(null, "Felicidades!\nEl numero que escribiste ("+n+") estaba en la pocicion ["+i+"] del array", "Felicidades", JOptionPane.INFORMATION_MESSAGE);
					}
					else
					{
						JOptionPane.showMessageDialog(null, "Los numeros de Array eran:\n"+numsArray+"\nLo siento no adivinaste en los 3 intentos posibles \nvuelve a jugar si quieres", "Lo siento ...", JOptionPane.INFORMATION_MESSAGE);
					}
					volvioMenu = true;
					break;
				case 2:
					JOptionPane.showMessageDialog(null, "EL juego funciona de la siguiente manera:\n se genera un array con 10 numeros aleatorios\n y tu tienes que adivinar uno de esos numeros\n tienes 3 intentos nada mas\n SUERTE!", "Como funciona", JOptionPane.INFORMATION_MESSAGE);
					volvioMenu = true;
					break;
				case 3:
					JOptionPane.showMessageDialog(null, "Gracias por Jugar", "Gracias", JOptionPane.INFORMATION_MESSAGE);
					break;

			}
		}while(opc != 3);
	}

	public static void main(String[] args)throws IOException
	{
		adivinaElNumero array1 = new adivinaElNumero();

		array1.llenarArray();
		array1.opc = Integer.parseInt(JOptionPane.showInputDialog("==[Menu]==\n [1]Jugar [2]Ver instrucciones [3]Salir"));
		array1.elegir();
	}
}

```
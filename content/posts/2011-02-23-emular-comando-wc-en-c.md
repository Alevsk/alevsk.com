---
title: Emular comando WC en C
author: Alevsk
type: post
date: 2011-02-23T16:36:22+00:00
url: /2011/02/emular-comando-wc-en-c/
categories:
  - C y C++
  - Linux
  - Programming
  - Tips
  - Tutorials
tags:
  - backtrack
  - Linux Debugging
  - debian
  - distros
  - grep
  - grub
  - Hello world
  - Hello World
  - Java
  - Linux
  - Programming
  - Social Media
  - ubuntu

---
[![](/images/web_hosting.jpg)](http://www.alevsk.com/2011/02/emular-comando-wc-en-c/web_hosting/)  
Hola de nuevo, aquí les traigo un código que nos dejaron en la clase de Sistemas Operativos.  
Básicamente tenemos que emular la salida del comando **wc** de **linux** (el que cuenta el numero de lineas, caracteres o palabras de un archivo).

Pero con unas pequeñas diferencias

  * Recibe n archivos (parámetros)
  * Cuenta el numero de lineas, caracteres y palabras de cada archivo
  * Muestra la suma total de lineas, caracteres y palabras de todos los archivos
  * Cada archivo es manipulado por un thread

```Transact-SQL
#include   // fork
#include      // getpid, getppid
#include       // printf
#include	// wait
#include	// strcat
#include

//Constantes
#define TIEMPO 1
//Variables globales
int total_lineas = 0;
int total_palabras = 0;
int total_caracteres = 0;


void* manejoArchivo (char* archivo)
{	
	int *a,*b,*c;
	a = &total_lineas;
	b = &total_palabras;
	c = &total_caracteres;
	char x;

	int nlineas = 0, npalabras = 1, ncaracteres = 0;
	
	
	//printf("%s\n",archivo);
	
	FILE *file;
	file = fopen(archivo, "rt");
	if (file == NULL)
	{
		puts("Error al abrir el archivo");
	}
	else
	{
		puts("Accediendo al archivo");
		while (feof(file) == 0)
		{
		        //fgets(caracteres,100,archivo);
		        //printf("%s",caracteres);
			x = getc(file); // Obtiene un caracter del archivo
			//putchar(x); // Lo despliega en pantalla y continua..
			if(x == 32)
			{
				npalabras++;

			}
			if(x == '\n') 
			{
				nlineas++;
			}
			if(x != '\n' && x != ' ')
			{
				ncaracteres++;
			}
		}
		ncaracteres = ncaracteres - 1;
		if(npalabras > 1){npalabras = npalabras + (nlineas - 1);}
	
		*a = *a + nlineas;
		*b = *b + npalabras;
		*c = *c + ncaracteres;
		
		printf("El numero de lineas del archivo %s es %d\n",archivo,nlineas);
		printf("El numero de caracteres del archivo %s es %d\n",archivo,ncaracteres);
		printf("El numero de palabras del archivo %s es %d\n",archivo,npalabras);
	}
}

int main(int argc, char *argv[])
{
	int n_ficheros = 0;
	int i = 0;
	char *puntero;
	
    	if(argc < 2)
    	{
        	printf("Debes teclear el nombre de almenos 1 fichero, ej:\n");
		printf("./wc_emulado archivo.txt archivo2.txt archivo3.txt\n");
        	exit(1);
    	}

	n_ficheros = argc - 1; //Numero de ficheros a leer

	//creo tantos threads como ficheros haya pasado por argumentos
	pthread_t ficheros_t[n_ficheros];
	
	for (i=0;i<=n_ficheros;i++)
	{
		sleep(TIEMPO);		
		pthread_create(&ficheros_t[i],NULL,&manejoArchivo,argv[i+1]);
	}

	printf("EL numero total de lineas es: %d\n",total_lineas);
	printf("EL numero total de caracteres es: %d\n",total_caracteres);
	printf("EL numero total de palabras es: %d\n",total_palabras);
	return -1;
	
}

```

[Aquí les dejo el código mas legible listo para que lo compilen.][1] 

salu2

 [1]: http://www.copypastecode.com/64450/
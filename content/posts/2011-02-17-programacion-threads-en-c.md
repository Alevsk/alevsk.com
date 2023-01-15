---
title: 'Programacion: Threads en C'
author: Alevsk
type: post
date: 2011-02-17T15:34:36+00:00
url: /2011/02/programacion-threads-en-c/
categories:
  - C y C++
  - Linux
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - Linux
  - Programming
  - shell
  - software libre
  - Solutions
  - Tutorials

---
### [![](/images/formsheader.jpg)](http://www.alevsk.com/2011/02/programacion-threads-en-c/formsheader/)

### 3GUGFVCXPCUB

De Wikipedia:

`In computer science, a thread of execution is the smallest unit of processing that can be scheduled by an operating system. It generally results from a fork of a computer program into two or more concurrently running tasks. The implementation of threads and processes differs from one operating system to another, but in most cases, a thread is contained inside a process. Multiple threads can exist within the same process and share resources such as memory, while different processes do not share these resources. In particular, the threads of a process share the latter's instructions (its code) and its context (the values that its variables reference at any given moment). To give an analogy, multiple threads in a process are like multiple cooks reading off the same cook book and following its instructions, not necessarily from the same page.`

## En resumen

Un thread es un subproceso que corre en paralelo y que comparte la memoria y los recursos con su proceso padre (el proceso padre puede tener varios threads), esto nos permite resolver el problema de la ejecución lineal, y podemos lograr que por ejemplo 2 procesos modifiquen el valor de una misma variable (esto también se puede hacer usando forks u apuntadores :p).

A continuación ejemplifico en un código el rol de un productor y un consumidor, el productor genera Items y el consumidor los consume xD.

Funciona de la siguiente forma, cada thread apunta a una misma localidad de memoria donde va modificando los valores, pero en orden, ya que si no fuera así el valor actual podría ser modificado varias veces por un proceso (el consumidor podría consumir 2 veces seguidas o el productor producir 2 items seguidos).

```Transact-SQL
#include 
#include 
#include 
/* Parameters to print_function.
*/

#define BUFFER_SIZE 10
//PRODUCTOS EN EXISTENCIA (memoria que compartiran los threads)
int j = 0; //in
//PRODUCTOS CONSUMIDOS (memoria que compartiran los threads)
int k = 0; //out

//TIPO DE DATO ITEM
typedef struct
{
	int dato;
}item;

//ARGUMENTOS DEL THREAD PRODUCTOR
struct propiedades_prod
{
	item buffer[BUFFER_SIZE];
	//numero de thread creado
	int n;
	int nextProduced;
};
//ARGUMENTOS DEL THREAD CONSUMIDOS
struct propiedades_cons
{
	item buffer[BUFFER_SIZE];
	int nextConsumed;
};

void* productor (void* parameters)
{
	struct propiedades_prod* p = (struct propiedades_prod*) parameters;

	int *creados;
	creados = &j

	int *consumidos;
	consumidos = &k
	
	while(1)
	{
		//while((*creados + 1) % BUFFER_SIZE == *consumidos) ;
		while((*creados + 1) == *consumidos) ;
		p->buffer[*creados].dato = p->nextProduced++;
		//printf("Productor: %d creo el producto: %d, %d %d \n",p->n,*creados,p->buffer[*creados].dato,*consumidos);
		printf("Productor: %d creo el producto: %d\n",p->n,*creados);
		*creados = (*creados + 1) % BUFFER_SIZE;
		//*creados = *creados + 1;		
		sleep(1);
	}
}
void* consumidor (void* parameters)
{ 
	struct propiedades_cons* p = (struct propiedades_cons*) parameters;

	int *creados;
	creados = &j

	int *consumidos;
	consumidos = &k
	
	while(1)
	{
		while(*creados == *consumidos) ;
		p->nextConsumed = p->buffer[*consumidos].dato;
		//printf("Consumio %d, %d %d \n",*consumidos,p->nextConsumed,*creados);
		printf("Consumio %d \n",*consumidos);
		*consumidos = (*consumidos + 1) % BUFFER_SIZE;
		//*consumidos = *consumidos + 1;		
		sleep(1);
	}
}
/* The main program.
*/
int main ()
{
	pthread_t thread1_id;//productores
	pthread_t thread2_id;//productores
	pthread_t thread3_id;//consumidor

	struct propiedades_prod thread1_prop;
	struct propiedades_prod thread2_prop;
	struct propiedades_cons thread3_prop;

	/* Creamos el 1 thread */
	thread1_prop.n = 1;
	thread1_prop.nextProduced = 0;
	pthread_create (&thread1_id, NULL, &productor, &thread1_prop);
	
	/* Creamos el 2 thread */
	thread2_prop.n = 2;
	thread2_prop.nextProduced = 0;
	pthread_create (&thread2_id, NULL, &productor, &thread2_prop);

	/* Creamos el 3 thread que sera el consumidor */
	thread3_prop.nextConsumed = 0;
	pthread_create (&thread3_id, NULL, &consumidor, &thread3_prop);

	pthread_join (thread1_id, NULL);
	pthread_join (thread2_id, NULL);
	pthread_join (thread3_id, NULL);
	return 0;
}


```

Para compilar el programa lo pueden guardar por ejemplo como **thread.c** y desde la shell de linux escriben:

```Text only
gcc -lpthread thread.c -o thread
```

salu2
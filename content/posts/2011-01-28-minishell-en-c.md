---
title: MiniShell en C
author: Alevsk
type: post
date: 2011-01-28T17:41:38+00:00
url: /2011/01/minishell-en-c/
categories:
  - C y C++
  - Linux
  - Personal
  - Programming
  - Tutorials
tags:
  - backtrack
  - Linux Debugging
  - debian
  - distros
  - hackers
  - Hello world
  - Linux
  - Personal
  - Programming
  - Technology
  - Tutorials
  - ubuntu

---
[![](/images/shell_banner.jpg)](http://www.alevsk.com/2011/01/minishell-en-c/shell_banner/)

Hola, este es un programa que me dejaron en una clase que estoy tomando que se llama Sistemas Operativos, se trata de crear procesos hijos (con fork) para emular una pequeña shell de sistema.

El programa recibe los comandos y parámetros como argumento, por ejemplo:

**./shell cat /etc/passwd | grep home | cut -d: -f1,1,5**

Para obtener los logins y nombres de todos los usuarios del sistema donde su directorio personal este en el home.  
`
```Transact-SQL

/*************************************************
 * Interprete de comandos en C by Alevsk	 *
 *************************************************/

#include   // fork
#include      // getpid, getppid
#include       // printf
#include	// wait
#include	// strcat

int main(int argc, char *argv[])
{
    	int n,m, i = 1;
	char comando[256];
	char *puntero;

    	if(argc < 2)
    	{
        	printf("Debes teclear almenos 1 comando, ej. ls\n");
        	exit(1);
    	}

   	strcpy(comando,argv[i]);
   
   	do
   	{
		if(argv[i] && argv[i+1])
		{
			//strcat(argv[1]," ");
			//strcat(argv[1],argv[i+1]);
			strcat(comando," ");
			puntero = strcat(comando,argv[i+1]);		
			i++;
		}
		else
		{
			puntero = comando;
			break;
		}	
   	}while(1);


	if(n = !fork())
	{
	
		//execlp("bash","bash","-c",argv[1],0);
		execlp("bash","bash","-c",puntero,0);
		printf("\n");
		exit(1);
	}
	wait(&n); //Esperar a que el proceso hijo termine
	return -1;
}

```
<p>`

### Descargar SHell

http://www.alevsk.com/proyectos/programacion/shell.c

salu2</p>
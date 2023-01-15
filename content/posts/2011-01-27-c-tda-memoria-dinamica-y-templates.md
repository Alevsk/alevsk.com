---
title: C++ TDA memoria dinamica y templates
author: Alevsk
type: post
date: 2011-01-27T15:25:41+00:00
url: /2011/01/c-tda-memoria-dinamica-y-templates/
categories:
  - C y C++
  - Linux
  - Personal
  - Programming
tags:
  - CSS
  - Hello world
  - Hello World
  - Java
  - Javascript
  - Jquery
  - Linux
  - Personal
  - Programming
  - software libre
  - Solutions
  - Tutorials
  - ubuntu

---
[![](/images/cpp_meatboy.jpg)](http://www.alevsk.com/2011/01/c-tda-memoria-dinamica-y-templates/cpp_meatboy/)  
Hola este no es un tutorial, solo es un programa en C++ que estoy haciendo para una clase donde tenemos que crear un tipo de dato abstracto Matriz, sobrecargar algunos operadores y métodos, usar algo de manejo de memoria dinámica y templates.

Dejo el código por si a alguien le sirve 🙂 …

[![](/images/cpp1.png)](http://www.alevsk.com/2011/01/c-tda-memoria-dinamica-y-templates/cpp1/)
<p style="text-align: center;">
  Menu del programa
</p>
<p style="text-align: center;">
[![](/images/cpp2.png)](http://www.alevsk.com/2011/01/c-tda-memoria-dinamica-y-templates/cpp2/)
</p>
<p style="text-align: center;">
  Mostrar las matrices
</p>
<p style="text-align: center;">
[![](/images/cpp3.png)](http://www.alevsk.com/2011/01/c-tda-memoria-dinamica-y-templates/cpp3/)[](http://www.alevsk.com/2011/01/c-tda-memoria-dinamica-y-templates/cpp4/)
</p>
<p style="text-align: center;">
  Sumar las Matrices[![](/images/cpp4.png)](http://www.alevsk.com/2011/01/c-tda-memoria-dinamica-y-templates/cpp4/)
</p>
<p style="text-align: center;">
[](http://www.alevsk.com/2011/01/c-tda-memoria-dinamica-y-templates/cpp4/)La transpuesta de la matriz
</p>

### Implementacion

```Arduino
#include
#include "Matriz.h"
//#include  //descomentar esta linea en windows
using namespace std;

int main(){

    int opc = 0;
    Matriz a(1),b(1),c,d;

    a.llenaMatriz();
    b.llenaMatriz(1);
    do
    {
        cout<<"[0] Sumar matrices"<<<"[1] Multiplicar matrices"<<<"[2] Mostrar matrices"<<<"[3] Transpuesta (los resultados de suma/multiplicacion)"<<<"[4] Las diagonales (los resultados de suma/multiplicacion)"<<<"[5] Numero menor de la matriz (los resultados de suma/multiplicacion)"<<<"[6] Salir del programa"<<<<"Elije una opcion: "; cin>>opc;

        switch(opc)
        {
            case 0:
                c=a+b;
                cout<<<<"Matriz A"<<<<"Matriz B"<<<<<<"El numero menor de la Matriz: "<<<<<"Es: "<<<<<<"Gracias por usar el programa";
                break;
            default:
                cout<<"Opcion invalida, elije un numero del menu";
        }
    }while(opc != 6);

    //getch(); //descomentar esta linea en windows
    return 0;
}
```

### Diseño

```Transact-SQL
#include 
#include 
#include 
#include 
using namespace std;
        const int ren = 5;
        const int col = 5;

template  class Matriz
{
    public:
        //constructores
        Matriz();
        Matriz(T);
        Matriz(Matriz &);
        ~Matriz();

        //metodos
        void operator = (const Matriz &);
        T getDato(int, int);
        void setDato(int, int, T);
        void transpuesta (Matriz &);
        void muestradiagonales();
        void llenaMatriz();
        void llenaMatriz(int);
        T menor();


    private:
        //puntero a punteros
        T **datos;
        //T datos[ren][col];
};

templateMatriz::~Matriz()
{
    //liberar localidades de memoria
    for (int i=0; iMatriz::Matriz()
{
    //datos = new T[ren*col];

    datos = (T **)malloc (sizeof(int *)*col); /*Reservas tantos punteros como filas*/
for (int i=0; iMatriz::Matriz(T valorinicial)
{
    //datos = new T[ren*col];

        datos = (T **)malloc (sizeof(int *)*col); /*Reservas tantos punteros como filas*/
for (int i=0; i void Matriz::llenaMatriz()
{
    int n = 0;
    srand(time(NULL));
    for(int i = 0; isetDato(i,j,n);
        }
    }
}
template void Matriz::llenaMatriz(int sal)
{
    int n = 0;
    srand(time(NULL));
    for(int i = 0; i 100) {setDato(i,j,100);}else{

            setDato(i,j,n+sal);}
        }
    }
}
templateMatriz::Matriz( Matriz &M)
{
    //datos = new T[ren*col];

        datos = (T **)malloc (sizeof(int *)*col); /*Reservas tantos punteros como filas*/
for (int i=0; iT Matriz::getDato(int c, int r)
{
    //c = columna
    //r = renglon

    return datos[c][r];
    //return datos[col*c+r];
}

template T Matriz::menor()
{
    int menor = this->getDato(0,0);
    for(int i = 0; igetDato(i,j) < menor) menor = this->getDato(i,j);
        }
    }

    return menor;
}

templatevoid Matriz::muestradiagonales()
{
    int renglon = ren-1;
    cout<getdato(i,i)<<"]"; !="col)" &="" (matriz="" -="" 1;="" aceptan="" c,="" cout<="" cout<<"solo="" cout<getdato(renglon,i)<<"]";="" cuadradas";="" dato)="" datos[c][r]="dato;" datos[col*c+r]="dato;" datos[col*r+c]="dato;" else="" float="" for(int="" i="0;" if(ren="" int="" isetdato(i,j,m.getdato(j,i));="" m)="" matrices="" matriz::setdato(int="" matriz::transpuesta="" r,="" renglon="renglon" se="" t="" template="" this-="" tmp="0;" void="" {="" }="">setDato(j,i,tmp);
            }
        }
    }

}
template  void Matriz::operator = (const Matriz &igualar)
{
    int i = 0, j = 0;
     for(i = 0; isetDato(i,j,igualar.datos[i*j]);
             //this->setDato(i,j,igualar.datos[i*j]);

             this->setDato(i,j,igualar.datos[i][j]);
             this->setDato(i,j,igualar.datos[i][j]);
         }
     }
}
template  Matriz operator + (Matriz &uno, Matriz &dos)
{

     Matriz temp;
     for(int i = 0; i Matriz operator * (Matriz &uno, Matriz &dos)
{

    int i = 0, j = 0, k = 0;
     Matriz objTemp;
     for(i = 0; i std::ostream& operator<< (std::ostream &salida, Matriz &objeto)
{
     for(int i = 0; i

### Descargar los archivos

[practica3.cpp][1]  
[Matriz.h][2]

salu2

PD: El banner del post no tiene nada que ver xD, lo que pasa que en ese momento estaba jugando Super Meat Boy :p

 [1]: http://www.alevsk.com/proyectos/programacion/practica3.cpp
 [2]: http://www.alevsk.com/proyectos/programacion/Matriz.h
```</getdato(i,i)<<"]";>
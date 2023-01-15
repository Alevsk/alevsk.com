---
title: Juego 4 en raya hecho en C++
author: Alevsk
type: post
date: 2012-08-22T18:31:58+00:00
url: /2012/08/juego-4-en-raya-hecho-en-c/
categories:
  - C y C++
  - Personal
  - Programming
tags:
  - Linux Debugging
  - Math
  - Programming
  - software
  - software libre
  - Solutions

---
Revisando entre mis curiosidades me encontré un código que hice hace varios años (de la prepa creo), se trata del juego 4 en línea o **4 en raya hecho en C++**, he decidido subirlo al blog ya que no me gustaría que se perdiera en el final de los tiempos xD.

[![](/images/4_en_raya_cpp.png)](http://www.alevsk.com/2012/08/juego-4-en-raya-hecho-en-c/4_en_raya_cpp/)

Pueden descargar el código fuente aca:

[Juego 4 en raya hecho en C++](http://pastebin.com/Xq5SLamV)

```cpp
#include <iostream>

using namespace std;

const int n=6;  
const int m=8;

bool sobranEspaciosLibres(int tablero\[n\]\[m\])  
{  
for(int i = 0; i < 6; i++)  
{  
for(int j = 0; j < 8; j++)  
{  
if(tablero\[i\]\[j\] == 0)  
{  
//Sobran espacios donde colocar fechas  
//cout<<"Hay espacios"<<endl; ";="" .="" 6;="" 8;="" <="" colocar="" colocarfichaen(int="" columna)="" cout<<"="" cout<<"no="" cout<<endl;="" donde="" else="" empatado="" empate"<<endl;="" espacios="" espacios:="" false;="" fichas,="" for(int="" hay="" i="" i++)="" if(!(i+1="" if(tablero\[i\]\[j\]="2)" imprimirtablero(int="" int="" j="" j++)="" juego="" mas="" no="" o="" return="" sobran="" tablero\[n\]\[m\])="" tablero\[n\]\[m\],="" true;="" void="" x="" {="" }=""> 5))  
{  
if(tablero\[i\]\[columna\] == 0 && tablero\[i+1\]\[columna\] != 0 )  
{  
return i;  
}  
}  
else  
{  
//Alcanzo la base del tablero  
if(tablero\[i\]\[columna\] == 0)  
{  
return i;  
}  
}  
}

return -1;  
}

bool columnaATope(int tablero\[n\]\[m\], int columna)  
{  
if(tablero\[0\]\[columna\] != 0)  
{  
cout<<"No hay espacio para colocar la ficha ahi"<<endl; !="0))" !encontrado)="" "<<columna<<endl;="" "<<fila<<"="" "<<i<<endl;="" "<<jugador<<"="" "<<nuevacolumna<<endl;="" "<<nuevafila<<"="" "<<total<<endl;="" &&="" <="" \="" a="" base="" bool="" break;="" columna="" columna,="" columna:="" coordenadas="" cout<<"el="" cout<<"fila:="" cout<<"i:="" cout<<"nueva="" cout<<"total:="" diagonal="" do="" donde="" else="" en="" encontrado="false;" false;="" fila="" fila,="" fila:="" for(int="" gana!"<<endl;="" ganador(int="" horizontal="" i="" i++)="" if(encontrado)="" if(nuevafila="" if(tablero\[fila\]\[i\]="jugador" if(tablero\[i\]\[columna\]="jugador" if(total="4)" inicia="" int="" jugador="" jugador)="" la="" m;="" n;="" nueva="" nuevacolumna="0)" nuevacolumna–;="" nuevafila="fila;" nuevafila–;="" obtener="" return="" tablero\[n\]\[m\],="" total="0;" total++;="" true;="" vertical="" while((nuevafila="" {="" ||="" }="" –="">= n)  
break;

//cout<<"nueva Fila: "<<nuevafila<<" !="m))" !encontrado)="" "<<columna<<endl;="" "<<fila<<"="" "<<jugador<<"="" "<<nuevacolumna<<endl;="" "<<nuevafila<<"="" "<<total<<endl;="" &&="" <="" break;="" columna:="" cout<<"el="" cout<<"fila:="" cout<<"nueva="" cout<<"total:="" diagonal="" do="" else="" encontrado="false;" fila:="" gana!"<<endl;="" if(encontrado)="" if(nuevafila="" if(tablero\[nuevafila\]\[nuevacolumna\]="jugador" if(total="4)" jugador="" n);="" nueva="" nuevacolumna="m)" nuevacolumna++;="" nuevafila="fila;" nuevafila++;="" nuevafila–;="" return="" total="0;" total++;="" true;="" while((nuevafila="" {="" ||="" }="" }while(nuevafila="">= n)  
break;

//cout<<"nueva Fila: "<<nuevafila<<" !encontrado)="" ";="" "<<endl;="" "<<jugador<<"="" "<<nuevacolumna<<endl;="" "<<total<<endl;="" &&="" 0's="" 1="" 8:="" <="" al="" bool="" cin="" colocarcolumna="-1;" columna:="" columnatope="true;" con="" cout<<"="" cout<<"el="" cout<<"total:="" cout<<"turno="" cout<<matriz\[i\]\[j\]<<"="" del="" do="" el="" elije="" else="" encontrado="true;" false;="" for(int="" gana!"<<endl;="" i="" i++)="" if(encontrado)="" if(tablero\[nuevafila\]\[nuevacolumna\]="jugador" if(total="4)" if(ultimo="1)" int="" j="" j++)="" juego="" jugador="" logica="" m;="" main()="" matriz\[i\]\[j\]="0;" matriz\[n\]\[m\];="" n);="" n;="" nueva="" nuevacolumna–;="" nuevafila++;="" numero="" preparamos="" rellenandolo="" return="" tablero="" total="0;" total++;="" true;="" ultimo="0;" un="" {="" }="" }while(nuevafila="" –="">>colocarColumna; cout<<endl; 0="" <="" colocarcolumna="" colocarcolumna–;="" columnatope="columnaATope(matriz,colocarColumna);" while((colocarcolumna="" ||="" }=""> 7) || columnaTope);

int colocarFila = ColocarFichaEn(matriz,colocarColumna);  
matriz\[colocarFila\]\[colocarColumna\] = jugador;  
ImprimirTablero(matriz);

//Revisar si hay un 4 en raya  
if(ganador(matriz,colocarFila,colocarColumna,jugador))  
{  
break;  
}

ultimo = jugador;  
jugador++;  
}  
while(sobranEspaciosLibres(matriz));

return 0;  
}
```

PD 

No tiene nada de **inteligencia artificial** ni **algoritmos minimax**, es el código del juego simplemente, muy sencillo y algo feo también :p.</endl;></nuevafila<<"></nuevafila<<"></endl;></endl;></iostream>
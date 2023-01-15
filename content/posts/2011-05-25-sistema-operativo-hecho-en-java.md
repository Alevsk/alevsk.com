---
title: Sistema Operativo hecho en Java
author: Alevsk
type: post
date: 2011-05-25T01:08:29+00:00
url: /2011/05/sistema-operativo-hecho-en-java/
categories:
  - Java
  - Linux
  - Mac
  - Personal
  - Programming
  - Tutorials
tags:
  - backtrack
  - Linux Debugging
  - debian
  - Storage
  - distros
  - Hello World
  - Java
  - Linux
  - Personal
  - Programming

---
[![](/images/SO_Java.jpg)](http://www.alevsk.com/2011/05/sistema-operativo-hecho-en-java/so_java/)

Hola lectores, quiero comentarles que ya estoy de vacaciones :), este final de semestre acabo muy atareado, termine varios proyectos y comencé con otros nuevos (prometo realizar algunos post sobre cosas en las que estoy trabajando actualmente :)), reforcé mas mis conocimientos en programación y aprendí a programar para varias plataformas también (iphone, android, symbian, etc), también aprendí nuevas cosas sobre **SEO**, **SMO**, y cosas que tienen que ver con posicionamiento web x'D.

Pero bueno, en resumen preparare un post con varios proyectos que he terminado para que los vean, ahora como ya es de costumbre quiero publicar el código de un “**Sistema Operativo**" hecho en **Java** que nos dejaron como proyecto final para la clase de **Sistemas Operativos** (valga la redundancia xD), dijo **Sistema Operativo** entre comillas ya que en realidad no lo es, si no que simula uno, los componentes y las partes mas importantes de estos, como el administrador de memoria, administrador de procesos, la calendarización, el swaping, pages faults, el procesador, los **algoritmos** de **administración** tanto de memoria como de procesador y cosas así x'D.

Si bien yo hubiera decidido programar el “Sistema Operativo" en **C**, **C++** o algún lenguaje de ese tipo, la practica lo pedía en **java** para ver como era el compartido de la memoria utilizando **threads** (aunque en **C** también se puede utilizar el multiprocesamiento y el mapeo de memoria, pero pues que se le hacia x'D) y la simulación de la memoria utilizando **pilas** y/o **listas** (según el **algoritmo** de administración que eligiéramos).

Como datos mas técnicos se utilizo el **algoritmo** [LRU][1] para realizar la administración, paginado, swaping, etc referente a la memoria.

Como bono extra también le agregamos una **shell** (consola/interfaz de comandos) para pasar ciertos comandos y que regresara el estado actual de la **memoria**, los procesos que están corriendo (su **pid**, etc), lanzar nuevas shells, matar procesos y hasta ejecutar un juego … también hecho en **JAVA** x'D.

A continuación una lista mas detallada de los comandos:

```Tera Term macro
CommandOutput += "process report    ... show how many process are running on the system (system & normal process) and their names\n";
    			CommandOutput += "memory report     ... show a report about the total amount of pages that every process are consuming\n";
    			CommandOutput += "show commands     ... Show this help menu\n";
    			CommandOutput += "launch new shell  ... Open a new command shell\n";
    			CommandOutput += "close this shell  ... Close the currenlty shell in use\n";
    			CommandOutput += "play snake        ... Play Snake the video game\n";
    			CommandOutput += "any Unix command  ... show the output of the command (if any)\n";
    			CommandOutput += "shutdown          ... Shutdown the Operating system\n";

```

Puedes descargar el codigo haciendo clic en “**Descargar**"

<div class="demobox">
[![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/download.png)](http://www.megaupload.com/?d=Z8OJ82DK)
</div>

La mayor ganancia que me dejo realizar este proyecto fue que ahora comprendo mas a fondo como es que un **sistema operativo** funciona x'D (el despachador, procesos, memoria, cache, swaping, segmentación, paginado, etc), en el **proyecto** no lo incluí pero también aprendimos como funciona un disco duro (ejecuta un impulso magnético en los sectores del **disco duro**, lo que hace que este en 0 o 1 :p), las partes del disco duro (pistas, discos, cilindros cabezal), algoritmos de acceso a memoria, **sistemas de archivos**, particionamiento (unidades lógicas, primarias, por que la tabla de particiones es de bytes, etc) y también sobre tabla tablas y mas tablas U.U :S. La materia contenía muchísima teoría pero al final si que valió la pena :).

salu2

 [1]: http://es.wikipedia.org/wiki/Algoritmos_de_reemplazo_de_p%C3%A1ginas
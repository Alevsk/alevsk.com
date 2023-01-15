---
title: Activar colores en la terminal de MAC
author: Alevsk
type: post
date: 2011-09-03T00:23:55+00:00
url: /2011/09/activar-colores-en-la-terminal-de-mac/
categories:
  - Mac
  - Tips
  - Tutorials

---
En algún post anterior les había mencionado sobre una buena app llamada [iTerm][1], pero pasando los meses pense que es mucho mejor Terminal (la **app** de interprete de comandos que trae por default el sistema operativo), sin embargo le hacia falta algo, **Activar colores en la terminal de MAC** como en la **shell de linux** :p, así que me di a la tarea de investigar como se activaban, es realmente facil, a continuación aqui en listo los pasos.

**Primero**  
Yo decidi cambiar el diseño que trae por defecto la terminal, para hacer eso se van a **Terminal > Preferencias > Ajustes** y elijan la que uds quieran.

[![](/images/Captura-de-pantalla-2011-09-02-a-las-19.05.21.png)](http://www.alevsk.com/2011/09/activar-colores-en-la-terminal-de-mac/captura-de-pantalla-2011-09-02-a-las-19-05-21/)

**Segundo**  
En la raiz de directorio de usuario **/Users/tuUsuario**, edita (si no existe lo creas) el archivo .bash_profile

```Text only
glados:~ alevsk$ pwd
/Users/alevsk
glados:~ alevsk$ vi .bash_profile

```

**Tercero**  
Dentro del archivo copia y pega las siguientes lineas (preciona la letra i de tu teclado para comenzar a escribir)

```GDScript
export CLICOLOR=1

export LSCOLORS=Gxfxcxdxbxegedabagacad

```

Al final guardas y sales de vi con el comando **:wq!** (presiona **esc** para salir del modo de escritura).

Los código de colores **LSCOLORS** que puedes elegir son los siguientes:

```Text only
a = black
b = red
c = green
d = brown
e = blue
f = magenta
g = cyan
h = light gray
x = default

```

y el orden de asignación va de la siguiente manera:

```Text only
DIR
SYM_LINK
SOCKET
PIPE
EXE
BLOCK_SP
CHAR_SP
EXE_SUID
EXE_GUID
DIR_STICKY
DIR_WO_STICKY

```

Lo anterior es solamente para que sepan que significa lo que acaban de copiar y pegar, ya existen servicios que te generan tu configuración de colores de manera grafica y amigable 🙂 [LSCOLOR Generator][2]

A continuación un ejemplo de como configure mi **terminal** 🙂

[![](/images/Captura-de-pantalla-2011-09-02-a-las-19.19.55.png)](http://www.alevsk.com/2011/09/activar-colores-en-la-terminal-de-mac/captura-de-pantalla-2011-09-02-a-las-19-19-55/)

 [1]: http://www.alevsk.com/2011/05/mi-top-18-de-aplicaciones-para-mac-2/
 [2]: http://geoff.greer.fm/lscolors/
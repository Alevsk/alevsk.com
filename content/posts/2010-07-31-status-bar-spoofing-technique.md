---
title: Status Bar Spoofing Technique
author: Alevsk
type: post
date: 2010-07-31T05:38:48+00:00
url: /2010/07/status-bar-spoofing-technique/
categories:
  - Ethical Hacking
  - HTML
  - Javascript
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - Bar
  - hackers
  - Programming
  - Spoofing
  - Status
  - Ulr
  - web

---
[![Photobucket](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/etiquetas.jpg)](http://s251.photobucket.com/albums/gg290/midgar156/alevsk-zone/?action=view¤t=etiquetas.jpg)

La palabra Spoofing en términos de seguridad de redes hace referencia al uso de técnicas de suplantación de identidad generalmente con usos maliciosos o de investigación, existen diferentes tipos de técnicas de spoofing, pueden leer un poco en el siguiente link http://es.wikipedia.org/wiki/Spoofing, de lo que escribiré en esta ocasión es de una técnica que no es nada nueva llamada Status Bar Spoofing pero vale la pena tenerla en cuenta para protegernos y para aplicar técnicas derivadas a partir de este vector de ataque, todo esto en un ambiente seguro y controlado, claro esta … continuemos

En la actualidad muchas personas piensan que al pasar el mouse por encima de un link la url que se muestra en la status bar es a la que sera redirigida, sin embargo se ha demostrado que esto es fácil de falsificar, a continuación pondré algunos ejemplos:

  * [http://www.hsbc.com](http://www.hsbc.com/)
  * [http://www.presidencia.gob.mx/](http://www.presidencia.gob.mx/)
  * [http://www.pan.org.mx/](http://www.pan.org.mx/)

_Nota: Para ver el ejemplo tienes que tener javascript habilitado_

Viendo los ejemplos anteriores vemos que las maneras de evitar caer esta trampa seria o checar el código fuente de cada pagina a la que le vayamos a dar un clic o instalar algún addon en firefox que nos bloquee los scripts, pueden ver el codigo de los links spoofeados a continuacion:

```Text only
[http://www.hsbc.com](http://www.hsbc.com/)
[http://www.presidencia.gob.mx/](http://www.presidencia.gob.mx/)
[http://www.pan.org.mx/](http://www.pan.org.mx/)
```

Si analizan el código bien pueden ver que toda la magia la hace el evento **“onmousedown"** de javascript.

### onmouse**down**

Se produce el evento onmousedown cuando el usuario pulsa sobre un elemento de la página. onmousedown se produce en el momento de pulsar el botón, se suelte o no, aqui tienen una lista completa de eventos en javascript > http://www.desarrolloweb.com/articulos/1236.php

Ya con esto es fácil armar enlaces spoofeados siguiendo la siguiente estructura

[![Photobucket](http://i251.photobucket.com/albums/gg290/midgar156/alevsk-zone/status_bar_spoofing.png)](http://s251.photobucket.com/albums/gg290/midgar156/alevsk-zone/?action=view¤t=status_bar_spoofing.png)

Con todo lo anterior se me ocurre que esta técnica puede ser utilizada con fines maliciosos para robo de cookies en alguna pagina que tenga cross site scripting, mandar datos por GET o una combinación de técnicas de phishing y scams avanzados, así parecería que la víctima siempre esta navegando en el sitio web de confianza.

## Actualizado!

En el blog de mi amigo [Dr. White][1] vi que el abordo el mismo tema sobre la peligrosidad del status bar spoofing, sin embargo el comentaba que no era muy efectivo el evento **onmousedown** de javascript por que al hacer clic y arrastrar el link se podia ver el verdadero link, pueden ver en el siguiente ejemplo

  * [http://twitter.com/](http://twitter.com/)

_Hagan clic sobre el link y arrastrenlo y veran en el status bar el link real_

Visto esto el link fraudulento ha fallado, pero ahora entra el evento **onmouseup**, intenten hacer lo mismo de dar clic en el link y arrastrarlo.

  * [http://twitter.com](http://twitter.com)

Como ven gracias al evento onmouseup el link original continua escondido, eso es por que el evento se ejecuta una vez que hayamos soltado el dedo el mouse cuando ya no hay marcha atras.

———————————————————————————————-

_**Lectura Obligatoria:**_

 _La información de este post en especifico asi como los otros que traten sobre hacking, es con fines únicamente de informar y de que el lector aprenda de las amenazas que existen en la red, no es para andar haciendo cosas maliciosas, [www.alevsk.com][2] así como el administrador [@Alevsk][3] no se responsabiliza del mal uso que se pueda llegar a hacer con estos estudios de hacking ético … nuevamente los exhorto a ver el hacking desde un punto de vista ético, de aprendizaje y mas que nada como una disciplina muy interesante 🙂 Happy hacking_

 [1]: http://www.seguridadblanca.org/
 [2]: http://www.alevsk.com
 [3]: http://twitter.com/Alevsk
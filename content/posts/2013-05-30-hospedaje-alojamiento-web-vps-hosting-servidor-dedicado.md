---
title: ¿Nuevo proyecto? ¿Cual es la solución que mi cliente necesita?
author: Alevsk
type: post
date: 2013-05-30T01:26:13+00:00
url: /2013/05/hospedaje-alojamiento-web-vps-hosting-servidor-dedicado/
categories:
  - Geek
  - Programming
  - Social Media
  - Technology
  - Tips
tags:
  - Programming
  - Social Media
  - software libre
  - Solutions
  - Technology
  - Tutorials
  - web

---
[![942060_639498696079525_1765687384_n](/images/942060_639498696079525_1765687384_n.jpg)](http://www.alevsk.com/2013/05/hospedaje-alojamiento-web-vps-hosting-servidor-dedicado/942060_639498696079525_1765687384_n/)

## Educando a nuestros clientes

Muchas veces cuando comenzamos un proyecto personal o incluso cuando nos piden que realicemos una cotización no siempre tenemos en cuenta el “hardware" necesario que utilizara nuestra aplicación, sitio web o proyecto en general y por ende elegir la plataforma y las distintas tecnologías que utilizaremos resulta una tarea complicada.

Además si nosotros no tenemos idea de esto desde antes de comenzar el desarrollo el cliente mucho menos lo cual al final va a causar problemas

Uno de los ejemplos mas comunes es:

> <strong>Cliente</strong>: ¿Por que tengo este cobro extra de 100 USD?

> <strong>Desarrollador freelance</strong>: Ese cobro corresponde a el hosting y el dominio, esto no estaba incluido en la cotización del sitio web de su empresa

<em>* Cliente se enoja y lo paga de mala gana – o aveces ni lo paga *</em>

> <strong>Desarrollador freelance</strong>: Este pago es anual y es necesario para que su sitio web se mantenga en línea y pueda ser visitado

> <strong>Cliente</strong>: ¿Qué? ósea que me vas a cobrar 100 dólares anuales de por vida

<em>* Cliente no entiende nada y se enoja aun mas *</em></p></div>

La anterior es una de las conversaciones mas comunes que suelen suceder al termino de un proyecto, sobre todo cuando el desarrollador tiene poca experiencia en este mundo, por ende es responsabilidad del programador educar a sus cliente comenzando por explicarles a grandes rasgos el funcionamiento y que es lo mínimo que necesita un sitio web para funcionar, todo esto con la finalidad de que el cliente este enterado de los pagos que tendrá que realizar en el futuro.

<strong>Dominio</strong>: Es el nombre que escribirán los visitantes en <strong>Internet Explorer</strong> (por lo general es el navegador que los clientes conocen, pero siempre es bueno mostrarle que existen mas opciones como chrome, firefox, safari, Opera, etc) para poder acceder a su sitio web, le recomendamos que el nombre que elija sea algo acorde al sitio web o al nombre de su empresa.<strong>Hosting</strong>: Es una computadora que esta conectada las 24 hrs a Internet y es donde estarán almacenados los archivos del sitio web de su empresa para que puedan ser accesibles en cualquier momento

Estas son las necesidades mínimas y le costara – <em>Inserte cantidad aquí </em>– USD mas – <em>Inserte cantidad aquí</em> – USD por la aplicación / pagina web que quiere.

Explicando rápidamente los 2 conceptos anteriores a nuestros cliente (no nos tardamos mas de 10 minutos) nos permitirá evitarnos un escenario como el de la conversación anterior.

Ahora, ya que hemos adoctrinado a nuestro cliente respecto a las necesidades básicas de todo proyecto nos toca a nosotros determinar cual es la mejor opción en cuanto a las tecnologías utilizando algo yo llamo el “sentido común del desarrollador freelance", esto es algo que vamos reforzando mas y mas con la experiencia.

No importa el caso, desarrollador independiente o equipo de desarrollo, las personas que programen un sistema o cualquier tipo de aplicación en general tienen que tener la capacidad suficiente para crear predicciones de posibles comportamientos del “producto" en un futuro, me refiero a aspectos mas técnicos como por ejemplo cantidad de usuarios que utilizaran el sistema, cantidad de bases de datos, correos, posibles servicios web, etc. Y es que no son las mismas necesidades de por ejemplo un sitio web pequeño (como el de una empresa que solo requiere mostrar su misión, visión, objetivos, etc) al de por ejemplo la creación de una plataforma web que tenga su propia api y que utilice oAuth para interactuar con datos internos de un corporativo.

Podemos tomar por ejemplo la necesidad básica del almacenamiento (hosting) y tomar como punto de partida las 3 opciones principales en el mercado (no incluyo cloud computing ya que hablare de esa tecnología mas a detalle en un post futuro).

- Plan de Hosting compartido
- VPS (Virtual Private Server)
- Servidor dedicado

## Plan de Hosting compartido

Adquirir un hosting compartido es rentar espacio en el disco duro de un servidor donde podremos almacenar cierta cantidad de información, también es rentado por mas clientes además de que los recursos del servidor como la memoria RAM, el ancho de banda total, la velocidad de procesador, etc son compartidas por todos. Comúnmente los planes de hosting también brindan a los clientes otros servicios como nombres de dominio, cuentas de correo y bases de datos sin embargo estos son bastante limitados.

Este tipo de soluciones son ideales para sitios web pequeños, que no esperan una gran cantidad de visitas de usuarios al día, ni un crecimiento que supere las capacidades del servidor en el futuro, Ej: Pagina web sencilla de una empresa o institución o un blog personal.

## VPS (Virtual Private Server)

Como mencionaba anteriormente un servidor posee recursos (Memoria, espacio de almacenamiento, velocidad de procesador), la virtualización de servidores es una tecnología que nos permite tomar los recursos de una maquina y dividirlos de tal forma que simulemos que tenemos una computadora con menores capacidades, lo que al final nos permite tener virtualizados 100 servidores en un solo servidor físico (claro que esto depende de las capacidades físicas de la maquina perse). Podríamos crear servidores virtuales con recursos determinados como por ejemplo 1 Gb de memoria Ram, 500 Gb de espacio en disco duro y 1.5 Ghz de velocidad de procesador, una de las principales ventajas es que no tenemos que compartir el servidor virtual con ningún otro cliente por lo que podemos hacer uso de los recursos como queramos (sin embargo no es posible excedernos de los recursos que nos asignaron al principio), utilizar un VPS nos da mucha mas flexibilidad ya que ha diferencia de los hosting compartidos que generalmente vienen limitados en cuanto a tecnologías pre instaladas (por ejemplo solamente instalaciones de php, perl) en los VPS somos libres de instalar lo que nosotros queramos.

Los <strong>VPS</strong> generalmente son entregados en blanco, es decir sin nada instalado ni siquiera un sistema operativo, sin embargo en la mayoría de los paneles de administración decentes de empresas como hosting vps de Red Coruna, Rackspace o [Linode](https://www.linode.com/) se nos permite realizar varias tareas como elegir el sistema operativo que utilizara el servidor, realizar backups, reportes de rendimiento, etc.
Este tipo de soluciones son las ideales para empresas que manejaran sistemas internos de su compañía como nominas, seguimiento de campañas de marketing, ventas, contabilidad, etc o también para clientes que poseen varios sitios web y quieren administrarlos personalmente. Es necesario recalcar que la mayoría de las veces en proyectos donde hay involucrados VPS es necesaria la intervención de un administrador de sistemas. Es obvio que el costo por rentar un VPS es superior al de un plan de <strong>Hosting compartido</strong>, pero si lo que nuestro cliente quiere es exclusividad de recursos entonces esta seria la opción indicada.
## Servidor dedicado

Por ultimo pero no menos importante están los servidores dedicados que como su nombre lo indica es una maquina física exclusivamente para nosotros, aquí no hay limitaciones de recursos impuestas solo estamos nosotros y el hardware, obviamente su precio de renta varia de acuerdo a las capacidades físicas de la maquina, este tipo de soluciones son aplicables a compañías en donde los procesos internos son críticos y en donde es recomendable que la información que manejan sea totalmente privada, así como para sitios web, servidores de videojuegos, o aplicaciones que reciben una gran cantidad de usuarios al día y que tienen una gran demanda de ancho de banda, además de que no se pueden permitir estar fuera de línea ni un solo minuto (misión critica) y para esto tienen que implementar soluciones extra de redundancia de datos, etc.

Bueno con todo lo anterior en cuenta es mas fácil para nosotros como desarrolladores realizar cotizaciones mas exactas, además de que nunca esta de mas conocer cuales son las mejores opciones que hay en el mercado para así mismo recomendarlas a los usuarios comunes y mantener una buena imagen y credibilidad con ellos.
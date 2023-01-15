---
title: Introducción a GraphQL, Queries y Mutations
author: Alevsk
type: post
date: 2017-11-13T05:42:19+00:00
url: /2017/11/introduccion-a-graphql-queries-y-mutations/
categories:
  - Javascript
  - Personal
  - Talks and Events
  - Programming
  - Snippets
  - Technology
  - Tips
  - Tutorials
tags:
  - api
  - apis
  - expressjs
  - facebook
  - graphql
  - Javascript
  - nodejs
  - server

---
Como algunos de ustedes sabrán llevo poco mas de 1 año trabajando con una startup (si, deje Oracle XD) cuyo stack esta conformado en su mayoría por tecnologías de Javascript (NodeJS, ReactJS, Redux, Apollo, GraphQL, React-native, etc). y en esta ocasión quiero compartir con ustedes el material de la platica que di en el [GDLJS](https://www.facebook.com/gdljs/) del mes de octubre en Guadalajara, se trata de una breve introducción a GraphQL y cual ha sido mi experiencia con esta tecnología.

[![](/images/1-IvCDlfi3vQfgyKO1eFv4jA.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/1-ivcdlfi3vqfgyko1efv4ja/)

## ¿Que es GraphQL?

Primero lo primero, [GraphQL](http://graphql.org/) es un **lenguaje de consultas para tu API** creado por Facebook en 2012, es decir, es un intermediario comúnmente utilizado entre un cliente y algún [orm](https://en.wikipedia.org/wiki/Object-relational_mapping) de tu elección, es importante mencionar que GraphQL no se conecta directamente a tu base de datos, en lugar de eso ayuda a que el cliente defina el formato de la respuesta que desea obtener del servidor, mas adelante veremos algunos ejemplos.

## ¿Cual es la diferencia?

> Ya existen bastantes frameworks para desarrollar apis ¿Por que quisiera usar GraphQL? 

Bueno una de las principales diferencias con apis basadas en REST simple que tienen múltiples [endpoints](https://en.wikipedia.org/wiki/Communication_endpoint) es que en tu api basada en GraphQL solo tendras uno.

[![](/images/1-qpyJSVVPkd5c6ItMmivnYg.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/1-qpyjsvvpkd5c6itmmivnyg/)

Ademas de eso las apis comunes utilizan varios métodos HTTP (GET, POST, DELETE, PUT, OPTIONS, etc) según la operación que vayan a realizar, mientras que con GraphQL usaras solamente POST si así lo deseas, un endpoint para gobernarlos a todos 😉

> Todo bien hasta aquí, pero no me haz dicho realmente cual es el beneficio de usar esta tecnología 

Tranquilo pequeño saltamontes, consideremos el caso siguiente:

[![](/images/1-RapSQHY4a5TWqDaKpxUe-A-1200x601.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/1-rapsqhy4a5twqdakpxue-a/)

Del lado izquierdo tenemos un cliente que hace una petición GET a un endpoint de álbumes pasando un id para obtener sus assets, posteriormente por cada uno de esos assets solicita los comentarios (múltiples peticiones al servidor), adicionalmente los objetos JSON que reciba en las respuestas siempre tendrán los mismos atributos.

Del lado derecho vemos la petición POST equivalente para un endpoint basado en GraphQL, como podemos observar en el mismo payload de nuestra petición estamos indicando el formato de respuesta que queremos que el servidor nos regrese, atributos en los objetos, etc.

Habra quien diga que puede ingeniárselas para que la petición defina la respuesta del servidor, regresar atributos dinámicamente, etc. y le creo pero buena suerte manteniendo algo como esto 🙂

```bash
GET /albums/1/assets/comments/?include=asset.name,comment.author,comment.text
```

Este es precisamente el problema que GraphQL resuelve, GraphQL nos permite definir relaciones entre las entidades de nuestra aplicación e inyectar esos objetos relacionados en las respuestas cada vez que el cliente lo pida.

El siguiente ejemplo de código esta basado en Javascript utilizando expressJS, supongamos que el cliente necesita desplegar en su frontend un objeto como el siguiente:

[![](/images/Screen-Shot-2017-11-12-at-7.47.38-PM-473x300.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/screen-shot-2017-11-12-at-7-47-38-pm/)

Un objeto película con datos como su nombre, el año y la calificación de la critica, adicionalmente también queremos los datos de los actores involucrados y los comentarios de los visitantes que han visto esa pelicula.

Manos a la obra, vamos a iniciar un nuevo proyecto con **NodeJS**

```bash
$ npm init  
$ npm install –save express express-graphql graphiql graphql
```

Adicionalmente me gusta definir algunos comandos e instalar algunas dependencias para tener soporte es6, aquí pueden ver como queda mi [package.json](https://github.com/Alevsk/graphql-demo-server/blob/master/package.json) al final.

La estructura del proyecto es mas o menos la siguiente (demo-server)

[![](/images/Screen-Shot-2017-11-12-at-7.59.59-PM-1183x800.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/screen-shot-2017-11-12-at-7-59-59-pm/)

Los archivos y carpetas mas importantes son:

  * **app.js** es nuestro entry point
  * **graphql** es la carpeta donde guardaremos nuestros “objetos QL"
  * **data** es la carpeta donde tendremos algunos objetos de ejemplo que simulan registros de la base de datos

Vamos a comenzar con el objeto Movie (película), en la carpeta graphql creamos un nuevo archivo llamado movieQL.js

```javascript
import {  
GraphQLObjectType,  
GraphQLInt,  
GraphQLString,  
GraphQLList,  
GraphQLBoolean,  
GraphQLNonNull,  
GraphQLFloat,  
} from 'graphql';

import actorQL from './actorQL';  
import commentQL from './commentQL';

const movieQL = new GraphQLObjectType({  
name: 'movieQL',  
description: 'This is a movie QL object',  
fields: () => {  
return {  
name: {  
type: GraphQLString,  
resolve(movie) {  
return movie.name;  
}  
},  
score: {  
type: GraphQLFloat,  
resolve(movie) {  
return movie.score;  
}  
},  
year: {  
type: GraphQLInt,  
resolve(movie) {  
return movie.year;  
}  
},  
actors: {  
type: new GraphQLList(actorQL),  
resolve(movie) {  
return movie.actors;  
}  
},  
comments: {  
type: new GraphQLList(commentQL),  
resolve(movie) {  
return movie.comments;  
}  
},  
}  
}  
});

export default movieQL;
```

Como podemos observar al inicio estamos haciendo import de varios módulos que representan tipos de datos escalares en **graphQL**, adicionalmente hacemos import de otras 2 entidades de nuestra aplicación, [actorQL.js](https://github.com/Alevsk/graphql-demo-server/blob/master/graphql/actorQL.js) y [commentQL.js](https://github.com/Alevsk/graphql-demo-server/blob/master/graphql/commentQL.js), después en el atributo **fields** de nuestro objeto **movieQL** definimos varios campos del mismo junto con su tipo y aqui viene lo mas importante, definimos **actors** como una lista de tipo **actorQL** y **comments** como una lista de tipo **commentQL**, el código de las otras entidades es bastante similar al de **movieQL** por lo que no lo pondre en el post, pueden revisarlo en el repositorio: [actorQL.js](https://github.com/Alevsk/graphql-demo-server/blob/master/graphql/actorQL.js) y [commentQL.js ](https://github.com/Alevsk/graphql-demo-server/blob/master/graphql/commentQL.js)

## Queries y mutations

Otro de los conceptos básicos en graphQL son las **queries** y las **mutations**, existe toda una teoría detrás pero en resumen:

  * **Queries:** nos permiten leer datos del servidor (por lo general extraídos de una db) 
  * **Mutations:** Crear / modificar / borrar datos en el servidor

Dentro de la misma carpeta graphql vamos a crear 2 nuevos archivos, **queryQL.js** y **mutationQL.js**

```javascript
import {  
GraphQLObjectType,  
GraphQLList,  
GraphQLString,  
GraphQLInt,  
GraphQLBoolean  
} from 'graphql';

import movieQL from './movieQL';  
import { movies } from '../data';

const query = new GraphQLObjectType({  
name: 'Query',  
description: 'This is the root Query',  
fields: () => {  
return Object.assign({  
getMovies: {  
type: new GraphQLList(movieQL),  
args: {},  
resolve(root, args, request) {  
// do some db queries  
return movies;  
}  
},  
});  
},  
});

export default query;
```

Para efectos de que esto es un demo no estamos utilizando ningún orm para conectarnos a alguna base de datos, pero ustedes son libres de elegir e implementar el que mas le guste, de la misma forma que en **movieQL.js** definimos los fields aquí estamos definiendo nuestros “endpoints", por ejemplo estamos diciendo que getMovies es una query que nos regresara una lista de movieQL y estamos haciendo return del objeto movies (que es un objeto de ejemplo que importamos de la carpeta data).

De la misma forma dentro de **mutationQL.js** declaramos una operación llamada **createMovie** que nos retornara un objeto tipo movieQL (después de haberlo creado), la parte importante aquí es que por lo general los mutations reciben argumentos (name, year, score, lista de actores, lista de comentarios) y de nuevo, para efectos de que esto es un demo no estamos haciendo nada con los datos que nos enviá el usuario, simplemente los regresamos en la respuesta.

```javascript
import {  
GraphQLObjectType,  
GraphQLInt,  
GraphQLString,  
GraphQLNonNull,  
GraphQLList,  
GraphQLInputObjectType,  
GraphQLBoolean,  
GraphQLFloat,  
} from 'graphql';

import movieQL from './movieQL';

const actorInputQL = new GraphQLInputObjectType({  
name: 'actorInputQL',  
fields: {  
name: { type: GraphQLString },  
age: { type: GraphQLInt },  
country: { type: GraphQLString },  
},  
});

const commentInputQL = new GraphQLInputObjectType({  
name: 'commentInputQL',  
fields: {  
user: { type: GraphQLString },  
commentary: { type: GraphQLString },  
timestamp: { type: GraphQLString },  
},  
});

const mutation = new GraphQLObjectType({  
name: 'Mutation',  
description: 'This is the root Mutation',  
fields: () => {  
return Object.assign({  
createMovie: {  
type: movieQL,  
args: {  
name: {  
type: new GraphQLNonNull(GraphQLString),  
},  
year: {  
type: GraphQLInt,  
},  
score: {  
type: GraphQLFloat,  
},  
actors: {  
type: new GraphQLList(actorInputQL),  
},  
comments: {  
type: new GraphQLList(commentInputQL),  
},  
},  
resolve(root, args, request) {  
// do something here  
return args;  
},  
},  
});  
},  
});

export default mutation;
```

Hasta aquí ya tenemos definidos nuestros queries y mutations de ejemplo, ha llegado el momento de definir un schema de graphQL e integrar todo con express, es bastante sencillo, comenzamos creando un archivo llamado schemaQL.js también dentro de la carpeta graphql

```javascript
import { GraphQLSchema } from 'graphql';  
import queryQL from './queryQL';  
import mutationQL from './mutationQL';

const schemaQL = new GraphQLSchema({  
query: queryQL,  
mutation: mutationQL,  
});

export default schemaQL;
```

Como podemos ver, simplemente importamos los modulos de queryQL y mutationQL y finalmente en nuestro entry point (app.js) mandamos llamar a graphQL con el schema recién creado.

```javascript
import express from 'express';  
import GraphHTTP from 'express-graphql';  
import schemaQL from './graphql/schemaQL';

var app = express();

app.use('/graphiql', GraphHTTP({  
schema: schemaQL,  
pretty: true,  
graphiql: true  
}));

app.use('/graphql', GraphHTTP({  
schema: schemaQL  
}));

app.get('/', function (req, res, next) {  
const reponse = {  
message: 'hello world',  
};  
return res.json(reponse);  
});

module.exports = app;
```

Notaran que tenemos definidos 2 endpoints, **graphql** y **graphiql**. GraphiQL es una herramienta bastante útil que viene con el modulo de graphQL, se trata de una pequeña interfaz web desde donde podemos probar nuestras queries y mutations y la cual nos genera una documentación con base en los objetos QL de nuestro código, por ejemplo para probar nuestra query de **getMovies** seria algo como lo siguiente:

[![](/images/Screen-Shot-2017-11-12-at-10.57.31-PM-1122x800.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/screen-shot-2017-11-12-at-10-57-31-pm/)

Observen que del lado izquierdo estoy definiendo los atributos que quiero que contengan los objetos de la respuesta, puedo solicitar mas o menos dependiendo de lo que el cliente pida, ayudando bastante a, por ejemplo, reducir el tamaño de los mensajes si la petición se hace desde un cliente móvil.

[![](/images/Screen-Shot-2017-11-12-at-11.02.49-PM-1200x417.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/screen-shot-2017-11-12-at-11-02-49-pm/)
[![](/images/Screen-Shot-2017-11-12-at-11.03.04-PM-1200x320.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/screen-shot-2017-11-12-at-11-03-04-pm/)
[![](/images/Screen-Shot-2017-11-12-at-11.03.24-PM-1200x414.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/screen-shot-2017-11-12-at-11-03-24-pm/)

De la misma forma podemos probar nuestro mutation por medio de **graphiQL**

[![](/images/Screen-Shot-2017-11-12-at-11.10.28-PM-1200x781.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/screen-shot-2017-11-12-at-11-10-28-pm/)

Observen como desde el cliente podemos pasar directamente el objeto con sus atributos, incluso los objetos relacionados como la lista de actores y comentarios, ya es cuestión de procesar todo eso en nuestro backend y crear los registros en la base de datos.

Todo bien hasta el momento, ya sabemos utilizar graphiQL, ahora como usamos nuestra api ya en un proyecto real, muy sencillo, cada vez que hacemos un request en google developer toolbar podemos observar cual es el payload que se enviá al servidor:

[![](/images/Screen-Shot-2017-11-12-at-11.15.35-PM-1200x393.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/screen-shot-2017-11-12-at-11-15-35-pm/)

Podemos tomar ese mismo payload y con la ayuda de [POSTMAN](https://www.getpostman.com/) enviarlo como raw body a nuestro endpoint de **graphQL** en **/graphql** 

[![](/images/Screen-Shot-2017-11-12-at-11.14.50-PM-1125x800.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/screen-shot-2017-11-12-at-11-14-50-pm/)

Observa como el POST request va dirigido a **/graphql** y no **/graphiql**, por ultimo desde el mismo POSTMAN podemos ver cual seria el HTTP request generado haciendo clic en el boton **code**

[![](/images/Screen-Shot-2017-11-12-at-11.15.01-PM-986x800.png)](http://www.alevsk.com/2017/11/introduccion-a-graphql-queries-y-mutations/screen-shot-2017-11-12-at-11-15-01-pm/)

Finalmente lo único que queda es implementar ese request en tu lenguaje de programación / framework favorito, a continuación dejo la presentación que utilice durante el evento por si necesitan revisarla asi como el repositorio de github donde esta alojado el código de este demo: [graphql demo server](https://github.com/Alevsk/graphql-demo-server)
<div style="margin-bottom:5px">
<strong> [Introducción a GraphQL](//www.slideshare.net/Alevsk/introduccion-a-graphql) </strong> from <strong>[Lenin Alevski Huerta Arias](https://www.slideshare.net/Alevsk)</strong>
</div>
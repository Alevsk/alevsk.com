---
title: Implementación teórica con BlockChain para un sistema de votaciones
author: Alevsk
type: post
date: 2018-05-06T00:11:31+00:00
url: /2018/05/implementacion-teorica-con-blockchain-para-un-sistema-de-votaciones/
categories:
  - Geek
  - Javascript
  - Personal
  - Programming
  - Sin categoría
  - Snippets
  - Technology
  - Tutorials
tags:
  - bitcoin
  - blockchain
  - hacking
  - Javascript

---
[![](/images/blockchain-vote.jpg)](http://www.alevsk.com/2018/05/implementacion-teorica-con-blockchain-para-un-sistema-de-votaciones/blockchain-vote/)

Ha inicios de este año recibí un mensaje en Linkedin donde me preguntaban si estaba interesado en comenzar un proceso de reclutamiento, lo cual no es nada raro ya que siendo ingeniero de software (una de las industrias con más de profesionales en la actualidad) te llegan correos con propuestas laborales todos los días, sin embargo esta propuesta me pareció bastante interesante ya que necesitaban un **Senior BlockChain Engineer**, el mensaje en cuestión era:

[![](/images/Screen-Shot-2018-05-05-at-12.56.52-PM-727x800.png)](http://www.alevsk.com/2018/05/implementacion-teorica-con-blockchain-para-un-sistema-de-votaciones/screen-shot-2018-05-05-at-12-56-52-pm/)

Si bien no tengo experiencia desarrollando [BlockChain][1] como tal, si tengo bastante experiencia con sistemas distribuidos, así que me di a la tarea de comenzar a aprender el funcionamiento de esta tecnología desde un punto de vista técnico, sus conceptos básicos y sobre todo tratar de entender por que se volvió tan popular y sera el “futuro".

_Disclaimer: El código mostrado en el articulo a continuación no es una implementación real de BlockChain (no esta ni cerca del 1% de ser un proyecto real) la intención es resaltar y explicar las partes mas importantes y hacer hincapié en los conceptos básicos de lo que es BlockChain, el código dista de ser perfecto y no debe ser usado en producción._

Bueno ya estan advertidos hehe, comenzamos.

## El bloque

Para entender lo que es la cadena de bloques primero tenemos que entender lo que es un bloque, el bloque puede ser representado como un objeto que contiene un identificador único, un [timestamp][2], información en cualquier formato que queramos, un hash o [checksum][3] que representa la información que contiene y lo mas importante es que debe tener una referencia al bloque anterior, como si de una [lista enlazada][4] se tratara.

Con un lenguaje tan sencillo como Javascript podemos representar al bloque de la siguiente forma:

```javascript
class Block {  
constructor(index, timestamp, data, previousHash = ") {  
this.index = index;  
this.timestamp = timestamp;  
this.data = data;  
this.previousHash = previousHash;  
this.hash = this.calculateHash();  
}

calculateHash() {  
return SHA256(this.index + this.timestamp + JSON.stringify(this.data) + this.previousHash).toString();  
}  
}
```

La clase bloque contiene una función muy especial llamada **calculateHash**, esta función toma toda la información del bloque (index, timestamp, data, previousHash), la concatena y le aplica un algoritmo de hashing para generar un [checkSum][3] que despues sera almacenado en el mismo bloque, la parte interesante y una de las razones por las que **BlockChain** es seguro es precisamente el uso de estas funciones criptográficas, ya que su integridad esta respaldada de forma matemáticamente.

Detengamonos por unos segundos y pensemos, si todo bloque debe de tener una referencia al hash del bloque anterior, y ese dato (previousHash) se utiliza para calcular el hash del bloque actual eso significa que si alguien hackea/modifica/elimina uno de los bloques anteriores todos los siguientes bloques quedarían invalidados 🙂 , seria un efecto domino de fallas en la integridad de los bloques.

Esta es la representación mas básica que se me ocurre de un bloque, en la vida real son estructuras de datos mucho mas complejas y en la parte de los datos pueden contener muchísimas mas piezas de información y no solo una, como lo es el caso de las transacciones en la BlockChain de [Bitcoin][5].

## La cadena

Habiendo entendido un poco lo que es el bloque ahora toca el turno de la cadena, esta es otra estructura de datos que funciona alrededor de los bloques y realiza operaciones con ellos, mencione que esta tecnología es muy parecida a una lista enlazada, si el bloque es uno de los nodos entonces la cadena serian las operaciones de agregar, eliminar, modificar, etc nodos, aunque en BlockChain solo podemos agregar bloques y nunca eliminarlos por lo que mencionaba sobre la integridad de los hashes.

En Javascript podemos representar la cadena de la siguiente forma:

```javascript
class BlockChain {  
constructor() {  
this.chain = [this.createGenesisBlock()];  
}

createGenesisBlock() {  
return new Block(0, new Date(), "Genesis block");  
}

getLatestBlock() {  
return this.chain[this.chain.length – 1];  
}

addBlock(block) {  
block.previousHash = this.getLatestBlock().hash;  
block.hash = block.calculateHash();  
this.chain.push(block);  
}

isChainValid() {  
for(let i = 1; i < this.chain.length; i++) {  
const currentBlock = this.chain[i];  
const previousBlock = this.chain[i – 1];  
if (currentBlock.hash !== currentBlock.calculateHash()) {  
return false;  
}  
if(currentBlock.previousHash !== previousBlock.hash) {  
return false;  
}  
}  
return true;  
}  
}
```

Tenemos varias funciones interesantes como addBlock (agregar nuevo bloque), getLatestBlock (obtener el ultimo bloque), isChainValid (valida la integridad de la cadena de bloques) y **createGenesisBlock**, estas dos ultimas son las mas interesantes.

Mencione que cada bloque debe tener una referencia al bloque anterior ¿Pero entonces cuál fue el primer bloque 🙂 ?

Toda cadena de bloques inicia con un bloque llamado **[Bloque Genesis][6]**, ese nombre no es nada mas que una convención, es la forma de inicializar la cadena.

La función **isChainValid** verifica la integridad de la cadena utilizando los hashes de cada uno de los bloques, comienza revisando a partir del segundo bloque (uno después del bloque génesis) y primero revisa que el hash actual efectivamente corresponda con la información del bloque

```javascript
if (currentBlock.hash !== currentBlock.calculateHash()) {  
return false;  
}
```

Después revisa que la referencia (previousHash) al bloque anterior sea la correcta:

```javascript
if(currentBlock.previousHash !== previousBlock.hash) {  
return false;  
}
```

Así hasta llegar al ultimo bloque y si todo sale bien la cadena es valida :). Sin embargo si entendieron bien el concepto de verificación de integridad pueden ver el problema con esta implementación, si bien no es posible modificar la información de un bloque intermedio, teóricamente es posible “hackear" la información del ultimo bloque antes de que agreguen nuevos nodos a la cadena.

Este precisamente es el problema que se aborda en el primer paper de Bitcoin por [Satoshi Nakamoto][7]: [Bitcoin: A Peer-to-Peer Electronic Cash System][8]

Sin entrar en detalles, en implementaciones reales la cadena de bloques no se encuentra centralizada en una sola maquina, en lugar de eso es una red distribuida y todas las computadoras de la red contienen una copia completa de la cadena, entonces cada vez que alguien va a agregar un nuevo bloque toda la red tiene que consentir y finalmente ese bloque se almacena en las cadenas de todas las maquinas, sin embargo esta solución abre la posibilidad a nuevos tipos de ataques como por ejemplo el [double spend attack][9], aun así, teóricamente sigue siendo posible “hackear" la BlockChain pero para eso tendrías que modificar los últimos bloques de todas las maquinas de la red lo cual requiere una cantidad inmensa de recursos y por lo tanto no es factible.

## Ejemplo de BlockChain para votaciones

Habiendo aprendido los conceptos básicos ahora podemos pensar en como usar BlockChain para almacenar información referente a un sistema de votaciones, vamos a escribir unas cuantas pruebas en **Javascript** para probar nuestras dos clases, **Block** y **BlockChain**.

```javascript
it('Generate genesis block', () => {  
voteChain = new BlockChain();  
assert.lengthOf(voteChain.chain, 1);  
assert.equal(voteChain.chain[0].data, 'Genesis block');  
});
```

Con este test probamos que la cadena se inicializa y el bloque génesis es generado correctamente (la longitud de la cadena es 1 y data del primer bloque contiene el string 'Genesis block')

Ahora vamos a agregar unos cuantos bloques a la cadena

```javascript
it('Add some blocks', () => {  
voteChain.addBlock(new Block(1, new Date(), { user: 'Manuel', voted: 'PRI' }));  
voteChain.addBlock(new Block(2, new Date(), { user: 'Andres', voted: 'PAN' }));  
voteChain.addBlock(new Block(3, new Date(), { user: 'Julio', voted: 'PRD' }));  
voteChain.addBlock(new Block(4, new Date(), { user: 'Carlos', voted: 'PRI' }));  
voteChain.addBlock(new Block(5, new Date(), { user: 'Ruben', voted: 'PAN' }));  
voteChain.addBlock(new Block(6, new Date(), { user: 'Laura', voted: 'PRD' }));  
assert.lengthOf(voteChain.chain, 7);  
});
```

Estamos almacenando nombres de personas y el partido político mexicano por el que votaron, un bloque a la vez y al final verificamos que la longitud de la cadena es 7 (incluyendo el bloque génesis). En la vida real esto es mucho mas complicado ya que la gente no podría agregar bloques “solo por que si", al igual que con **Bitcoin** se utilizaría una tecnología de [PKI][10] (Infraestructura de llave publica) en donde cada transacción de voto deberá ser firmada usando la llave privada (como con la FIEL del SAT) de la persona que emite su voto, de esa manera nadie podría votar a nombre de alguien mas.

Ahora tenemos nuestro test para verificar la integridad de la BlockChain, si la cadena es valida esperaríamos que la función **isChainValid** nos devolviera **true**.

```javascript
it('Validate chain integrity', () => {  
assert.isOk(voteChain.isChainValid(), 'Block hashes are incorrect'); // this should return true  
});
```

Observen como en cada uno de los bloques el valor de **previousHash** es identico al **hash** del bloque anterior

[![](/images/Screen-Shot-2018-05-05-at-6.53.02-PM-771x800.png)](http://www.alevsk.com/2018/05/implementacion-teorica-con-blockchain-para-un-sistema-de-votaciones/screen-shot-2018-05-05-at-6-53-02-pm/)

En la ultima prueba simulamos que alguien modifico el voto de alguien mas, para eso tomamos de forma aleatoria un bloque y cambiamos el valor de su **data** por el nombre de otro partido político.

```javascript
it('Changing random data in the BlockChain', () => {  
const min = 0; // first block id  
const max = 5; // for academic purpose this cannot be 6 (the last block id) due to double spend attack  
const blockId = Math.floor(Math.random() * (max – min + 1) + min); // https://stackoverflow.com/questions/4959975/generate-random-number-between-two-numbers-in-javascript  
const block = voteChain.chain[blockId];  
block.data = { user: block.data.user, voted: 'MORENA' }; // Changing block value  
block.hash = block.calculateHash(); // Re calculate the current block hash so no one notices the hack  
assert.isNotOk(voteChain.isChainValid(), 'Block hashes are incorrect'); // this should return false  
});
```

[![](/images/Screen-Shot-2018-05-05-at-6.58.02-PM-1137x800.png)](http://www.alevsk.com/2018/05/implementacion-teorica-con-blockchain-para-un-sistema-de-votaciones/screen-shot-2018-05-05-at-6-58-02-pm/)

El test, de forma aleatoria, tomo el bloque con **index 2** y cambio los valores que tenia en **data** y eso hizo que el hash resultante de ese bloque cambiara completamente.

hash antes del cambio:  
**9ecbe54e3e6b3f22a522bbee7f399002f1de2d653c15a74d2d321f27cdfe116b**

hash después del cambio:  
**3e6c8f5c0a734db4bb19483a11022081250171621e5c5c17c21a302d1d9d14d0**

Por lo tanto el **previousHash** del bloque **index 3** ya no coincide con el del bloque **index 2**.

Debido a este cambio la validación de integridad de la cadena fallara (siempre y cuando no modifiquemos los datos del ultimo bloque) y **isChainValid()** nos devolverá **false**.

Y eso es todo por ahora, finalmente si quieren descargar este sencillo código para verlo mas a detalle o simplemente para tenerlo lo pueden hacer desde el siguiente repositorio de github [alevsk blockchain javascript][11] con los siguientes comandos

```bash
$ git clone https://github.com/Alevsk/blockchain-javascript  
$ cd blockchain-javascript  
$ npm install  
$ mocha index.test.js
```

[![](/images/Screen-Shot-2018-05-05-at-5.36.40-PM-1006x800.png)](http://www.alevsk.com/2018/05/implementacion-teorica-con-blockchain-para-un-sistema-de-votaciones/screen-shot-2018-05-05-at-5-36-40-pm/)

## Resumen

**BlockChain** nos ofrece ante todo integridad de la información, nos asegura que la información no puede ser cambiada ni eliminada sin que nos demos cuenta, ademas por su naturaleza de ser un sistema distribuido es virtualmente imposible hackear la red, esta tecnología aplicada a un sistema de votaciones nos garantiza que algo como el robo de votos no puede ocurrir y tendríamos total transparencia en las votaciones.

Si quieren aprender mas sobre esta tecnología les recomiendo ver este video en donde se explica con mucho mas detalle como funciona Bitcoin y la BlockChain en general, se abordan muchísimos mas conceptos de los que mencione en este articulo.



Happy hacking 🙂

 [1]: https://es.wikipedia.org/wiki/Cadena_de_bloques
 [2]: https://es.wikipedia.org/wiki/Marca_temporal
 [3]: https://es.wikipedia.org/wiki/Suma_de_verificaci%C3%B3n
 [4]: https://es.wikipedia.org/wiki/Lista_enlazada
 [5]: https://es.wikipedia.org/wiki/Bitcoin
 [6]: https://es.bitcoin.it/wiki/Bloque_G%C3%A9nesis
 [7]: https://es.wikipedia.org/wiki/Satoshi_Nakamoto
 [8]: https://bitcoin.org/bitcoin.pdf
 [9]: https://bitcoin.stackexchange.com/questions/4974/what-is-a-double-spend
 [10]: https://es.wikipedia.org/wiki/Infraestructura_de_clave_p%C3%BAblica
 [11]: https://github.com/Alevsk/blockchain-javascript
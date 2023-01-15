---
title: Análisis y solución de un wargame de Criptografia
author: Alevsk
type: post
date: 2011-08-07T18:59:48+00:00
url: /2011/08/analisis-y-solucion-de-un-wargame-de-criptografia/
categories:
  - C y C++
  - Geek
  - Ethical Hacking
  - Java
  - Javascript
  - Jquery
  - Programming
  - Tutorials
tags:
  - backtrack
  - debian
  - grep
  - grub
  - Hello world
  - Hello World
  - Linux
  - Programming
  - Solutions
  - Technology
  - Tutorials

---
[![](/images/hacker.jpg)](http://www.alevsk.com/2011/08/analisis-y-solucion-de-un-wargame-de-criptografia/hacker/)

Bueno no se si sera exactamente **criptografia** x'D (mas bien es como resolver el acertijo), les comento lectores, ayer sábado estaba terminando algunos pendientes del trabajo y quise hechar un vistazo a ver como iba la **comunidad** de [diosdelared][1], para los que no lo saben **diosdelared** es una comunidad de **seguridad informatica** con la característica de que tiene incluido un sistema de rangos y wargames, conforme vas solucionando mas retos vas avanzando de rango :).

Tengo mi cuenta ahi desde algunos meses o años ya.

Recordando la sección de retos informáticos (wargames) me apeteció ponerme a resolver uno antes de salir al cine a ver capitan america :p, como tenia algo de ganas de pensar en logica elegi el que se llama **Valid Token**, hasta aqui quiero comentarles que mostrare paso por paso como se soluciona el reto, así que si eres miembro ya de la comunidad o te gustaría serlo y pasar los retos intelectuales te recomiendo que lo intentes por ti mismo en un principio :).

Como ya es característico, el reto comienza con un texto que te hace sentir como si fueras algún ciber agente de la **NSA** o de la **CIA** xD (Murder siempre tan dramático).

Ok las instrucciones dicen lo siguiente:

> Tenemos acceso al E-Mail de un administrador de SafePoint. Hemos podido recuperar su usuario y contraseña y una serie de Tokens.  
> El problema es que estas tokens se caducan tras ser usadas y según hemos confirmado, el algoritmo de generación cambia mensualmente.  
> Por si te sirve, hemos encontrado lo siguiente.  
> Ayudanos a generar un token valido y recibirás tu recompensa.  
> El usuario y contraseña que conseguimos es:  
> $email == 'admin@safepoint' && $password == 'one2one'
> 
> Suerte en tu misión.

mas abajo hay un link que nos dirige al siguiente panel de login:

[![](/images/Captura-de-pantalla-2011-08-07-a-las-12.16.03.png)](http://www.alevsk.com/2011/08/analisis-y-solucion-de-un-wargame-de-criptografia/captura-de-pantalla-2011-08-07-a-las-12-16-03/)

En las instrucciones se nos proporciona un usuario y una contraseña, pero nos falta un token (como sacamos el maldito token x'D?), entonces procedemos a descargar el archivo, que se supone es un archivo robado del generador de tokens :p

```ECL
prefix_token, $token);
		$string = $string_explode_array[1];
		return $string;
		}
	public function CheckToken($token)
		{
		$test_token = $this->TokenCalculate($this->DebugToken($token));
		if($test_token == $this->valid_algorithm)
			{
      echo "verdadero";
			return true;
			}
		else
			{
      echo "falso";
			return false;
			}
		}
	}

```

Y comenzamos el análisis del código.

Vemos que tenemos 3 metodos en la clase, 2 privados (DebugToken, TokenCalculate ) y el otro publico (CheckToken), partimos del hecho de que como es publica sera la función que nos diga si nuestro token es valido o no (ademas el nombre es muy obvio no xd?).

```ECL
public function CheckToken($token)
		{
		$test_token = $this->TokenCalculate($this->DebugToken($token));
		if($test_token == $this->valid_algorithm)
			{
      echo "verdadero";
			return true;
			}
		else
			{
      echo "falso";
			return false;
			}
		}

```

La función recibe un parametro que después es pasado al metodo privado DebugToken, veamos su código entonces.

```ECL
private function DebugToken($token)
		{
		$string_explode_array = explode($this->prefix_token, $token);
		$string = $string_explode_array[1];
		return $string;
		}

```

Al igual que el primer metodo este tambien recibe un parametro solamente, comenzando tenemos una variable que recibe el valor resultante aplicar la función [explode][2], para los que no saben explode te permite cortar una cadena en varias partes utilizando una expresion como delimitador, en este caso **$this->prefix_token**, al inicio de la clase esta declarada esta variable:

```Text only
private $prefix_token = 'ddlr-'; 
```

Llegados a este punto sabemos que el token contiene si o si la sub cadena ddlr- :p, ¿por que? pues por que en la función DebugToken después de utilizar explode se le asigna a la variable $string el contenido del arreglo $string\_explode\_array en la posición 1, la posición 0 quedo vacía puesto que no había nada antes de **ddlr-** al final $string es devuelto un nivel mas arriba, ósea a la función **CheckToken**.

Recordemos que teníamos algo así como

```ECL
$test_token = $this->TokenCalculate($this->DebugToken($token));
```

Entonces el resultado de DebugToken ($string) es pasado directamente a TokenCalculate, veamos el metodo.

```Tera Term macro
private function TokenCalculate($string)
		{
		$md5_1 = md5($string[0]);
		$md5_2 = md5($string[1]);
		$md5_3 = md5($string[2]);
		$md5_4 = md5($string[3]);
		$md5_5 = md5($string[4]);
		$token = ord($md5_1).'-'.ord($md5_2).'-'.ord($md5_3).'-'.ord($md5_4).'-'.ord($md5_5);
		return $token;
		}

```

Al igual que los 2 metodos anteriores recibe solo un parámetros, del cual extra los caracteres individualmente y obtiene su hash en md5, después de eso guarda el resultado de todos las variable que contiene el md5 de cada caracter en la variable $token y les asigna un '-' entre cada valor.

Hay vemos algo interesante, mientras se hace la concatenación se le aplica el metodo [ord][3], lo que hace ord es tomar el primer caracter de una cadena y regresar su equivalente en ascii, al final la cadena $token es regresada.

Regresando a nuestro metodo original (CheckTone), ya ven que esto es como inception x'D, el resultado de todo eso es asignado en $test_token y abajo hay una comparación interesante

```ECL
if($test_token == $this->valid_algorithm)

```

Nos esta diciendo que si nuestra cadena resultante es $this->valid_algorithm, que al inicio es declarado

```Text only
private $valid_algorithm = '56-101-52-51-56';

```

Entonces nuestro token es valido, de lo contrario es invalido :).

Ahora, después de este análisis ¿por donde comenzamos?, ¿nuestro $test\_token tiene que ser igual a $this->valid\_algoritm verdad?, una vez que sabemos como se construye la cadena y como funciona el algoritmo procedemos a aplicar **ingeniería inversa** o resolver el acertijo … vaya :).

Lo primero que tenemos que hacer es ver cual es el valor de los números ascii, ¿por que?, pues como ya habíamos dicho arriba, si no recuerdas regresa a leer xd, el ultimo paso era aplicar la función ord que devuelve el ascii del primer caracter de una cadena, en este caso los hash en md5.

Los valores son:

```Scilab
/*

  56-101-52-51-56

  56 = 8
  101 = e
  52 = 4
  51 = 3
  56 = 8

  8-e-4-3-8

  */

```

¿Ahora que hacemos? tenemos que confiar en que el creador del wargame no se paso mucho de listo y generar todos los md5 que comiencen con dichos caracteres **(8-e-4-3-8)**, usando las letras del abecedario y los números del 0-9 (por eso dije que no se haya pasado de listo y haya utilizando caracteres raros jaj)

Tengo un arreglo ya preparado

```Text only
$abc = array('@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[',']','^','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~');

```

Imprimo las cadenas hash resultantes que coincidan con nuestro patron de búsqueda.

```Tera Term macro
for($i = 0; $i < count($abc); $i++)
  {
    switch(substr(md5($abc[$i]),0,1))
    {
      case '8':
      echo $abc[$i]." : ".md5($abc[$i])."";
      break;
      
      case 'e':
      echo $abc[$i]." : ".md5($abc[$i])."";
      break;
      
      case '4':
      echo $abc[$i]." : ".md5($abc[$i])."";
      break;
      
      case '3':
      echo $abc[$i]." : ".md5($abc[$i])."";
      break;
    }

```

Y el resultado es (ya organizados)

```Scilab
/*
8-e-4-3-8

= 8 = 

F : 800618943025315f869e4e1f09471012
N : 8d9c307cb7f3c4a32822a51922d1ceaa
[ : 815417267f76f6f460a4a61f9db75fdb
` : 833344d5e1432da82ef02e1301477ce8
d : 8277e0910d750195b448797616e091ad
f : 8fa14cdd754f91cc6554c9e71929cce7
i : 865c0c0b4ab0e063e5caa3387c1a8741
k : 8ce4b16b22b58894aa86c421e8759df3
p : 83878c91171338902e0fe0fb97a8c47a

= e =

R : e1e1d3d40573127e9ee0480caf1283d6
e : e1671797c52e15f763380b45e841ec32
t : e358efa489f58062f10dd7316b65649e

= 4 =

P : 44c29edb103a2872f519ad0c9a0fdaaa
U : 4c614360da93c0a041b22e537de151eb
c : 4a8a08f09d37b73795649038408b5f33
r : 4b43b0aee35624cd95b910189b3dc231
y : 415290769594460e2e485922904f345d
~ : 4c761f170e016836ff84498202b99827

= 3 =

E : 3a3ea00cfc35332cedf6e5e9a32e94da
j : 363b122c528f54df4a0446b6bab05515
*/

```

Hagamos cuentas para ver cuantas contraseñas posibles podríamos generar x'D, **9 \* 3 \* 6 * 2** = 324 contraseñas posibles xD, no podemos utilizar fuerza bruta por que el **server** nos banearia así que, una vez mas una prueba de fe, armamos nuestra cadena que corresponda a **8-e-4-3-8** tomando los primeros resultados y queda 

```Scilab
/*
8 = F
e = R
4 = P
3 = E
8 = N (la segunda letra correspondiente a los hash que comienzan con 8)

FRPEN
*/

```

Por ultimo le agregamos el '**ddlr-**' quedando '**ddlr-FRPEN**'.

Ahora probamos, tan solo le pasamos el token que creemos es el correcto al metodo de la clase.

```ECL
$testing = new Crypt0reto();
 $testing->CheckToken("ddlr-FRPEN");

```

Y voilà el metodo nos regresa verdadero :), lo probamos en el formulario junto con el correo y la contraseña y efectivamente nos deja entrar al panel y superamos el reto :).

salu2

**PD**  
Este tipo de retos me gustan mucho, me tomo 12 minutos entenderle y hacer la **ing inversa**, tal vez algunos lo hicieron mas rapido y mas lento, eso no importa lo importantes es tener algo para ejercitar la mente x'D

**PD 2**  
Cada reto dice el numero de personas que lo han superado, este wargames han sido alrededor de 40 personas los que lo han pasado, quiero pensar que es por que no saben programar jeje

 [1]: http://diosdelared.com
 [2]: http://php.net/manual/es/function.explode.php
 [3]: http://php.net/manual/es/function.ord.php
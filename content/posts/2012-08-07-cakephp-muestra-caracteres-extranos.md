---
title: CakePHP muestra caracteres extraños
author: Alevsk
type: post
date: 2012-08-07T21:54:12+00:00
url: /2012/08/cakephp-muestra-caracteres-extranos/
categories:
  - Programming
  - Snippets
  - Tutorials
tags:
  - cakePHP
  - Programming
  - software libre
  - Solutions
  - web

---
Con este snippet de código puedes solucionar el problema de por que **CakePHP muestra caracteres extraños**, por lo general el problema se presenta cuando nuestra base de datos tiene almacenados caracteres latinos (como ñ, ó, á, etc). La solución es bastante simple, tan solo tenemos que ubicar nuestro archivo de conexión **database.php** que se encuentra en **webapp/app/config/database.php** abrirlo y agregar una línea de código, quedando su contenido de la siguiente manera.

```php
<?php  
class DATABASE_CONFIG {

var $default = array(  
'driver' => 'mysql',  
'persistent' => false,  
'host' => 'host',  
'login' => 'user_name',  
'password' => 'user_password',  
'database' => 'database',  
'prefix' => ",  
'encoding' => 'utf8'  
);

}  
?>
```

salu2
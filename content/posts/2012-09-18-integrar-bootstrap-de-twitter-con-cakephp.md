---
title: Integrar bootstrap de twitter con CakePHP
author: Alevsk
type: post
date: 2012-09-18T02:50:50+00:00
url: /2012/09/integrar-bootstrap-de-twitter-con-cakephp/
categories:
  - HTML
  - Javascript
  - Jquery
  - Programming
  - Tips
  - Tutorials
tags:
  - cakePHP
  - CSS
  - Jquery
  - Programming
  - software libre
  - Solutions
  - Technology
  - Tutorials
  - twitter
  - web

---
[![](/images/cakephp_bootstrap.jpg)](http://www.alevsk.com/2012/09/integrar-bootstrap-de-twitter-con-cakephp/cakephp_bootstrap/)  
**Bootstrap de twitter** es un poderoso framework para diseñar front-end es por eso que hoy en día muchos desarrolladores web lo utilizan, en este sencillo tutorial aprenderás a **integrar bootstrap con CakePHP**.

  * Lo primero que tenemos que hacer es descargar la ultima versión del framework (**cakePHP**) [aquí](http://cakephp.org/) he instalarlo (si no tienes idea de como hacerlo hecha un vistazo a este tutorial [Configurar servidor web en ubuntu 10.04 e instalar CakePHP](http://www.alevsk.com/2010/12/configurar-servidor-web-en-ubuntu-10-04-e-instalar-cakephp-1/))
  * Después tambien tenemos que descargar la ultima versión de **twitter bootstrap** [aquí](http://twitter.github.com/bootstrap/)

Al descomprimir la carpeta de bootstrap nos encontraremos con 3 directorios en su interior:

```php
/*  
bootstrap  
├── css  
│ ├── bootstrap-responsive.css  
│ ├── bootstrap-responsive.min.css  
│ ├── bootstrap.css  
│ └── bootstrap.min.css  
├── img  
│ ├── glyphicons-halflings-white.png  
│ └── glyphicons-halflings.png  
└── js  
├── bootstrap.js  
└── bootstrap.min.js  
*/
```

Si ya tienes algo de experiencia con cakephp sabrás que en el framework existe la carpeta **webroot**, que es exactamente a donde tenemos que copiar estos archivos, la estructura de directorios y archivos dentro **webroot** debe de quedar algo así:

```php
/*  
webroot/  
├── css  
│ ├── bootstrap-responsive.css  
│ ├── bootstrap-responsive.min.css  
│ ├── bootstrap.css  
│ ├── bootstrap.min.css  
│ └── cake.generic.css  
├── favicon.ico  
├── files  
│ └── empty  
├── img  
│ ├── cake.icon.png  
│ ├── cake.power.gif  
│ ├── glyphicons-halflings-white.png  
│ ├── glyphicons-halflings.png  
│ ├── test-error-icon.png  
│ ├── test-fail-icon.png  
│ ├── test-pass-icon.png  
│ └── test-skip-icon.png  
├── index.php  
├── js  
│ ├── bootstrap.js  
│ ├── bootstrap.min.js  
│ └── empty  
└── test.php  
*/
```

Nota como ahora los archivos de bootstrap están en sus respectivos directorios (css, img y js), ahora estamos listos para mandar llamar los archivos en nuestro **default.ctp**

Abrimos el archivo default.ctp para modificarlo (se encuentra en **app/View/Layout/default.ctp**) y buscamos la siguiente porción de código:

```php
<?php  
echo $this->Html->meta('icon');

echo $this->Html->css('cake.generic');

echo $this->fetch('meta');  
echo $this->fetch('css');  
echo $this->fetch('script');  
?>
```

y las modificamos por estas (solo agregamos las llamadas al css y el js de bootstrap):

```php
<?php  
echo $this->Html->meta('icon');  
echo $this->Html->css('bootstrap');  
echo $this->html->script('bootstrap');  
echo $this->fetch('meta');  
echo $this->fetch('css');  
echo $this->fetch('script');  
?>
```

Y eso es todo!, podrás comenzar a desarrollar **front-end con bootstrap en CakePHP** :), yo he copiado el código fuente del ejemplo que nos pone el bootstrap en su sitio en mi layout.ctp para ver que todo funciona bien, el resultado fue:

[![](/images/bootstrap_plus_cakephp.jpg)](http://www.alevsk.com/2012/09/integrar-bootstrap-de-twitter-con-cakephp/bootstrap_plus_cakephp/)
---
title: Utilizar ReCaptcha en CakePHP
author: Alevsk
type: post
date: 2011-09-03T02:31:55+00:00
url: /2011/09/utilizar-captcha-en-cakephp/
categories:
  - Programming
  - Snippets
  - Tutorials
tags:
  - cakePHP
  - Programming
  - Social Media
  - slackware
  - software libre
  - Solutions
  - Technology
  - Tutorials
  - web

---
[![](/images/Captura-de-pantalla-2011-09-02-a-las-21.25.36.png)](http://www.alevsk.com/2011/09/utilizar-captcha-en-cakephp/captura-de-pantalla-2011-09-02-a-las-21-25-36/)

Seguramente muchos de ustedes ya sabrán de que va todo esto pero para los que no, ReCaptcha es un servicio que nos permite implementar captchas (software para detección de bots) en nuestras aplicaciones web y que fue adquirido por google hace algún tiempo ya.

Entonces en este post aprendermos a **utilizar captcha en cakephp**, los captchas son muy importantes a la hora de manejar formularios, así nos aseguramos que los datos que entran son escritos realmente por un ser humano y no por un bot (aunque no es 100% aun).

Ok manos a la obra, lo primero que tienen que hacer es dar de alta su cuenta para obtener una key en el siguiente sitio [ReCaptcha][1]

[![](/images/Captura-de-pantalla-2011-09-02-a-las-19.52.53.png)](http://www.alevsk.com/2011/09/utilizar-captcha-en-cakephp/captura-de-pantalla-2011-09-02-a-las-19-52-53/)

Atención, estoy obviando la parte de que ustedes ya están familiarizados con el framework [CakePHP][2] y por lo tanto saben lo que es un controlador, una vista, un componente, un helper, el AppController, etc :), aun así el espacio de comentarios hasta abajo estará destinado a resolver las dudas que puedan surgir.

Primero tienen que [descargar el componente y el helper del reCaptcha][3], yo he subido los archivos a megaupload (son los que me funcionan perfectamente jeje) pero si uds quieren puedes buscarlos en google.

<div class="demobox" style="margin-top: 10px; height:auto;">
[ ![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/download.png) ](http://www.megaupload.com/?d=ODF53GU1)
</div>

Descompriman el archivo en su proyecto de cakePHP, al final les debería de quedar el archivo **recaptcha.php** en **controllers/components/** y el helper **recaptcha.php** en la ruta **views/helpers/** dentro de la carpeta de su aplicación.

Para este ejemplo yo tengo un **controlador** llamado **links** (links_controller.php es mi archivo), dentro del mismo hago la declaración de los componentes y los helpers que utilizare con el siguiente código:

```Objective-C




  Con esas 2 instrucciones le indicamos a CakePHP que utilizaremos el componente y el helper de ReCaptcha (los archivos que previamente descargaron y colocaron en sus respectivos lugares) después también escribí un método llamado go (si, este es el código de una [aplicación](http://www.alevsk.com/2011/06/un-proyecto-de-la-noche-a-la-manana/) que hice llamada [Easylink Share](http://protector.alevsk.com/)), el código del método es el siguiente:




public function go($key = null)
  {
    $this->layout = 'redirect';
    if(empty($key) && empty($this->data))
    {
      /*$this->msg_result = "link_noexist";
		  $this->Session->setFlash(__($this->msg_result, true), 'default');*/
		  $this->redirect(array('controller' => 'pages', 'action' => 'view', '404-no-existe-el-link'));
    }

    if($register = $this->Link->find('first',array('conditions' => array('Link.active' => '1', 'Link.key' => $key))) or 
          $register = $this->Link->find('first',array('conditions' => array('Link.active' => '1', 'Link.key' => $this->data['Link']['key']))))
    {
       //Si los datos que trae el form no son nulos
       if(!empty($this->params['form']))
       {
          //Esta es la parte mas importante, aqui es donde se valida que el código que trae el formulario es el correcto
          if(!$this->Recaptcha->valid($this->params['form']))
	        {
		          $this->redirect(array('action' => 'go',$register['Link']['key']));
	        }
          else
          {
              $this->redirect($register['Link']['url']);
          }
       }
       else
       {
          $this->set('register', $register);
       }
    }
    else
    {
      $this->redirect(array('controller' => 'pages', 'action' => 'view', '404-no-existe-el-link'));
    }
  }





  Para hacer mas entendible el código anterior, esta es la parte mas importante de la validación:




if(!$this->Recaptcha->valid($this->params['form']))
	        {
		          //Si el captcha no es correcto hacer esto
	        }
          else
          {
              //Si el captcha si esta correcto hacemos esto otro
          }




  El código de tu vista (go.ctp) que incluye el formulario se debe de ver algo parecido a lo siguiente:









  Como ven donde se manda llamar el formulario es en la parte de: 




display_form('echo'); ?>




  Tan solo agregar un botón de enviar y entonces lo que coloquemos será enviado y validado por nuestro controlador (el que mostré anteriormente :)).




  Y listo, así de fácil se implementa ReCaptcha en CakePHP


 [1]: https://www.google.com/recaptcha
 [2]: http://www.alevsk.com/?s=cakephp&x=0&y=0
 [3]: http://www.megaupload.com/?d=ODF53GU1
```
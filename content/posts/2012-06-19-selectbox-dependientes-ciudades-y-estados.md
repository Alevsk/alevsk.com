---
title: SelectBox dependientes – ciudades y estados
author: Alevsk
type: post
date: 2012-06-19T07:02:06+00:00
url: /2012/06/selectbox-dependientes-ciudades-y-estados/
categories:
  - CSS
  - HTML
  - Javascript
  - Jquery
  - Programming
  - Snippets
  - Tutorials
tags:
  - Javascript
  - Jquery
  - Programming
  - software libre
  - Solutions
  - Technology
  - Tutorials

---
[![](/images/ajax-jquery.png)](http://www.alevsk.com/2012/06/selectbox-dependientes-ciudades-y-estados/ajax-jquery/)

Retomando los post sobre programación web en esta ocasión les comparto un rápido ejemplo sobre **selectbox dependientes**, mas concretamente el ejemplo de **selectbox de ciudades y estados**. Básicamente tenemos 2 selectbox, el primero contendrá los estados de la republica mexicana, cuando seleccionamos alguno el segundo selectbox contendrá ahora las ciudades de ese estado, para hacer esto necesitamos una pequeña base de datos con 2 tablas (ciudades y estados .. obvio), después algo de código php que se encargue de hacer la conexión y otro mas que nos devuelva los datos de las consultas vía **JSON** y por ultimo nuestro **html** y **javascript** que se encargara de mostrar el resultado. 

Al terminar el tutorial tendremos algo que se vera así 🙂

<div class="demobox">
[![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/download.png)](http://sdrv.ms/M9sEGc)[![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/demo.png)](http://www.alevsk.com/proyectos/estados_ciudades/)
</div>

Puedes descargar los archivos que se utilizara en la practica a continuación.

<div class="demobox" style="height:auto">
<ul>
<li>
[index.html – selectbox dependientes](http://www.copypastecode.com/244371/)
</li>
<li>
[data.php – selectbox dependientes](http://www.copypastecode.com/244378/)
</li>
<li>
[mysql.php – selectbox dependientes](http://www.copypastecode.com/244389/)
</li>
<li>
[estados_ciudades.sql – selectbox dependientes](hhttp://www.copypastecode.com/244397/)
</li>
</ul>
</div>

Comenzamos pues :).

Comenzamos creando el archivo que hará la conexión a la **base de datos**, yo acostumbro hacer una clase para eso ya que luego puedo hacer extends de la misma y todo es mas fácil.

```Tera Term macro
ID);
	}
	
	function _last_id(){
		global $ID_BD;
			return	mysql_insert_id($ID_BD);
	}
}	


?>


```

Después creamos el archivo que se encargara de hacer las consultas y regresar el **JSON** correspondiente, realizaremos peticiones a este archivo via ajax por medio de **jquery**.

```verilog
_registers("SELECT * FROM states;");
    return json_encode($states);
  }

  function getCities($idState)
  {
    $idState = (int) $idState;
    $cities = $this->_registers("SELECT * FROM cities WHERE id_state = " . $idState . ";");
    return json_encode($cities);
  }
}

  $data = new data();
  if($_GET['action'] == "getStates")
  {
    echo $data->getStates();
  }
  else if($_GET['action'] == "getCities" && isset($_GET['stateID']))
  {
    echo $data->getCities($_GET['stateID']);
  }

?>


```

Como podemos ver he empaquetado el código en una clase y casi en la parte final del código reviso si existen algunos parámetros pasados por GET para mandar llamar a las funciones correspondientes :), examinemos por ejemplo la función que nos trae los estados: ```Transact-SQL
 

Básicamente hacemos un select y el arreglo asociativo resultante (checar la clase **mysql** para mas información) lo pasamos por **json_encode** para ser manipulado con javascript, lo mismo pasa con la función que te arroja las ciudades solo que esa tiene una clausula WHERE que te manda traer solo las ciudades de X estado :).

Finalmente creamos nuestro archivo html donde desplegaremos los 2 selectbox, para eso escribimos el siguiente código.






[Selecciona un estado](#)




[Selecciona una ciudad](#)








  







Como pueden ver, al inicio cargamos la librería de **JQuery** desde google, después hacemos la primera petición al script data.php via **ajax** para que nos traiga los estados y poder “rellenar el primer selectbox", después tenemos el siguiente código javascript.

$('#states').change(function() {
      $.ajax({
        url: 'data.php?action=getCities&stateID=' + $('#states').val(),
        dataType: 'json',
        success: function(data) {
          var size = Object.size(data);
          var items = "";
          for(var i = 0; i < size; i++)
          {
            items = items + '' + data[i].name + '';
            //console.log(data[i].id_state + " : " + data[i].name);
          }  
          $('#cities').html("");
          $('#cities').append(items);
          $('#cities').change();
        }
      });      
     });



change() nos permite detectar el cambio de selección de un selectbox, entonces utilizamos ese evento para “refrescar" las opción del segundo selectbox, vemos cual es el estado que esta seleccionado, extraemos su valor (es el mismo id que le corresponde en la tabla de estados) y armamos la petición para mandar traer las ciudades :).

Y listo con esto tenemos listo un mini ejemplo de selectbox dependientes, espero les sirva este pequeño snippet :), ya saben cualquier duda pónganla en comentarios.

La verdad es un código bastante sencillo y fácil de implementar (unos 10 mins a lo mucho), con un poco mas de código se podría mostrar la ubicación de la ciudad en **google maps** o utilizar esto en algún **formulario de registro** o cualquier otra cosa.

salu2
```
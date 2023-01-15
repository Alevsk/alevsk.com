---
title: Google weather API y PHP
author: Alevsk
type: post
date: 2011-03-08T20:26:14+00:00
url: /2011/03/google-weather-api-y-php/
categories:
  - CSS
  - Diseño
  - Linux
  - Personal
  - Programming
  - Technology
  - Tutorials
tags:
  - php
  - Programming
  - software libre
  - Solutions
  - Technology
  - ubuntu
  - web

---
[![](/images/weather.png)](http://www.alevsk.com/2011/03/google-weather-api-y-php/weather/)

Hace un par de días un internauta me pregunto sobre si era posible hacer una web que mostrar las ciudad mas importantes del país así como el clima “actual" de la región, haciendo uso de servicios ya existentes que presten este tipo de información, pues me puse a investigar y encontré una aplicación muy buena de **Google** llamada [Google Weather][1], la cual tiene a disposición de los programadores una **API** muy bien documentada y fácil de usar e implementar.

Hace rato que tenia un tiempo libre me puse a ver lo que se podia hacer e hice un pequeño ejemplo, un formulario donde escribes el nombre de una ciudad, Ej. **Guadalajara, Morelia, Queretaro** y haciendo uso de **Google Weather** te muestra el clima de hoy así como el clima de los siguientes 4 días :), la verdad es muy fácil de usar, a continuación les dejo el código.

[![](/images/screenshot12.png)](http://www.alevsk.com/2011/03/google-weather-api-y-php/screenshot1-3/)
```Transact-SQL

	


xpath("/xml_api_reply/weather/forecast_information");
$current = $xml->xpath("/xml_api_reply/weather/current_conditions");
$forecast_list = $xml->xpath("/xml_api_reply/weather/forecast_conditions");
?>

    
    
        


  city['data']; ?>

        


  El clima de hoy
 
        


  ![weather](icon['data']?>)
              
  
  
              temp_f['data'] ?>° F,
              
  
  condition['data'] ?>
              
          

        


  Forecast

        


        


  ![weather](icon['data']?>)
              
  
  
    day_of_week['data']; ?>
  
              
  
  
  	            low['data'] ?>° F - 
  
  high['data'] ?>° F,
  	            
  
  condition['data'] ?>
              
          
	
        


        ... 


  [Regresar <<](weather.php?phpMyAdmin=3068b5491f703bc27d2a43326f772556)

    






```

Si no aparece correctamente el codigo aqui en el blog (como es de costumbre) aca les deje el codigo en copypastecode.com … http://www.copypastecode.com/65593/

salu2

 [1]: http://www.google.com/Top/News/Weather/
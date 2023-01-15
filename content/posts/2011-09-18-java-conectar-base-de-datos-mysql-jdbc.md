---
title: Conexiones simples a mysql con JDBC en Java
author: Alevsk
type: post
date: 2011-09-18T07:34:52+00:00
url: /2011/09/java-conectar-base-de-datos-mysql-jdbc/
categories:
  - Java
  - Programming
  - Snippets
  - Tips
  - Tutorials
tags:
  - Hello world
  - Hello World
  - Java
  - Programming
  - software libre
  - Technology
  - Tutorials

---
![](/images/data_base.jpg)

Hace algún tiempo ya un amigo me pregunto que si era posible conectarse a una base de datos mysql utilizando Java, y le respondí claro que si, una opción es utilizar JDBC y el driver de mysql, hice un ejemplo bastante sencillo con el que seguro queda claro cual es la idea principal.

Lo primero que tienen que hacer es descargar el driver de conexión a mysql: **mysql-connector-java-5.1.5-bin.jar** y lo instalan, si utilizan eclipse es muy sencillo, tienen que copiarlo a la carpeta de su proyecto y después hacer clic con el botón secundario en su proyecto y seleccionar Build Path > Libraries > Add Jars y agregan su archivo :).

Después de eso pueden probar este pequeño código de ejemplo.

```Python
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class jdbcExample {

	Connection newDB;

	void getStates()
	{
        try {

            Statement STMT1 = newDB.createStatement();
            String SQLQuery = "SELECT name FROM states";
            ResultSet RX = STMT1.executeQuery(SQLQuery);

            while (RX.next()) {
                System.out.println(RX.getString("name"));
            }
        }
        catch(SQLException e) {

        }
	}

	void insertState(String name) {
		name = name.trim();
        if (name.length() > 0) {
            try {
                Statement STMT = newDB.createStatement();

                String SQLQuery = "INSERT INTO states (name) VALUES ('" + name + "');";
                STMT.executeUpdate(SQLQuery);
                System.out.println("Se agrego un nuevo estado: " + name);
            }
            catch (SQLException e) {
                System.out.println("ERROR AL INSERTAR NUEVO ESTADO " + e.toString());
            }
        }
    }

	void removeState(String name)
	{
        try {

            Statement STMT1 = newDB.createStatement();
            String SQLQuery = "DELETE FROM states WHERE name = '" + name + "'";
            STMT1.executeUpdate(SQLQuery);

            System.out.println("Se elimino el estado: " + name);
        }
        catch(SQLException e) {
        	System.out.println("ERROR AL BORRAR ESTADO " + e.toString());
        }
	}

	void performConnection() {

        String new_hostName = "127.0.0.1";
        String new_userName = "root";
        String new_password = "";
        String new_dataBase = "zonauPruebas";

        try {

        	Class.forName("com.mysql.jdbc.Driver");

            String newConnectionURL = "jdbc:mysql://" + new_hostName + "/" + new_dataBase + "?" + "user=" + new_userName + "&password=" + new_password;
            newDB = DriverManager.getConnection(newConnectionURL);

    	} catch (SQLException e) {
    		System.out.println("SQL Exception: " + e.toString());
    	} catch (ClassNotFoundException cE) {
    		System.out.println("Class Not Found Exception: " + cE.toString());
    	}

    	//obteniendo datos
    	getStates();
    	insertState("Java Town");
    	removeState("Java Town");
	}

    public static void main(String[] args) {
    	jdbcExample nuevaConexion = new jdbcExample();
        nuevaConexion.performConnection();
    }
}
```

Ok para los que ya están familiarizados con **java** les resultara muy sencillo de entender, para los que aquí va la explicación, (omitiré la parte de los imports de librerías por obvias razones xD).

```Text only
public class jdbcExample {

	Connection newDB;
```

Al inicio de creo una nueva variable de clase de tipo **Connection**, desde aquí comenzamos a hacer uso de la maravilloso de los **objetos** :p.

```CSS+Lasso
void performConnection() {

        String new_hostName = "127.0.0.1";
        String new_userName = "root";
        String new_password = "";
        String new_dataBase = "zonauPruebas";

        try {

        	Class.forName("com.mysql.jdbc.Driver");

            String newConnectionURL = "jdbc:mysql://" + new_hostName + "/" + new_dataBase + "?" + "user=" + new_userName + "&password=" + new_password;
            newDB = DriverManager.getConnection(newConnectionURL);

    	} catch (SQLException e) {
    		System.out.println("SQL Exception: " + e.toString());
    	} catch (ClassNotFoundException cE) {
    		System.out.println("Class Not Found Exception: " + cE.toString());
    	}

    	//obteniendo datos
    	getStates();
    	insertState("Java Town");
    	removeState("Java Town");
	}
```
```Text only
Después, esta es la parte mas importante del código, aquí es donde establecemos la conexión a la base de datos, es especial esta
```
```CSS+Lasso
String newConnectionURL = "jdbc:mysql://" + new_hostName + "/" + new_dataBase + "?" + "user=" + new_userName + "&password=" + new_password;
```
```Text only
Donde utilizamos el protocolo JDBC para conectarnos.

Después mas abajo verán la parte donde se mandan llamar métodos de la clase
```
```Text only
getStates();
    	insertState("Java Town");
    	removeState("Java Town");
```

Ahora explico lo que hace cada uno de ellos, el primero hace un **SELECT**, el segundo un **INSERT** y el tercero un **DELETE**.

```Tera Term macro
void getStates()
{
        try {

            Statement STMT1 = newDB.createStatement();
            String SQLQuery = "SELECT name FROM states";
            ResultSet RX = STMT1.executeQuery(SQLQuery);

            while (RX.next()) {
                System.out.println(RX.getString("name"));
            }
        }
        catch(SQLException e) {

        }
}
```

Como el código lo indica, creamos un nuevo dato de tipo Statement, armamos nuestra **Query** y al final realizamos la consulta (el **SELECT**) utilizando **executeQuery** y guardamos el resultado en un **ResultSet** que al final recorreremos utilizando un **While**, imprimimos el contenido con **getString**, esto implícitamente funciona moviendo un apuntador a través del **ResulSet** pero eso es otra historia xD.

```verilog
void insertState(String name) {
		name = name.trim();
        if (name.length() > 0) {
            try {
                Statement STMT = newDB.createStatement();

                String SQLQuery = "INSERT INTO states (name) VALUES ('" + name + "');";
                STMT.executeUpdate(SQLQuery);
                System.out.println("Se agrego un nuevo estado: " + name);
            }
            catch (SQLException e) {
                System.out.println("ERROR AL INSERTAR NUEVO ESTADO " + e.toString());
            }
        }
}
```

En este método al igual que en el anterior utilizamos un **Statement**, pero recibimos como parámetro un string, le aplicamos el método **trim()** que remueve espacios al inicio y al final de la cadena, después armamos nuestra consulta agregando el string de la variable **name** y la ejecutamos con **executeUpdate**

Entonces hasta ahorita ya deberían de saber como recuperar datos y como agregarlos de una **base de datos** :p, vamos por la tercera que seria eliminarlos.

```CSS+Lasso
void removeState(String name)
	{
        try {

            Statement STMT1 = newDB.createStatement();
            String SQLQuery = "DELETE FROM states WHERE name = '" + name + "'";
            STMT1.executeUpdate(SQLQuery);

            System.out.println("Se elimino el estado: " + name);
        }
        catch(SQLException e) {
        	System.out.println("ERROR AL BORRAR ESTADO " + e.toString());
        }
}
```

Es igual al método anterior solo que ahora la consulta en lugar de contener un **INSERT** será un **DELETE** :).

```Text only
public static void main(String[] args) {
    	jdbcExample nuevaConexion = new jdbcExample();
        nuevaConexion.performConnection();
    }
```

Al final creamos nuestro tan importante método main (se rumora que una vez un programador hizo un programa con 3 mains O.o???), y creamos una nueva instancia de nuestra clase y después ejecutamos el método **performConnection()** que realiza la conexión.

Bueno hasta aqui este mega tutorial relámpago de **conexiones a bases de datos mysql con JDBC en Java**, me voy a dormir, espero les sirva y cualquier duda comenten por favor.

Aquí les dejo el código **sql** de la tabla que utilice en el ejemplo para si ustedes quieren utilizarla.

<div class="demobox" style="margin-top: 10px; height: auto;">
[ ![](http://www.alevsk.com/wp-content/themes/ModernStyle//images/download.png) ](http://pastebin.com/ptM6LXi8)
</div>

Les recuerdo que aun esta en pie el concurso [Ganate una cuenta premium de megaupload GRATIS][1]

salu2

 [1]: http://www.alevsk.com/2011/09/cuenta-de-megaupload-gratis-2011/
---
title: Como crear usuarios y asignar permisos en PostgreSQL
author: Alevsk
type: post
date: 2012-10-15T00:00:49+00:00
url: /2012/10/como-crear-usuarios-y-asignar-permisos-en-postgresql/
categories:
  - Linux
  - Mac
  - Technology
  - Tutorials
tags:
  - Linux
  - mac
  - software libre
  - Solutions
  - Technology
  - Tutorials

---
[![](/images/logo_postgres-791620.png)](http://www.alevsk.com/2012/10/como-crear-usuarios-y-asignar-permisos-en-postgresql/logo_postgres-791620/)

En este tutorial veremos **como crear un nuevo usuario y darle permisos sobre una base de datos usando postgreSQL**, concretamente necesitaremos los siguientes comandos:

  * **adduser**: comando utilizado agregar usuarios en un sistema **UNIX/Linux**
  * **psql**: Llamada al interprete de comandos de postgreSQL (Si quieres ver una guia de la instalacion puedes revisar [Instalar PostgreSQL 9.2 en Mac OSX][1]).
  * **CREATE USER**: Sirve para dar de alta un nuevo usuario en el gestor de base de datos.
  * **CREATE DATABASE**: Crea una nueva base de datos.
  * **GRANT ALL PRIVILEGES**: Define los privilegios que un usuario tendra sobre una base de datos.

Los siguientes pasos fueron probados utilizando **debian squeeze 6**, sin embargo el procedimiento no debería de variar mucho en otras distribuciones de Linux (tal vez y algunos comandos del sistema son diferentes pero no mas).

# Desde la terminal 

Lo primero que tenemos que hacer es crear un nuevo usuario en el sistema (necesitamos privilegios de **root**)

```bash
# adduser alevsk  
# passwd alevsk
```

Despues tenemos que acceder como el super usuario de postgresql (por lo general es postgres)

```bash
# su – postgres
```

Luego mandamos llamar el interprete del gestor indicando un usuario y una base de datos, por defecto también es postgres y postgres (usuario y base de datos).

```bash
# psql -h localhost -d postgres -U postgres
```  
Si todo va bien la consola debería de mostrar algo como esto:  
```bash
You are using psql, the command-line interface to PostgreSQL.  
Type: \copyright for distribution terms  
\h for help with SQL commands  
\? for help with psql commands  
\g or terminate with semicolon to execute query  
\q to quit  
postgres=#
```

Una vez dentro simplemente indicamos que queremos agregamos un nuevo usuario.

```bash
postgres=# CREATE USER alevsk WITH PASSWORD 'elpassword';
```

Luego creamos la base de datos.

```bash
postgres=# CREATE DATABASE blog;
```

Y finalmente damos los privilegios al usuario sobre la **base de datos** que acabamos de crear.

```bash
postgres=# GRANT ALL PRIVILEGES ON DATABASE blog to alevsk;  
postgres=# \q
```

Y listo, ahora para corroborar que lo hicimos bien podemos intentar acceder al gestor con la cuenta que acabamos de crear.

```bash
$ su – alevsk  
$ psql –h localhost -d blog -U alevsk
```

Si todo salió bien la salida seria:

```bash
Welcome to psql 7.4.16, the PostgreSQL interactive terminal.  
Type: \\copyright for distribution terms  
\\h for help with SQL commands  
\\? for help on internal slash commands  
\\g or terminate with semicolon to execute query  
\\q  
blog=>
```

salu2

 [1]: http://www.alevsk.com/2012/10/instalar-postgresql-9-2-en-mac-osx/
---
title: Instalar PostgreSQL 9.2 en Mac OSX
author: Alevsk
type: post
date: 2012-10-14T23:25:06+00:00
url: /2012/10/instalar-postgresql-9-2-en-mac-osx/
categories:
  - Mac
  - Technology
  - Tutorials
tags:
  - mac
  - Programming
  - software libre
  - Solutions
  - Technology
  - Tutorials

---
PostgreSQL es una de las tantas opciones que tenemos a la hora de trabajar con bases de datos, en lo personal lo he estado utilizando desde hace algunos meses ya y me encuentro muy cómodo con este gestor :), instalarlo es realmente sencillo, a continuación los pasos que yo realice para **Instalar PostgreSQL 9.2 en Mac OSX** (esta guia es para instalar la version 9.2.1 en Lion, pero seguramente funciona para cualquier otra versión).

## Crear el usuario PostgreSQL

Lo primero que tenemos que hacer es crear un nuevo usuario, por convención lo llamamos postgres. (desde la terminal)

```bash
sudo dscl . -create /Users/postgres UserShell /usr/bin/false
```

## Descargar postgreSQL 9.2.1 y comenzar la instalación

Despues descargamos el instalador DMG desde el [sitio oficial][1].

Corremos el instalador, si nos da un error referente a memoria compartida simplemente seleccionamos Ok para que el instalador haga los cambios necesarios, reiniciamos nuestro equipo y lo intentamos de nuevo.

Al final el instalador me mostro los siguientes errores:

```bash
Problem running post-install step.  
Installation may not complete correctly  
The database cluster initialization failed.
```

Leyendo en algunos foros y blogs se supone que la razón es creación la del usuario postgres previa a la instalación, sin embargo no hay nada por que preocuparse, continuamos …

## Probando PSQL en la terminal

Abrimos nuestra terminal y escribimos el comando **psql**, si nos da un error referente a que el comando no existe lo que tenemos que hacer es lo siguiente:

Escribimos:

```bash
which psql
```

Y probablemente la terminal nos mostrara algo como

```bash
/usr/bin/psql
```

Esta apuntando al path de instalación e por defecto del gestor y no ha donde acabamos de instalarlo. Para resolver ese problema tenemos que editar nuestro archivo bash_profile, que lo podemos encontrar en **~/.bash_profile**, agregamos la siguiente linea:

```bash
export PATH=/Library/PostgreSQL/9.2/bin:$PATH
```

Si al abrir el archivo notas que ya tienes una entrada con export, no unico que tienes que hacer es agregar **/Library/PostgreSQL/9.2/bin** en alguna parte antes de **$PATH**, teniendo en cuidado de separar el path de otros usando **:**, al final debes de tener algo como:

```bash
export PATH=/opt/local/bin:/opt/local/sbin:/Library/PostgreSQL/9.2/bin:$PATH
```

Nota: 9.2 debe ser remplazado por la versión de **postgreSQL** que acabas de instalar.

Escribimos una vez mas en la consola  
```bash
source ~/.bash_profile
```  
despues  
```bash
which psql
```  
Y si todo esta bien debemos debemos de obtener algo como  
```bash
/Library/PostgreSQL/9.2/bin/psql
```

Damos los permisos correspondientes a la carpeta de instalación (le asignamos la propiedad al usuario postgres)

```bash
sudo chown postgres /Library/PostgreSQL/9.2/data/
```

Y después lanzamos el servicio

```bash
sudo -u postgres initdb -D /Library/PostgreSQL/9.2/data
```  
```bash
sudo -u postgres postgres -D /Library/PostgreSQL/9.2/data
```

Para comenzar a hacer uso de nuestro gestor podemos acceder desde la terminal  
```bash
psql -h localhost -d basededatos -U usuario
``` que es una excelente GUI para hacer uso de **postgreSQL**.

O si lo prefieres puedes **[descargar pgAdmin III][2]**

[![](/images/postgresql.png)](http://www.alevsk.com/2012/10/instalar-postgresql-9-2-en-mac-osx/postgresql/)

salu2

 [1]: http://www.enterprisedb.com/products-services-training/pgdownload#osx "download postgresql"
 [2]: http://www.pgadmin.org/download/macosx.php
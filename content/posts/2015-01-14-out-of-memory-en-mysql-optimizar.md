---
title: OOM en MySQL (cuando las bases de datos mueren)
author: Alevsk
type: post
date: 2015-01-14T03:09:18+00:00
url: /2015/01/out-of-memory-en-mysql-optimizar/
categories:
  - Geek
  - Linux
  - Technology
  - Tips
  - Tutorials
tags:
  - debian
  - Linux
  - mysql
  - shell
  - software libre
  - Technology
  - ubuntu

---
[![devotion_to_duty](/images/devotion_to_duty.png)](http://www.alevsk.com/2015/01/out-of-memory-en-mysql-optimizar/devotion_to_duty/)

Durante 2014 estuve trabajando bastante con **servidores virtuales** de la compañía [digitalocean.com](https://www.digitalocean.com/), esta compañía tiene planes bastante económicos y accesibles (desde 5 dólares por mes) si lo que queremos es montar micro sitios web, ideales para paginas web de pequeñas compañías que reciben algunas miles de visitas por mes.

Sin embargo esta es un arma de doble filo, ya que si lo que quieren las empresas es ahorrarse unos cuantos dólares al año tienen que invertirlos en un buen administrador de sistemas que optimice sus servidores para aprovechar al máximo los recursos tan limitados del servidor

  * 512 MB Memory
  * 1 CoreProcessor
  * 20 GB SSD Disk
  * 1 TB Transfer

Uno de los problemas mas comunes que he visto es el llamado **OOM** (**Out Of Memory**) de **Mysql**, lo que ocasiona que los sitios web queden fuera de servicio … incluso durante días hasta que alguien se da cuenta.

Por lo regular nos damos cuenta que es un problema de memoria cuando se cayo el servicio e intentamos restablecerlo, y en la consola nos es desplegado un mensaje como el siguiente:

```bash
root@server:/# service mysql start  
[FAIL] Starting MySQL database server: mysqld . . . . . . . . . . . . . . failed!
```

Podemos revisar los logs del servicio en los siguientes archivos:

  * /var/log/mysql.err – MySQL Error log file
  * /var/log/mysql.log – MySQL log file

También podemos revisar el estado de la memoria con el comando free:

```bash
root@server:/# free -m  
total used free shared buffers cached  
Mem: 497 467 29 0 8 146  
-/+ buffers/cache: 312 184  
Swap: 999 3 996
```

En este punto obviamente el servidor se esta cayendo a pedazos así que lo que tenemos que hacer es primeramente detectar las malas configuraciones de Mysql (configuraciones por default) y optimizarlas :D.

Existe una utilidad que nos hace la vida mas sencilla, un pequeño software llamado **mysqltuner**, así que lo instalamos.

```bash
root@server:/# apt-get install mysqltuner
```

Y lo ejecutamos con el comando mysqltuner, al inicio nos pedirá las credenciales de un usuario con privilegios de root, para después comenzar a realizar un análisis y sugerirnos varias configuraciones de acuerdo a los resultados

```bash
root@server:/# mysqltuner  
perl: warning: Setting locale failed.  
perl: warning: Please check that your locale settings:  
LANGUAGE = "en_US:en",  
LC_ALL = (unset),  
LC_CTYPE = "UTF-8",  
LANG = "en_US.UTF-8"  
are supported and installed on your system.  
perl: warning: Falling back to the standard locale ("C").

>> MySQLTuner 1.1.1 – Major Hayden  
>> Bug reports, feature requests, and downloads at http://mysqltuner.com/  
>> Run with '–help' for additional options and output filtering  
Please enter your MySQL administrative login: root  
Please enter your MySQL administrative password: 

——– General Statistics ————————————————–  
[–] Skipped version check for MySQLTuner script  
[OK] Currently running supported MySQL version 5.5.40-0+wheezy1-log  
[OK] Operating on 64-bit architecture

——– Storage Engine Statistics ——————————————-  
[–] Status: +Archive -BDB -Federated +InnoDB -ISAM -NDBCluster  
[–] Data in MyISAM tables: 5M (Tables: 33)  
[–] Data in InnoDB tables: 2M (Tables: 44)  
[–] Data in PERFORMANCE_SCHEMA tables: 0B (Tables: 17)  
[!!] Total fragmented tables: 52

——– Security Recommendations ——————————————-  
[OK] All database users have passwords assigned

——– Performance Metrics ————————————————-  
[–] Up for: 37m 4s (12K q [5.810 qps], 265 conn, TX: 24M, RX: 1M)  
[–] Reads / Writes: 92% / 8%  
[–] Total buffers: 192.0M global + 2.7M per thread (151 max threads)  
[!!] Maximum possible memory usage: 597.8M (120% of installed RAM)  
[OK] Slow queries: 0% (0/12K)  
[OK] Highest usage of available connections: 1% (3/151)  
[OK] Key buffer size / total MyISAM indexes: 16.0M/1.9M  
[OK] Key buffer hit rate: 99.3% (148K cached / 998 reads)  
[OK] Query cache efficiency: 63.4% (7K cached / 11K selects)  
[OK] Query cache prunes per day: 0  
[OK] Sorts requiring temporary tables: 0% (0 temp sorts / 446 sorts)  
[OK] Temporary tables created on disk: 19% (152 on disk / 792 total)  
[OK] Thread cache hit rate: 98% (3 created / 265 connections)  
[OK] Table cache hit rate: 24% (123 open / 495 opened)  
[OK] Open file limit used: 11% (120/1K)  
[OK] Table locks acquired immediately: 100% (4K immediate / 4K locks)  
[OK] InnoDB data size / buffer pool: 3.0M/128.0M

——– Recommendations —————————————————–  
General recommendations:  
Run OPTIMIZE TABLE to defragment tables for better performance  
MySQL started within last 24 hours – recommendations may be inaccurate  
Reduce your overall MySQL memory footprint for system stability  
Enable the slow query log to troubleshoot bad queries

root@server:/#
```

En este ejemplo **mysqltuner** nos arrojo problemas con algunas tablas fragmentadas y una configuración por default de memoria ram que permite que el gestor utilice el 120% de la memoria del sistema! (y así quieren que no se muera el servicio x.x), entonces, con esta información ya tenemos algunas pistas acerca de por donde comenzar a resolver y optimizar.

salu2
---
title: 'StringTransformer: the transformation tool'
author: Alevsk
type: post
date: 2016-09-02T05:08:43+00:00
url: /2016/09/stringtransformer-the-transformation-tool/
categories:
  - Geek
  - Ethical Hacking
  - Linux
  - Mac
  - Personal
  - Programming
  - Snippets
  - Technology
  - Tips
tags:
  - algoritmos
  - hacking
  - opensource
  - python
  - script

---
[![st](/images/st.png)](http://www.alevsk.com/2016/09/stringtransformer-the-transformation-tool/st/)

Hola lectores, en esta ocasión me gustaría compartir con ustedes una herramienta [opensource][1] que he publicado en mi repositorio de [github][2], se trata de [StringTransformer][3], un script desarrollado en [python][4] cuya finalidad es tomar una cadena de texto y transformarla a distintas representaciones equivalentes de la misma, por ejemplo binario, hexadecimal, octal, md5, sha256, etc. Las funciones de transformación son clases separadas del script principal por lo que la herramienta es modular, esto significa que es bastante fácil para cualquier programador (que sepa python) crear sus propias transformaciones y extender la funcionalidad de la herramienta.

Esta herramienta les puede ser útil cuando están jugando [Capture the flags][5] y necesitan una forma rápida de analizar cadenas de texto (o al menos esa es su finalidad), la herramienta sigue en desarrollo, corrigiendo bugs e implementando nuevas funcionalidades.

# Instalación 

Su instalación es bastante sencilla, primero deben de clonar el repositorio usando [git][6]

```bash
$ git clone https://github.com/Alevsk/stringTransformer.git
```

Una vez descargado el repositorio acceden a la carpeta del proyecto, dan los permisos de ejecución necesarios y lanzan el script:

```bash
$ cd stringTransformer  
$ chmod +x stringTransformer.py  
$ ./stringTransformer.py

\___\____  
\_____ | _ | \____  
| | \ V / | |  
| \ \ \_ _/ / / |  
\ \ \ \ ' / / / /  
\ \ | 'V' | / /  
|\ \__\_\\_\_| \ / |\_\_\___/ /|  
| \ | | / |  
| | ,/|| ||\, | |  
| \`| ' || || ' |\` |  
| | | || || | | |  
\ | | || || | | /  
\. | | ||_|| | | ./  
\ | | |\___| | | /  
\' , \_____ , '/  
\/ \___ \/  
/\___\ 

stringTransformer v0.1 (https://github.com/alevsk/stringTransformer/)

Usage: stringTransformer.py -i INPUT\_STRING | –input INPUT\_STRING | –load FILE

stringTransformer.py: error: Required argument is missing. Use '-h' for help.
```

Con el comando **-h** o **–help** podran ver el menu de ayuda:

```bash
Options:  
-h/–help show this help message and exit  
-i/–input=INPUT set the input string to test with  
-l/–load=LOAD_FILE load list of input strings (one per line)  
-x/–exclude=EXCLUDE exclude this representations  
-o/–only=ONLY transform input only to this representations  
-O/–output=OUTPUT generate an output file  
-p/–params=PARAMS use custom parameters on transformation functions  
–list list available input representations  
–update update from the official git repository

Examples:  
./stringTransformer.py -i [STRING]  
./stringTransformer.py -i [STRING] –exclude "hexa, octal"  
./stringTransformer.py -i [STRING] –only "hexa, octal"  
./stringTransformer.py -i [STRING] –params "rot.cipher=13,rot.encoding=utf-8"  
./stringTransformer.py –load list.txt  
./stringTransformer.py –list
```

Para ver las funciones de transformación actualmente disponibles pueden utilizar **–list**:

```bash
stringTransformer v0.1 (https://github.com/alevsk/stringTransformer/)

– sha1  
– octal  
– binary  
– sha256  
– html\_entities\_decode  
– html\_entities\_encode  
– md5  
– base64_encode  
– base64_decode  
– ascii  
– slug  
– rot_encode  
– hexa  
– urlencode
```

Puedes ayudar a crear más funciones de transformación para la herramienta, para eso sugiero lean la documentación en la página principal del repositorio (o en el archivo README.md) [https://github.com/Alevsk/stringTransformer](https://github.com/Alevsk/stringTransformer)

## Ejemplos de uso

Queremos aplicar una transformación hexadecimal, rot 13 encode y ascii a la cadena de texto **“The transformation tool"**  
```bash
$ ./stringTransformer.py -i "The transformation tool" -o "hexa,rot_encode,ascii"
```

Obtenemos como resultado:

```bash
stringTransformer v0.1 (https://github.com/alevsk/stringTransformer/)

[i] Loaded 3 representations to apply.  
[i] Starting tests at: "23:54:04"

The transformation tool

[i] applying transformation…

ascii:

84 104 101 32 116 114 97 110 115 102 111 114 109 97 116 105 111 110 32 116 111 111 108

rot_encode:

Gur genafsbezngvba gbby

hexa:

54 0x68 0x65 0x20 0x74 0x72 0x61 0x6e 0x73 0x66 0x6f 0x72 0x6d 0x61 0x74 0x69 0x6f 0x6e 0x20 0x74 0x6f 0x6f 0x6c 

==================================
```

Incluso podemos pasar parámetros a las funciones de transformación que lo soporten, rot_encode por defecto utilizar 13 posiciones de desplazamiento pero aquí indicamos que use 51

```bash
$ ./stringTransformer.py -i "The transformation tool" -o "rot\_encode" –params="rot\_encode.cipher=51"

stringTransformer v0.1 (https://github.com/alevsk/stringTransformer/)

[i] Loaded 1 representations to apply.  
[i] Starting tests at: "23:58:11"

The transformation tool

[i] applying transformation…

rot_encode:

Sgd sqzmrenqlzshnm snnk

==================================
```

La herramienta cuenta con muchísimos otros parámetros que los invito a explorar.  
saludos

 [1]: https://www.alevsk.com/?s=opensource
 [2]: http://github.com/Alevsk
 [3]: https://github.com/Alevsk/stringTransformer
 [4]: https://www.alevsk.com/?s=python
 [5]: https://www.alevsk.com/?s=ctf
 [6]: https://www.alevsk.com/?s=git
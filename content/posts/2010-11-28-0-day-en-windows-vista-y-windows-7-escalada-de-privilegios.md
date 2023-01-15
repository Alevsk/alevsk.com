---
title: 0-Day en Windows Vista y Windows 7 (Escalada de Privilegios)
author: Alevsk
type: post
date: 2010-11-28T01:55:36+00:00
url: /2010/11/0-day-en-windows-vista-y-windows-7-escalada-de-privilegios/
categories:
  - Geek
  - Ethical Hacking
  - IT News
  - Technology
tags:
  - backtrack
  - hackers
  - Linux
  - Programming
  - slackware

---
[![](/images/keyboard_hack.jpg)](http://www.alevsk.com/2010/11/0-day-en-windows-vista-y-windows-7-escalada-de-privilegios/keyboard_hack/)

Se ha publicado una vulnerabilidad y una PoC sobre una vulnerabilidad en las versiones de Windows Vista y Windows 7 que permiten una elevacion de privilegios con el cual un atacante podria ejecutar codigo malisioso. El problema reside en Win32k.sys, por lo tanto incluso un usuario con privilegios limitados podria ejecutar codigo en modo kernel.

El problema esta en que la API NtGdiEnableEUDC no valida correctamente algunas entradas causando un Stack Overflow y sobre escribiendo la direccion de retorno guardado en la pila. Un atacante podria modificar el valor de la direccion de retorno para apuntar a la direccion del su propio codigo malicioso y asi ejecutarlo en modo kernel. Al ser una vulnerabilidad de escalacion de privilegios esta incluso traspasa la proteccion de la UAC implementada en los sistemas Windows Vista y Window 7.

PoC:

  * http://www.exploit-db.com/sploits/uacpoc.zip

Mas Informacion:

  * http://www.prevx.com/blog/160/New-Windows-day-exploit-speaks-chinese.html
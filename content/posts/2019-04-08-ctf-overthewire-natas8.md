---
title: 'CTF OverTheWire: Natas8'
author: Alevsk
type: post
date: 2019-04-08T04:04:28+00:00
url: /2019/04/ctf-overthewire-natas8/
categories:
  - Ethical Hacking
  - HTML
  - IT News
  - Personal
  - Problem Solving
  - Programming
  - Technology
  - Tutorials
tags:
  - capture the flag
  - ctf
  - Linux
  - Personal
  - Programming
  - Tutorials

---
[![](/images/Screen-Shot-2018-05-29-at-1.57.38-AM-1200x596.png)](https://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-1-57-38-am/)

After a break we continue with the [CTF Natas](http://overthewire.org/wargames/natas/) series, now is the turn for [natas8](http://overthewire.org/wargames/natas/natas8.html)

```bash
  
Natas Level 7 → Level 8  
Username: natas8  
URL: http://natas8.natas.labs.overthewire.org  

```

Using the flag obtained in the previous challenge, we go to the URL showed in the description and we will see the following screen.

[![](/images/nata8_1.png)](https://www.alevsk.com/2019/04/ctf-overthewire-natas8/nata8_1/)

It's just a simple web page with a basic input form, if we type nonsense we get an error message displaying **Wrong secret**, we proceed to click the the **View sourcecode**

```php
  
<html>
<head>
<!--– This stuff in the header has nothing to do with the level –-->
<link href="http://natas.labs.overthewire.org/css/level.css" rel="stylesheet" type="text/css"/>
<link href="http://natas.labs.overthewire.org/css/jquery-ui.css" rel="stylesheet"/>
<link href="http://natas.labs.overthewire.org/css/wechall.css" rel="stylesheet"/>
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas8", "pass": "<censored>" };</script></head>
<body>
<h1>natas8</h1>
<div id="content">
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {  
return bin2hex(strrev(base64_encode($secret)));  
}

if(array\_key\_exists("submit", $_POST)) {  
if(encodeSecret($_POST['secret']) == $encodedSecret) {  
print "Access granted. The password for natas9 is <censored>";  
} else {  
print "Wrong secret";  
}  
}  
?>

<form method="post">  
Input secret: <input name="secret"/><br/>
<input name="submit" type="submit"/>
</form>
<div id="viewsource">[View sourcecode](index-source.html)</div>
</div>
</body>
</html>  

```

This is supposed to be the backend code of the HTML page we just saw, the important part of this challenge is in the PHP code functions, taking a quick look the data flow looks like this:

  * Check if submit key exists on **$_POST**
  * Pass **$_POST['secret']** to **encodeSecret** function
  * **encodeSecret** function will apply some transformation to the secret and return it
  * The transformed secret must be equal to **3d3d516343746d4d6d6c315669563362**, otherwise we are getting the **Wrong secret** error we saw already

As I say before, the important part is happening inside the **encodeSecret** function, the code is basically doing this:

> secret -> base64_encode -> strrev -> bin2hex -> 3d3d516343746d4d6d6c315669563362

So we need to perform exactly the same operations but in reverse order to obtain the original secret, ie: the old bin2hex should be hex2bin, I don't know if we should call this reverse engineering, anyway ¯\_(ツ)_/¯

> 3d3d516343746d4d6d6c315669563362 -> hex2bin -> strrev -> base64_encode -> secret

We can use **PHP** from the command line and do this:

```bash
  
$ php -r "echo base64_decode(strrev(hex2bin('3d3d516343746d4d6d6c315669563362')));"  
oubWYf2kBq  
$  

```

We get the secret: **oubWYf2kBq**, we try it on the input form.

[![](/images/nata8_2.png)](https://www.alevsk.com/2019/04/ctf-overthewire-natas8/nata8_2/)
[![](/images/nata8_3.png)](https://www.alevsk.com/2019/04/ctf-overthewire-natas8/nata8_3/)

The flag for the next level, natas9, is: **W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl**

> In this challenge we take advantage of a security vulnerability called [Source code disclosure](https://www.acunetix.com/blog/articles/source-code-disclosure-dangerous/) and then we did basic reverse engineering on the **PHP code**. 

Happy hacking 🙂
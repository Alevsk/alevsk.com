---
title: 'CTF OverTheWire: Natas9'
author: Alevsk
type: post
date: 2020-01-13T06:07:35+00:00
url: /2020/01/ctf-overthewire-natas9/
categories:
  - Ethical Hacking
  - Linux
  - Problem Solving
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - capture the flag
  - hacking
  - Ethical Hacking
  - Linux
  - Personal
  - Programming
  - Solutions
  - Technology
  - Tutorials

---
[![](/images/Screen-Shot-2018-05-29-at-1.57.38-AM-1200x596.png)](https://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-1-57-38-am/)

Continuing with the [CTF Natas](http://overthewire.org/wargames/natas/) series, now is the turn for [natas9](http://overthewire.org/wargames/natas/natas9.html)

```bash
  
Natas Level 8 → Level 9  
Username: natas9  
URL: http://natas9.natas.labs.overthewire.org  

```

Using the flag obtained in the previous challenge, we go to the URL showed in the description and we will see the following screen.

[![](/images/Screen-Shot-2020-01-12-at-9.01.52-PM-1200x431.png)](https://www.alevsk.com/2020/01/ctf-overthewire-natas9/screen-shot-2020-01-12-at-9-01-52-pm/)

It's just a simple web page with a basic input form, if we type nonsense nothing happens, we proceed to click the **View sourcecode** and we are redirected to **index-source.html**

This is supposed to be the backend code of the html form.

```php
<?  
  $key = "";

  if(array\_key\_exists("needle", $_REQUEST)) {  
    $key = $_REQUEST["needle"];  
  }

  if($key != "") {  
    passthru("grep -i $key dictionary.txt");  
  }  
?>  
```

The vulnerability in this code happens when calling the **[passthru](https://www.php.net/manual/en/function.passthru.php)** function, we are reading user input directly from the **needle** request parameter, then saving it into the **$key** variable and using it without any kind of sanitization when calling the function, that's essentially [command injection](https://www.owasp.org/index.php/Command_Injection). We are going to try to execute commands in the web server by exploiting this vulnerability.

Sending **;ls -la;**

[![](/images/Screen-Shot-2020-01-12-at-9.30.59-PM-1200x423.png)](https://www.alevsk.com/2020/01/ctf-overthewire-natas9/screen-shot-2020-01-12-at-9-30-59-pm/)

Results in all files on the current directory to be listed

[![](/images/Screen-Shot-2020-01-12-at-9.30.46-PM-1200x709.png)](https://www.alevsk.com/2020/01/ctf-overthewire-natas9/screen-shot-2020-01-12-at-9-30-46-pm/)

I was a little bit lost at this point but then I remember the CTF instructions.

> Each level has access to the password of the next level. Your job is to somehow obtain that next password and level up. All passwords are also stored in /etc/natas\_webpass/. E.g. the password for natas5 is stored in the file /etc/natas\_webpass/natas5 and only readable by natas4 and natas5.

So we do **;cat /etc/natas_webpass/natas10;**

[![](/images/Screen-Shot-2020-01-12-at-9.57.48-PM-1200x483.png)](https://www.alevsk.com/2020/01/ctf-overthewire-natas9/screen-shot-2020-01-12-at-9-57-48-pm/)

The flag for the next level, natas10, is: **nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu**

> As mentioned before, this challenge we exploit a command injection vulnerability that essentially allow us to execute arbitrary commands on the server, depending on the privileges of the user running the web server we might read, write or delete files.

Happy hacking 🙂
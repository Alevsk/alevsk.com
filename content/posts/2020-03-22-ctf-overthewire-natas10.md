---
title: 'CTF OverTheWire: Natas10'
author: Alevsk
type: post
date: 2020-03-22T03:46:21+00:00
url: /2020/03/ctf-overthewire-natas10/
categories:
  - Ethical Hacking
  - Linux
  - IT News
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - capture the flag
  - ctf
  - hackers
  - hacking
  - Linux
  - Programming
  - Solutions
  - Technology
  - web

---
[![](/images/Screen-Shot-2018-05-29-at-1.57.38-AM-1200x596.png)](https://www.alevsk.com/2018/05/ctf-overthewire-natas1/screen-shot-2018-05-29-at-1-57-38-am/)

Continuing with the [CTF Natas](http://overthewire.org/wargames/natas/) series, now is the turn for [natas10](http://overthewire.org/wargames/natas/natas10.html)

```bash
Natas Level 9 → Level 10  
Username: natas10  
URL: http://natas10.natas.labs.overthewire.org  
```

Using the flag obtained in the previous challenge, we go to the URL showed in the description and we will see the following screen.

[![](/images/Screen-Shot-2020-03-21-at-8.22.45-PM-1200x519.png)](https://www.alevsk.com/2020/03/ctf-overthewire-natas10/screen-shot-2020-03-21-at-8-22-45-pm/)

It's a simple web page with a basic input form, very similar to the previous one but they have added a character filter, we proceed to click the **View sourcecode** and we are redirected to **index-source.html**

This is supposed to be the backend code of the html form.

```php
<?  
  $key = "";

  if(array\_key\_exists("needle", $_REQUEST)) {  
    $key = $_REQUEST["needle"];  
  }

  if($key != "") {  
    if(preg_match('/[;|&]/',$key)) {  
      print "Input contains an illegal character!";  
    } else {  
      passthru("grep -i $key dictionary.txt");  
    }  
  }  
?>  
```

The **preg_match('/[;|&]/',$key)** function will make sure to drop any search request that contains the **;** or **&** characters so we cannot execute additional commands like we did on the previous level, but instead of trying to bypass this filter there is an easier way to solve this level, the [grep](https://linux.die.net/man/1/grep) command supports search for a pattern in multiple files so we are going to exploit that, the goal is to execute something like this:

```bash
grep -i " /etc/natas_webpass/natas11 dictionary.txt  
```

Since **" /etc/natas_webpass/natas11** doesn't contains any of the filtered characters we can just send this payload through the form.

[![](/images/Screen-Shot-2020-03-21-at-7.36.01-PM-1200x480.png)](https://www.alevsk.com/2020/03/ctf-overthewire-natas10/screen-shot-2020-03-21-at-7-36-01-pm/)

The flag for the next level, natas11, is: **U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK**

> In this challenge we exploit a command injection vulnerability that essentially allow us to execute arbitrary commands on the server, this time there was a security mechanism in place but the fundamental problem was still there. Depending on the privileges of the user running the web server we might read, write or delete files.

Happy hacking 🙂
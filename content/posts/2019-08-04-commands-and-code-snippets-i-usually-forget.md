---
title: Commands and Code Snippets I usually forget
author: Alevsk
type: post
date: 2019-08-04T02:10:10+00:00
url: /2019/08/commands-and-code-snippets-i-usually-forget/
categories:
  - Geek
  - Ethical Hacking
  - Javascript
  - Linux
  - Personal
  - Programming
  - Snippets
  - Technology
  - Tips
tags:
  - hackers
  - Javascript
  - Linux
  - software libre
  - Technology
  - ubuntu
  - web

---
Some commands and code snippets I use rarely during CTFs or my daily work, but still I need them from time to time and I'm very lazy to remember them. This note may grow over time.

# Javascript

##### Playing with dec, hexa and bin (not really) in JS

```javascript
String.fromCharCode(0x41) // 'A'

parseInt('0xf', 16) // 15

var n = 15

n.toString(16) // 'f'  
n.toString(2) // '1111'  
n.toString() // '15'

var n = 'A'  
n.charCodeAt() // 65  
// dec to hex  
n.charCodeAt().toString(16) // '41'  
// dec to bin  
n.charCodeAt().toString(2) // '1000001'  
// dec to hex  
parseInt(255).toString(16) // 'ff'  
// dec to bin  
parseInt(5).toString(2) // '101'  
```

##### Simple HTTP GET request using nodejs

```javascript
const https = require('https');

https.get('https://www.alevsk.com', (resp) => {  
let data = "";  
resp.on('data', (chunk) => {  
data += chunk;  
});  
resp.on('end', () => {  
//DO something with data  
});  
}).on("error", (err) => {  
console.log("Error: " + err.message);  
});  
```

##### Simple HTTP POST request using nodejs

```javascript
const https = require('https')

const data = JSON.stringify({  
todo: 'Buy the milk'  
})

const options = {  
hostname: 'whatever.com',  
port: 443,  
path: '/todos',  
method: 'POST',  
headers: {  
'Content-Type': 'application/json',  
'Content-Length': data.length  
}  
}

const req = https.request(options, res => {  
res.on('data', d => {  
process.stdout.write(d)  
})  
})

req.on('error', error => {  
console.error(error)  
})

req.write(data)

req.end()  
```

##### Extract content between regular expression patterns using JS

```javascript
const message = data.match(/<p>([^<]+)<\/p>/)[1];  
const lat = data.match(/name="lat" value="([^<]+)" min=/)[1];  
const long = data.match(/name="lon" value="([^<]+)" min=/)[1];  
const token = data.match(/name="token" value="([^<]+)"/)[1];  
```

# Linux

##### Mount NTFS on Linux

```bash
mount -t ntfs [FILE] [PATH]  
mount -t type device directory  
```

##### Extract extended attributes from NTFS disk

```bash
getfattr –only-values [FILE] -n [ATTR-NAME] > file  
```

##### Parsing file with awk and run xargs

```bash
cat [FILE] | awk '{print $1 .. $n}' | xargs  
```

# Python

##### Start Simple HTTP server with Python

```bash
python -m SimpleHTTPServer  
```

##### Inline Python commands

```bash
python -c 'print "\x41" * 20'  
```

# PHP

##### Run PHP interactive mode

```bash
php -a  
```
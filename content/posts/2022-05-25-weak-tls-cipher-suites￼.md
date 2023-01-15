---
title: Weak TLS cipher suites
author: Alevsk
type: post
date: 2022-05-25T05:38:58+00:00
url: /2022/05/weak-tls-cipher-suites￼/
yarpp_meta:
  - 'a:1:{s:27:"yarpp_display_for_this_post";i:1;}'
categories:
  - Ethical Hacking
  - Linux
  - Networking
  - IT News
  - Programming
  - Technology
  - Tutorials
tags:
  - docker
  - Linux
  - nginx
  - Programming
  - Technology
  - tls
  - web

---
![](/images/image.png)

[HTTP][1] and [HTTPS][2] are well known Internet protocols that don't require any introduction. The other day at work as part of a daily security scan one of our servers got tagged as using weak cipher suites during [TLS negotiation][3]. In this quick post I'll explain what a weak cipher suite means and how to fix it.

There are many tools out there to check if you are following the security best practices when it comes to SSL/TLS server configuration (supported versions, accepted cipher suites, certificate transparency, expiration, etc.) but one of my favorites is https://www.ssllabs.com/ssltest/analyze.html and [drwetter/testssl.sh][4].

SSLlabs.com is easy to use, you just have to enter a Hostname and the website will analyze all possible TLS configuration and calculate a score for you, this tool will also tell you what you can do to improve that score.

![](https://lh4.googleusercontent.com/g3nTPgnADL33Z3gIOwWEEQG68z1V6jgzs7HkzD52-fFRA2gyXHnQfl7bYpGQjXUNCd4MXB2e-2D8DEGaRwb7lfvhQOPEGhsTg9FaMgW4EPc321P_NM2xiEsOstMYqFwoIKbsU4E7rV4Trgn5) 

There are many [TLS protocol versions][5]: **1.0**, **1.1**, **1.2**, **1.3**. The first two are considered insecure and should not be used so I will focus on **1.2** and **1.3** only.  
In my case SSLlabs.com was complaining about weak cipher suites were supported for **TLS 1.2**:

![](https://lh6.googleusercontent.com/Ypq9wSJUO1TwDK4Wv2f_EC5WgwqvIT0BeIAUVaKMbwbM41rrIQ2JRMirjefbo7x_x5nRot7SXUKnoKv10Ohyyln-nQD79HjUr7KAFNvQ81O_YcDKZCn7Ll8f8ztgK3etioSiYdK0cWg6JIam) 

_The above report is showing ECDHE-RSA-AES256-SHA384E and ECDHE-RSA-AES256-SHA as weak cipher suites._

First let's clarify a couple of things, according to Wikipedia:

**Cipher suite:** A set of algorithms that help secure a network connection.

So a weak **cipher suite** will be algorithms with known vulnerabilities that can be used by attackers to downgrade connections or other nefarious things.

Fixing this is very easy and will require changing a line or two on the server configuration, deploying the changes and then testing again using SSLlabs.com.

Of course, the above only applies if you know exactly what you are doing, otherwise it will take you many attempts and you are going to waste precious time.

## Reproduce and fix the issue locally

Suppose you have the same issue I had, because this issue was reported on an Nginx Server now the task is to reproduce the issue locally and come up with a fix. With modern technologies like [docker containers][6] it's very easy to run a local Nginx server, the only thing you need is a copy of the **nginx.conf**, to run a docker container the command will be:

```Text only
docker run --name mynginx -v ./public.pem:/etc/nginx/public.pem -v ./private.pem:/etc/nginx/private.pem -v ./nginx.conf:/etc/nginx/nginx.conf:ro -p 1337:443 --rm nginx
```

The above command is telling docker to run an Nginx container; binding the local port **1337** to the container port **443** and also mounting the **public.pem** (public key), **private.pem** (private key) and **nginx.conf** (the server configuration) files inside the container.

The **nginx.conf** looks like this:

```GDScript
    server {
        listen 443 ssl;
        server_name www.alevsk.com;
        ssl_certificate /etc/nginx/public.pem;
        ssl_certificate_key /etc/nginx/private.pem;
        ssl_protocols TLSv1.3 TLSv1.2;
        ssl_prefer_server_ciphers on;
        ssl_ecdh_curve secp521r1:secp384r1:prime256v1;
        ssl_ciphers EECDH+AESGCM:EECDH+AES256:EECDH+CHACHA20;
        ssl_session_cache shared:TLS:2m;
        ssl_buffer_size 4k;
        add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains; preload' always;
    }
```

You can test the server is working fine with a simple **curl** command:

```GDScript
curl https://localhost:1337/ -v -k
*   Trying 127.0.0.1:1337...
* Connected to localhost (127.0.0.1) port 1337 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
* TLSv1.0 (OUT), TLS header, Certificate Status (22):
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS header, Certificate Status (22):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (OUT), TLS header, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS header, Certificate Status (22):
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS header, Finished (20):
* TLSv1.2 (IN), TLS header, Certificate Status (22):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use http/1.1
* Server certificate:
....
....
....
> 
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 Not Found
< Server: nginx
< Date: Sun, 15 May 2022 23:14:23 GMT
< Content-Type: text/html
< Content-Length: 146
< Connection: keep-alive
< Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
< 

404 Not Found

404 Not Found
nginx


* Connection #0 to host localhost left intact
```

The next step is to reproduce the report from https://www.ssllabs.com/ but that will involve somehow exposing our local Nginx server to the internet and that's time consuming. Fortunately there's an amazing open source tool that will help you to run all these TLS tests locally.

[drwetter/testssl.sh][4] is a tool for testing TLS/SSL encryption anywhere on any port and the best part is that runs on a container too, go to your terminal again and run the following command:

```Text only
docker run --rm -ti --net=host drwetter/testssl.sh localhost:1337
```

The above command will run the **drwetter/testssl.sh** container, the **–rm** flag will automatically delete the container once it's done running (keep your system nice and clean), **-ti** means interactive mode and **–net=host** will allow the container to use the parent host network namespace.

After a couple of seconds you will see a similar result as in the website, something like this:

Testing server's cipher preferences.

```Text only
Hexcode  Cipher Suite Name (OpenSSL)       KeyExch.   Encryption  Bits     Cipher Suite Name (IANA/RFC)                        
-----------------------------------------------------------------------------------------------------------------------------  
SSLv2                                                                                                                          
 -                                                                                                                             
SSLv3                                                                                                                          
 -                                                                                                                             
TLSv1                                                                                                                          
 -                                                                                                                             
TLSv1.1                                                                                                                        
 -                                                                                                                             
TLSv1.2 (server order)                                                                                                         
 xc030   ECDHE-RSA-AES256-GCM-SHA384       ECDH 521   AESGCM      256      TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384               
 xc02f   ECDHE-RSA-AES128-GCM-SHA256       ECDH 521   AESGCM      128      TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256               
 xc028   ECDHE-RSA-AES256-SHA384           ECDH 521   AES         256      TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384               
 xc014   ECDHE-RSA-AES256-SHA              ECDH 521   AES         256      TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA                  
 xcca8   ECDHE-RSA-CHACHA20-POLY1305       ECDH 521   ChaCha20    256      TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256         
TLSv1.3 (server order)                                        
 x1302   TLS_AES_256_GCM_SHA384            ECDH 256   AESGCM      256      TLS_AES_256_GCM_SHA384                              
 x1303   TLS_CHACHA20_POLY1305_SHA256      ECDH 256   ChaCha20    256      TLS_CHACHA20_POLY1305_SHA256                        
 x1301   TLS_AES_128_GCM_SHA256            ECDH 256   AESGCM      128      TLS_AES_128_GCM_SHA256
```

Even on this test we see the weak cipher suites (**ECDHE-RSA-AES256-SHA384** and **ECDHE-RSA-AES256-SHA**).

Great, now you are able to fully reproduce the issue locally and test as many times as you want until you have the perfect configuration. It's time to do the actual fix.

Open the **nginx.conf** file one more time and locate the line that starts with **ssl_ciphers** and just add **!ECDHE-RSA-AES256-SHA384:!ECDHE-RSA-AES256-SHA** at the end, ie:

```GDScript
 server {
        listen 443 ssl;
        server_name www.alevsk.com;
        ssl_certificate /etc/nginx/public.pem;
        ssl_certificate_key /etc/nginx/private.pem;
        ssl_protocols TLSv1.3 TLSv1.2;
        ssl_prefer_server_ciphers on;
        ssl_ecdh_curve secp521r1:secp384r1:prime256v1;
        ssl_ciphers EECDH+AESGCM:EECDH+AES256:EECDH+CHACHA20:!ECDHE-RSA-AES256-SHA384:!ECDHE-RSA-AES256-SHA;
        ssl_session_cache shared:TLS:2m;
        ssl_buffer_size 4k;
        add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains; preload' always;
    }
```

If you run the **Nginx container** with the new configuration and then run the [drwetter/testssl.sh][4] test again this time you will see no weak cipher suites anymore.

```Text only
TLSv1.2 (server order)                                                                                                         
 xc030   ECDHE-RSA-AES256-GCM-SHA384       ECDH 521   AESGCM      256      TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384              
 xc02f   ECDHE-RSA-AES128-GCM-SHA256       ECDH 521   AESGCM      128      TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256              
 xcca8   ECDHE-RSA-CHACHA20-POLY1305       ECDH 521   ChaCha20    256      TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256        
TLSv1.3 (server order)          
 x1302   TLS_AES_256_GCM_SHA384            ECDH 256   AESGCM      256      TLS_AES_256_GCM_SHA384                              
 x1303   TLS_CHACHA20_POLY1305_SHA256      ECDH 256   ChaCha20    256      TLS_CHACHA20_POLY1305_SHA256                        
 x1301   TLS_AES_128_GCM_SHA256            ECDH 256   AESGCM      128      TLS_AES_128_GCM_SHA256
```

## Conclusion

Congratulations, you just fixed your first **security engineer** issue and now you can push the fix to production. In general when it comes to fixing any kind of problem in tech it is better to start by reproducing the issue locally and work on a fix from there (of course this is debatable if you are facing an issue that only happens in a specific environment). SSL/TLS  and cipher suites are one of those technologies that you have to learn by heart or at least have a very good understanding if you want to work in application security, but not only that, once you understand it it will completely change the way you approach problems and debug security applications .

Happy hacking.

 [1]: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
 [2]: https://en.wikipedia.org/wiki/HTTPS
 [3]: https://www.ssl.com/article/ssl-tls-handshake-overview/
 [4]: https://github.com/drwetter/testssl.sh
 [5]: https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.0
 [6]: https://www.alevsk.com/2022/02/stop-passing-secrets-via-environment-variables-to-your-application/
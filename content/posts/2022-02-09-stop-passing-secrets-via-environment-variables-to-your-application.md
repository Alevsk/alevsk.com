---
title: Stop passing secrets via environment variables to your application
author: Alevsk
type: post
date: 2022-02-09T01:46:42+00:00
url: /2022/02/stop-passing-secrets-via-environment-variables-to-your-application/
yarpp_meta:
  - 'a:1:{s:27:"yarpp_display_for_this_post";i:1;}'
categories:
  - cloud
  - Ethical Hacking
  - Linux
  - IT News
  - Programming
  - Technology
  - Tutorials
tags:
  - containers
  - docker
  - hacking
  - Programming

---
![docker inspect command showing container secrets](/images/1639519328122-1200x493.png) 

Environment variables are great to configure and change the behavior of your applications, however there's a downside for that, if someone uses the \`docker inspect\` command your precious secrets will get revealed there, because of that you should never pass any sensitive data to your container using environment variables (the \`-e\` flag), I'll show you an example.

Suppose you have a simple python application (Download the source code of the app here: [https://github.com/Alevsk/docker-containers-env-vars-security](https://github.com/Alevsk/docker-containers-env-vars-security) ) that returns the hmac signature for a provided message using a configured secret, the code will look like this:

```Transact-SQL
app_secret = os.environ.get('APP_SECRET')
if app_secret is None:
    app_secret = ""

# derive key based on configured APP_SECRET
salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
secret = app_secret.encode("utf8")
key = pbkdf2_hmac("sha256", secret, salt, 4096, 32)

app = Flask(__name__)

@app.route("/")
def hello():
    message = request.args.get('message')
    if message is None:
        return "Give me a message and I'll sign it for you"
    else:
        h = hmac.new(key, message.encode(), hashlib.sha256)
        return "Original message: {}Signature: {}".format(message, h.hexdigest())

if __name__ == "__main__":
    app.run()
```

Pretty straightforward, then you build the [docker image][1] with:

```GDScript
docker build -t alevsk/app-env-vars:latest .
```

And run the application on a container with:

```GDScript
docker run --rm --name hmac-signature-service -p 5000:5000 -e APP_SECRET=mysecret alevsk/app-env-vars:latest
```

Test the endpoints works fine running a \`curl\` command:

```Text only
curl http://localhost:5000/?message=eaeae

Original message: eaeaeSignature: cce4625d3d586470bc84ac088b6e2ae24c012944832d54ab42a999de94252849%
```

Perfect, everything works as intended, however if you inspect the running container the content of \`APP_SECRET\` is leaked.

```Text only
docker inspect hmac-signature-service
    ..
    ...
    "Env": [
        "APP_SECRET=mysecret",
        "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "LANG=C.UTF-8",
        "GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568",
        "PYTHON_VERSION=3.9.9",
        "PYTHON_PIP_VERSION=21.2.4",
        "PYTHON_SETUPTOOLS_VERSION=57.5.0",
        "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/3cb8888cc2869620f57d5d2da64da38f516078c7/public/get-pip.py",
        "PYTHON_GET_PIP_SHA256=c518250e91a70d7b20cceb15272209a4ded2a0c263ae5776f129e0d9b5674309"
    ],
    ...
    ..
```

Additionally, you can get the \`process id\` of the app inside the container (\`1869799\` in this case) and then look at the content of the \`/proc/[pid]/environ\` file and your application secret will be there too.

```Text only
docker inspect hmac-signature-service
       ...
       ..
       .
       "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 1869799,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2021-12-14T08:40:24.338541774Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },

pstree -sg 1869799

systemd(1)───containerd-shim(1869776)───gunicorn(1869799)─┬─gunicorn(1869799)
                                                          ├─gunicorn(1869799)
                                                          ├─gunicorn(1869799)
                                                          └─gunicorn(1869799)

sudo cat /proc/1869799/environ

PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/binHOSTNAME=6a9110ff90e1APP_SECRET=mysecretLANG=C.UTF-8GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568PYTHON_VERSION=3.9.9PYTHON_PIP_VERSION=21.2.4PYTHON_SETUPTOOLS_VERSION=57.5.0PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/3cb8888cc2869620f57d5d2da64da38f516078c7/public/get-pip.pyPYTHON_GET_PIP_SHA256=c518250e91a70d7b20cceb15272209a4ded2a0c263ae5776f129e0d9b5674309HOME=/root%
```

## Mount secret file to the container and read from there instead {#mount-secret-file-to-the-container-and-read-from-there-instead}

You can fix that by doing a small change in the application source code, mainly how the application reads the secret, this time instead of reading from the \`APP_SECRET\` environment variable the app will read from a file located at \`/tmp/app/secret\`.

```Tera Term macro
secret_path = "/tmp/app/secret"
app_secret = open(secret_path).readline().rstrip() if os.path.exists(secret_path) else ""
```

Build the [docker](https://www.docker.com/) image and run the container mounting the secret file.

```GDScript
docker build -t alevsk/app-env-vars:latest .
docker run --rm --name hmac-signature-service -p 5000:5000 -v $(pwd)/secret:/tmp/app/secret alevsk/app-env-vars:latest
```

The secret file looks like this:

```Text only
mysecret
```

Try `curl` again:

```Text only
curl http://localhost:5000/?message=eaeae

Original message: eaeae
Signature: cce4625d3d586470bc84ac088b6e2ae24c012944832d54ab42a999de94252849%
```

The generated signature looks good, if you inspect the container you will not see the secret used by the application.

```Text only
docker inspect hmac-signature-service
    ..
    ...
    "Env": [
        "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "LANG=C.UTF-8",
        "GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568",
        "PYTHON_VERSION=3.9.9",
        "PYTHON_PIP_VERSION=21.2.4",
        "PYTHON_SETUPTOOLS_VERSION=57.5.0",
        "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/3cb8888cc2869620f57d5d2da64da38f516078c7/public/get-pip.py",
        "PYTHON_GET_PIP_SHA256=c518250e91a70d7b20cceb15272209a4ded2a0c263ae5776f129e0d9b5674309"
    ],
    ...
    ..
```

Also, if you exec into the container by running \`docker exec -it hmac-signature-service sh\` the \`APP_SECRET\` environment variable is not there, nor in the \`/proc/1/environ\` file or in the \`printenv\` command output.

```Text only
cat /proc/1/environ

PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/binHOSTNAME=afe80d4cafcaLANG=C.UTF-8GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568PYTHON_VERSION=3.9.9PYTHON_PIP_VERSION=21.2.4PYTHON_SETUPTOOLS_VERSION=57.5.0PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/3cb8888cc2869620f57d5d2da64da38f516078c7/public/get-pip.pyPYTHON_GET_PIP_SHA256=c518250e91a70d7b20cceb15272209a4ded2a0c263ae5776f129e0d9b5674309HOME=/root

printenv

HOSTNAME=afe80d4cafca
PYTHON_PIP_VERSION=21.2.4
SHLVL=1
HOME=/root
GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568
PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/3cb8888cc2869620f57d5d2da64da38f516078c7/public/get-pip.py
TERM=xterm
PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
LANG=C.UTF-8
PYTHON_VERSION=3.9.9
PYTHON_SETUPTOOLS_VERSION=57.5.0
PWD=/app
PYTHON_GET_PIP_SHA256=c518250e91a70d7b20cceb15272209a4ded2a0c263ae5776f129e0d9b5674309
```

## What if I cannot change the source code of my application? {#what-if-i-cannot-change-the-source-code-of-my-application}

In case you don't have access or cannot change the source code of the application not all is lost This time, instead of passing the \`APP_SECRET\` environment variable via docker \`-e\` flags, you will mount a \`secret\` file directly into the container and then modify the container entry point to source from that secret file.

The \`secret\` file will contain something like this:

```GDScript
export APP_SECRET="mysecret"
```

Launch the container like this:

```GDScript
docker run --rm --name hmac-signature-service -p 5000:5000 -v $(pwd)/secret:/tmp/app/secret --entrypoint="sh" alevsk/app-env-vars:latest -c "source /tmp/app/secret && gunicorn -w 4 -b 0.0.0.0:5000 main:app"
```

This will prevent the \`APP_SECRET\` environment variable to be displayed if someone runs the \`docker inspect\` command.

```Text only
docker inspect hmac-signature-service
    ..
    ...
    "Env": [
        "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "LANG=C.UTF-8",
        "GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568",
        "PYTHON_VERSION=3.9.9",
        "PYTHON_PIP_VERSION=21.2.4",
        "PYTHON_SETUPTOOLS_VERSION=57.5.0",
        "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/3cb8888cc2869620f57d5d2da64da38f516078c7/public/get-pip.py",
        "PYTHON_GET_PIP_SHA256=c518250e91a70d7b20cceb15272209a4ded2a0c263ae5776f129e0d9b5674309"
    ],
    ...
    ..
```

However \`APP_SECRET\` will still be visible inside \`/proc/[container-parent-pid]/environ\` (requires to be inside the container or root privileges on the machine running the container)

## Takeaway {#takeaway}

Environment variables are great but the risk of leaking secrets is just not worth it, if you give access to the docker command to somebody on your system that person can pretty much look what's running inside the container by running the docker inspect command (having docker access is equivalent to have root access on the system anyways), because of this reason it's preferable that applications read configurations and secrets directly from files and to leverage on the OS file system permissions.

Download the source code of the app here: [https://github.com/Alevsk/docker-containers-env-vars-security](https://github.com/Alevsk/docker-containers-env-vars-security)

Happy hacking

 [1]: https://www.alevsk.com/2020/06/docker-images-are-just-tar-files/ "docker image"
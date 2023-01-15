---
title: Docker images are just TAR files!
author: Alevsk
type: post
date: 2020-06-29T07:41:13+00:00
url: /2020/06/docker-images-are-just-tar-files/
categories:
  - Linux
  - Personal
  - Sin categoría
  - Technology
  - Tips
  - Tutorials
tags:
  - containers
  - docker
  - Kubernetes
  - Linux

---
[![](/images/linux-docker-support-cb-liveops-0x0-c-default@2x-1200x492.png)](https://www.alevsk.com/2020/06/docker-images-are-just-tar-files/linux-docker-support-cb-liveops-0x0-c-default2x/)

I have been using **Mac OSX** for development for half a decade now, I love the macbook pro design, the operating system and that everything works out of the box, but I've always struggled with the fact that once you got your mac you “cannot" upgrade its components, that is a problem if you are a **distributed systems** engineer and the projects you are working on increase in complexity (ie: adding new services), of course you can always rent a big machine on the cloud but sometimes you just don't have an Internet connection.

Anyway this blog post it's about how can you transfer docker images between docker registries on different machines, currently I'm using a 15 inches 2019 Macbook pro with 16GB of Ram and when I open a couple of Chrome windows, IntelliJ and run a couple of services everything start to run very slow. I need more power.

[![](/images/chrome_windows.png)](https://www.alevsk.com/2020/06/docker-images-are-just-tar-files/chrome_windows/)

So a couple of weeks ago I got the Lenovo X1 Extreme Gen 2 with 6 cores and 64GB of Ram, powerful enough, this laptops come with Windows preinstalled and you can even play videogames on them, but the main goal was to leverage the resources to the Macbook pro and I was not planning on switching machines right now, I love Linux, I use it every day but I still think the Linux desktop experience isn't great yet, so the first thing I did was to install **PopOS** [https://pop.system76.com/](https://pop.system76.com/) a distro based on Ubuntu.

In previous blog post I've explained how to **enable SSH**, add the public key of your clients to the **authorized_keys** file and create **ssh configs** in Linux box, you will need all of that [https://www.alevsk.com/2020/03/build-your-own-private-cloud-at-home-with-a-raspberry-pi-minio/][1]. 

Once you have ssh access enabled, and **docker** installed with a couple lines of bash you can start transferring docker images between your machines.

Let's say you have a **docker image** called **minio/minio:edge** in your local registry and want to use it in your remote machine (and you don't want to use the docker public registry for that), first you will need to export the image as a TAR file:

```bash
docker save -o /tmp/minio.tar minio/minio:edge
```

Next is transfer the file to the remote machine using scp.

```bash
scp /tmp/minio.tar user@remote:/tmp/minio.tar
```

Finally load that image in the remote docker registry via ssh.

```bash
ssh user@remote "docker load -i /tmp/minio.tar"  
rm -rf /tmp/minio.tar
```

It's a simple trick but it's very useful and allowed me to have this dual laptop setup.

[![](/images/IMAGE-2020-06-29-000855-1068x800.jpg)](https://www.alevsk.com/2020/06/docker-images-are-just-tar-files/image-2020-06-29-000855/)

You can put all of this on a simple script, I called it **dockerc**.

```bash
#!/bin/bash  
set -x

if [ $# -eq 0 ]; then  
echo "Usage: dockerc minio/minio:edge"  
exit 1  
fi

echo "Copying container: $1"

IMAGE\_TAR\_FILE="image.tar"

REMOTE_HOST=""  
REMOTE_USER=""  
REMOTE_PATH="/tmp/"

LOCAL_PATH="/tmp/"

ABS\_REMOTE\_IMAGE=$REMOTE\_PATH$IMAGE\_TAR_FILE  
ABS\_LOCAL\_IMAGE=$LOCAL\_PATH$IMAGE\_TAR_FILE

docker save -o $LOCAL\_PATH$IMAGE\_TAR_FILE $1  
scp $ABS\_LOCAL\_IMAGE $REMOTE\_USER@$REMOTE\_HOST:$ABS\_REMOTE\_IMAGE  
ssh $REMOTE\_USER@$REMOTE\_HOST "docker load -i $ABS\_REMOTE\_IMAGE && rm -rf $ABS\_REMOTE\_IMAGE"  
rm -rf $ABS\_LOCAL\_IMAGE
```

And just do.

```bash
./dockerc minio/minio:edge
```

## Bonus

If you wish to run more commands apart of **docker load** (in my case I'm using [kubernetes kind](https://kind.sigs.k8s.io/)) you just keep adding more after the **&&**, ie:

```bash
docker load -i $ABS\_REMOTE\_IMAGE && kind load docker-image $1 && rm -rf $ABS\_REMOTE\_IMAGE
```

Happy Hacking 🙂

 [1]: http://Build your own private cloud at home with a Raspberry Pi + Minio
---
title: I used AI to successfully migrate my website infrastructure
author: Alevsk
type: post
date: 2023-01-17T00:41:33+00:00
url: /2023/01/i-used-ai-to-successfully-migrate-my-website-infrastructure/
categories:
  - AI
  - Personal
  - Programming
  - Technology
  - ChatGPT
tags:
  - AI
  - Personal
  - Programming
  - Technology
  - ChatGPT

---

![artificial-intelligence.jpg](/images/artificial-intelligence.jpg)

## Motivation

A few days ago, I finally accomplished something that has been on my TO-DO list for a couple of years now. The task was simple, to migrate my personal blog https://www.alevsk.com (and some other websites), to a modern and more scalable infrastructure compared to what I’ve been using for the last 15 years.

I started my personal blog in 2008 (right before college). The main purpose was to be a place where I could document new things I was learning at the moment, to build my online identity and, in general, it was some kind of “digital sanctuary” in which I was able to experiment and express myself. Over the ~15 years my blog has existed (under different domains), I have experimented with managed services like wordpress.com and blogger, shared hosting and at some point I decided to get my own VPS because the number of websites I was managing at the moment started to grow.

![blog-evolution.jpg](/images/blog-evolution.jpg)

At that time, the LAMP stack started to get popular and I was interested in learning more about web development, so I set up my server with Linux, Apache, MySQL and PHP and everything worked perfectly, until it didn't.

![LAMP-architecture.png](/images/LAMP-architecture.png)

Some of the disadvantages in this architecture included a PHP version that was fixed for all the websites running on the server (At some point I managed to squeeze over 30 websites in this poor 5 usd instance). Many times I was in a situation where I was unable to upgrade because some of the websites were not compatible with the newest version of PHP. I remember another time where one of the pages started receiving so much traffic that it killed the database and, because the database was down, all the other websites went down as well.

To compensate, I installed (and learned) additional software, from monitoring tools like [Monit](https://mmonit.com/monit/) that will notify me when a service is down and try to restore it automatically to custom bash scripts and even cron jobs that will restart my server everyday at midnight.

Another thing that was problematic was managing the server. Most of the time I’ll have to ssh into the server to fix something or transfer files via sFTP or scp to update some of the websites. 

Don’t get me wrong, I learned a ton using the LAMP stack. These technologies were one of the most accessible and easiest to learn at the time and somehow I managed to make my server work with an infrastructure like that for over 10 years.

## It was time for a change

In Mexico we have a saying:

> En casa de herrero azadón de palo

The closest translation in English would be:

> The shoemaker's son always goes barefoot

Which means how ironic a situation like this is, where I work every day with modern technologies, but my own personal blog runs with technologies of the last decade.

I’ve been working with containers and cloud technologies for several years now. I've seen the benefits these technologies bring to the table when it comes to scalability, resilience, security, high availability and how easy it is to deploy and make new changes to them. The natural step for me was to migrate from the old LAMP stack to a modern architecture based on container technologies. Furthermore, I want to achieve the following:

- Add versioning to all websites to keep track of changes and be able to rollback
- Containerize existing application
- Some of the websites like [www.alevsk.com](http://www.alevsk.com) don’t really need to run on wordpress or need a database to store their content, instead it is enough to use something like [gohugo.io](https://gohugo.io/) that generates static content
- Ability to manage and deploy new applications without having to ssh into the server
- Single entry point (reverse proxy) for traffic into the server that can be audited and where TLS certificates can be managed and renewed automatically
- Automatically deploy new versions of the websites every time there’s a new change or a new release (CI/CD)

There was so much more I wanted to do, but the above was a good place to start and I estimated the effort for my project to be, at least, a couple months, working a few hours every weekend, but because of many different reasons, it has been on my plate for around 2 years now. But then something happened.

## ChatGPT and the start of a new Era (At least for me)

I’ve been using [ChatGPT](https://es.wikipedia.org/wiki/ChatGPT) for a couple of months now. I started, like everyone else, using it for fun, generating fictional stories or asking it to write songs and poems, but then at some point, I started integrating it into the workflows of some of my personal projects and I was impressed by how fast I was making progress.

Then at some point I thought, If I spend one weekend working on the migration of my infrastructure with the help of AI, how far would I get? In this post I’m going to describe some of the most interesting parts in which AI helped me to migrate [www.alevsk.com](http://www.alevsk.com).

Creating the github repositories and setting up the container environment was the easy part. I have done that a dozen times already. Sames goes for containerizing applications, most probably there’s already a [certified container image](https://catalog.redhat.com/software/containers/ubi8/ubi/5c359854d70cc534b3a3784e) for every environment you imagine. However, in my case, I had some dynamic PHP websites, like my blog, that their whole purpose is to display content stored on a database and that content doesn't change very often, so I decided that I want to migrate away from [wordpress CMS](https://wordpress.com/) to static content generated by [gohugo.io](https://gohugo.io/) that will not require any sort of backend or a database.

### Parsing HTML to Markdown

I started by using a plugin called [WordPress to Hugo Exporter](https://github.com/SchumacherFM/wordpress-to-hugo-exporter). This plugin allowed me to export all my existing publications into markdown format, however the first issue arrived. Because of the use of some plugin, most of the markdown code was malformed and some of the documents even contained invalid HTML. I tried to manually fix a couple of documents and I quickly realized that would be an impossible task, so I asked the AI for help.

![chatgpt-1.png](/images/chatgpt-1.png)

The idea was simple: If I have some python code that Iterates over all the existing markdown files and I somehow parse the missing/buggy HTML into a valid markdown, all the content from my blog will be migrated, so I asked the AI to do exactly that. I asked to create functions to scan the files and fix the markdown by doing the following:

- Convert HTML images to Markdown images and preserve alternate text for the image
- Convert code inside the  html tag to markdown code blocks
- Convert HTML quotes to markdown blockquotes
- Convert HTML links to markdown links
- Use the correct programming language in the markdown code blocks so the code is highlighted correctly
- Convert HTML tables to their markdown equivalent (I was very impressed with this one)

![chatgpt-2.png](/images/chatgpt-2.png)

The result was a python script that fixed about 90% of the content of my blog. You can see the actual program here [alevsk.com/parser.py at master · Alevsk/alevsk.com · GitHub](https://github.com/Alevsk/alevsk.com/blob/master/parser.py).

### Deleting unused images

The AI also helped me to create a script that deletes unused images. That way I saved some space when building the container image of my blog. It is not the most efficient script but it was fine because this was an operation that I had to run only one time. The script is here [alevsk.com/image_cleaner.py at master · Alevsk/alevsk.com · GitHub](https://github.com/Alevsk/alevsk.com/blob/master/image_cleaner.py).

### Creating NGINX redirect rules

I chose [NGINX](https://www.nginx.com/) as the reverse proxy to route traffic into the different websites inside my server and one important part was to create those redirect rules. Again, I asked the right questions and the AI generated the redirect rules for me. Part of the content migration project was to translate some of the old tags and categories my blog has from Spanish to English. However, I didn’t want to break any existing link to my blog, so I told the AI exactly that. I provided a list of Spanish words and the translation and I asked to generate the rules.

I provided something like this:

```text
/acerca-de -> /about
/portafolio -> /work-experience
/contacto -> /about
/tag/$tag -> /tags/$tag
/category/$tag -> /categories/$tag

Noticias Informáticas -> IT News
Platicas y congresos -> Talks and Events
Programacion -> Programming
Redes Sociales -> Social Media
Tecnologia -> Technology
Soluciones -> Solutions
Tutoriales -> Tutorials
Hola mundo -> Hello World
Juegos -> Gaming
Hacking Etico -> Ethical Hacking
Eventos -> Events
noticias -> News
ciclos excesivos -> Linux Debugging
discos duros -> Storage
ciencia -> Science
cine -> Movies
pitagoras -> Math
fin de semana -> Weekends
gobierno -> Government
robotica -> Robotics
seguridad -> Security
busquedas -> Search
```

The AI generated this beautiful nginx configuration file [alevsk.com/nginx.conf at master · Alevsk/alevsk.com · GitHub](https://github.com/Alevsk/alevsk.com/blob/master/nginx/nginx.conf#L50) based on the request above.

![chatgpt-3.png](/images/chatgpt-3.png)

Even when I had some weird bugs in my configuration, I explained to the AI my issue and the AI was able to point out the problem and provide a solution which saved me hours of manual debugging.

![chatgpt-4.png](/images/chatgpt-4.png)

> It was like having an Nginx consultant with me all weekend.

### Automating everything using CI/CD

Finally, with the help of AI, I created a github action that will build and push a new image container every time there is a merge into the master branch of the repository. You can see the actual file here [alevsk.com/jobs.yaml at master · Alevsk/alevsk.com · GitHub](https://github.com/Alevsk/alevsk.com/blob/master/.github/workflows/jobs.yaml).

![container-architecture.png](/images/container-architecture.png)

The final architecture after completing the migration looks similar to the above image. Now I’m able to manage all my websites from a UI, renew certificates and do everything without having to ssh into the server. I can quickly deploy new applications, create additional replicas or do rollbacks if necessary. If one website is down, that doesn’t impact any other. In general, I’m very satisfied with the result.

## Final thoughts

ChatGPT and AI in general are very interesting technologies. They are not magic, even if it sometimes feels like that. ChatGPT is the result of training a model using massive amounts of data to generate human-like text responses about everything you want.

Another important thing to mention is that the results I got from the AI worked around 60% of the time and that's fine. Many times I didn’t get the result I wanted the first time, so I had to ask again, adding different constraints every time. Other times the AI made silly mistakes that I fixed manually and that’s fine too. In the end, I finished the content migration using a combination of AI and find/replace across all the files.

This works only because I have been working with these technologies for over a decade now. I’m very experienced with them and I know exactly what it has to be done and how to do it or make the AI do it.

To be clear, I don’t think AI will replace me anytime soon. On the contrary, I’m using AI to my advantage and to expand my abilities. I'm embracing AI and I’m seeing the benefits of integrating it into my workflows and how it makes me more productive. For the project above, I initially estimated it to be two months of work and I ended up finishing the migration in just 4 days! If anything, I’m excited about what new projects I’ll do with the help of AI.

Happy hacking

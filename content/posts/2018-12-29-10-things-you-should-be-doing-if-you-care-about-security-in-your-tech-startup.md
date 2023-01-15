---
title: 10 things you should be doing if you care about security in your Tech Startup
author: Alevsk
type: post
date: 2018-12-29T19:50:30+00:00
url: /2018/12/10-things-you-should-be-doing-if-you-care-about-security-in-your-tech-startup/
categories:
  - cloud
  - Geek
  - Ethical Hacking
  - Linux
  - Mac
  - Networking
  - IT News
  - Personal
  - Sin categoría
  - Technology
  - Tips
tags:
  - hacking
  - infosec
  - Malware
  - security
  - Security
  - startup

---
![](/images/GettyImages-808157766-infoSec.jpg) 

I've been working in the startup world as a Software Engineer for a little bit more than two years now, as most of you already know, I'm very passionate about information security so I decided to create a list of things you can do to protect your technology Startup (most of them for free).

SPOILER ALERT: This publication is not going to be your typical article about which crypto cipher is better to use, IDS comparisons or talking about specific DLP products , instead, I would like to cover 10 actions (more like advices) you can take if you value your product, your data, your employees and if you want to protect your Startup in general.

So if you are the CEO, CTO, some high executive or a decision maker in your Startup this information is for you.

## 1: Enforce the use of password managers

Everything starts with a password, literally, sign-in into your computer is one of the first thing most of you do every morning. Whether email clients, social networks, instant messaging apps, or online banking all this requires the user to provide a password in order to access the service so it's natural for common users to want to think in a password only 1 time and then reuse it across multiple services.

Reusing passwords (even with small variations) it's a bad thing because once your password is guessed/stolen it can be used to compromise all your other accounts (facebook, twitter, instagram, gmail, outlook, etc), attackers can automate the process using hacking tools such as [credmap: The Credential Mapper.][1]

So how do we prevent employees passwords to be guessed ([dictionary attack][2]) while at the same time make sure they are using strong and unique passwords on each one of their accounts? The answer is **Password Managers**.

Password Managers allow you to have one master password (for choosing a strong master password please refer to my talk [How to create secure passwords][3]) and then generate all the others you need based on a secure configuration such as secret length, character types, etc.

![](/images/Screen-Shot-2018-12-17-at-11.13.26-PM.png)

So the next time you want to access your favorite social network you just need to copy and paste the password, that also prevents your password for being stolen in case of a keylogger attack. You don't want your community manager accounts to be stolen right?

There are a lot of good solutions out there for managing your passwords, some of them are free and open-source and some others requires you to buy a license, I personally use [KeePass][4] which is free, here is a list of the most popular password managers, doesn't matter which one you want to choose but go ahead and start using password managers if you are not doing it yet!

  * [1Password](https://1password.com/)
  * [KeePass](http://keepass.info/)
  * [LastPass](https://lastpass.com/)
  * [Dashlane](https://www.dashlane.com/)

## 2: Use multi-factor authentication if possible

The key of security is to add multiple layers of protection so in case one of them fails the other ones handle the risk, in particular for protecting accounts we can suggest our employees to use 2 factor or [multi-factor authentication][5] every time they can, so if a data breach happen and the passwords are stolen and cracked, attackers are still unable to log into the accounts because they are missing the token generator.

Now a days most of the more popular services support multi-factor authentication using [one time passwords][6], token generators (such as [google authenticator][7]) or even hardware authenticator devices.

Personally I use a [Yubico][8] authenticator key and I'm very happy with it 🙂 every time I need to access my accounts from a new IP address or an unrecognized browser, websites such as Facebook or Gmail will ask for my authentication key, that's very helpful because even if my password is leaked/cracked or someone guess it, they still need the physical key to access the service. 

![](/images/YubiKey-4-keychain-and-YubiKey-4-Nano-1095x800.png)

If you don't have a budget or prefer not to spend money on this you still can enforce multi-factor authentication using these free apps (every employee can have a token generator right on his smartphone):

  * [Google Authenticator][9]
  * [Authy][10]
  * [Lastpass Authenticator][11]

## 3: Choose a secure instant messaging application

![](/images/channels-inbox-whatsapp.png)

Every organization use some kind of real time communication application (Slack, Microsoft Teams, etc) and sometimes employees need to share sensitive information between them, they do not realize the information is also being shared with the third-party service provider who can read it.

Fortunately, nowadays more and more services support security features such as [end to end encryption][12] which means all communications between devices are encrypted (each device has a [public and a private key][13]) and not even the service provider can read them because they don't have the private keys.

![](/images/Screen-Shot-2018-12-20-at-12.59.43-AM-1200x621.png)

Another cool feature is self-destruct messages, basically you can set a timer so messages only exists during a particular amount of time after being send and then are destroyed, very useful when you want to share sensitive data such as passwords. 

![](/images/Screen-Shot-2018-12-20-at-12.41.27-AM-542x800.png)

Some free apps that include these features are:

  * [Keybase][14]
  * [Telegram][15]
  * [Signal][16]
  * [Wire][17] (It has a free version)

## 4: Securing all Email communications

Email communications is an essential part in every organization, making it a very attractive vector for attackers, according to a new report from [PhishMe][18], 91% of Cyberattacks start with a phishing email, so even if you have advanced network controls, deceiving your users is still easy.

Nowadays attackers have access to sophisticated phishing tools like [SET (Social-Engineer Toolkit)][19] or [Gophish][20] which they use to target your employees, they also have access to large repositories of [open-source phishing tools][21] they use to tune and adapt their attacks to specific people.

Most of this tools allow attackers to spoof corporate emails and trick your users into downloading malicious files into their systems and into your network, spotting spoofed email addresses is very difficult for common users however using security software like [PGP (Pretty Good Privacy)][22] & GPG can help you to mitigate the issue.

Enforcing the use of software such as [GPG (GNU Privacy Guard)][23] could help your startup in many ways, like verify the legitimacy of a received messages or encrypt an email content so only a specific user can read them.

You can verify if a message you receive is legit by using the public key of the sender (usually another employee in the organization), meaning: if the person that sent you the email also signed the message using his private key and that private key is associated with the public key you have, then you are guaranteed the message is coming from the right person.

I know this sounds a little bit confusing at the beginning, but the main idea is that every person in the company has a [key pair][24], a **public key** and a **private key**, everybody exchanges their public keys while keep their private keys to themself, so when I want to send a message to Mr John Doe I write the message normally and then I proceed to sign it with my own secret key, optionally I can encrypt the message using the public key of John Doe, so the message can only be decrypted and read it by the private/secret key of John, finally John can use my public key to verify the signature I applied to the original message (the one I generated with my private key).![](/images/Screen-Shot-2018-12-28-at-12.25.27-AM-1200x434.png) 

If you still don't get it don't worry about it, nowadays most email clients support PGP and the process for verifying and decrypting emails is automatically, there is also a chrome extension called [FlowCrypt][25] that I highly recommend!

![](/images/Screen-Shot-2018-12-28-at-1.02.46-AM-1027x800.png)
![](/images/Screen-Shot-2018-12-28-at-1.04.54-AM-1200x685.png)

## 5: Encrypting all your drives

Now we are introducing the concept endpoint protection and “[data loss prevention][26]“, in fact I think most of you already use some form of data encryption software, I'm not going to go deep into the details but encrypting your drives could protect your data in many cases, ie: someone steal a company hard drive and try to mount it in another computer to read the information.

If your employees are **MacOS** users, the operating system already come shipped with [FileVault][27] enabled by default, if they use **Windows** they can use [BitLocker][28] and if they use a modern Linux distribution (ie: **Ubuntu**) [full disk encryption][29] is also available.

![](/images/Screen-Shot-2018-12-22-at-12.17.28-AM-933x800.png)

Data encryption has pros and cons, but the benefits are superior from a privacy and security stand point so I highly recommend to use full disk encryption in all company devices if possible, also the solutions I mentioned above are all free, so you don't need to spend any money on this one too in order to protect your employees.

## 6: Encourage secure coding best practices

![](/images/the-secure-developer-1024x1024-800x800.jpg)

Usually, when you start a new company then financial resources are limited and you need to be very careful with the people you hire, basically you want to have the best developers, people that are really good at whatever they do but also are wiling to learn and adapt to different situations, you want Rockstar developers.

Rockstars developers have the potential for learning anything, so feed them with the right content, [Open Security Training][30] contains great resources about different topics of security like [Introduction to Secure Coding][30], the best part is, are you ready?, its all FREE! in fact this is how I have been learning about security all this years.

Besides **Open Security Training** there is also **The Open Web Application Security Project** [(OWASP)][31], which is also a good resource for starters so they can learn how to create secure [web applications][32] and also [secure mobile apps][33].

Everybody can learn about Security these days, encourage your developers to do it (give them time and resources) and your team will become stronger!, here are some extra sources I had used in the past:

  * [Microsoft Security Development Lifecycle (SDL)][34]
  * [Cybrary: Secure code training course][35]
  * [SAFECODE training][36]

## 7: Consider hiring a security expert to join your team or an external security team

This advice is more for mature startups or executives who already have a budget to spend on cybersecurity, but it can also apply if you are a small startup and have some friends in the security community.

![](/images/Security-man-expert-suit-e1467360748311.jpg)

The idea is to have someone in your team that can give you advice and guidance on different security matters, ie: implementing a security plan for the software development process, do [threat modeling][37] in your organization, security infrastructure (IDS, IPS, firewalls, etc), security training, network protection or just make sure your employees are safe are just some examples of things your tech Startup needs from a security perspective.

Besides having your own **security guy** consider hiring an external security team too, having the security assessment of an external team allow you to simulate more realistic attacks to your organization so you can be more prepared when the real thing happen.

Here are some personal thoughts about security people:

  * Security people are different
  * We enjoy talking about security all the time
  * We want to get asked about how to protect X or Y technology
  * We enjoy challenges and puzzles
  * we enjoy to break stuff and tell you how to fix them.

## 8: Start a bug bounty program

![](/images/bug-bounty-programs-e1518156198401.png)

Companies doesn't like the idea of their product being hacked, personally I believe that way of thinking need to change because it's a good thing to have a group of **white hat hackers** finding vulnerabilities in your software before the bad guys do it.

You can start a bug bounty program with a well defined scope so people can try to hack your product legally (you can even set some special environments for this), there are some guidelines regarding how much to pay depending on the type of vulnerability but if you are still a small startup you can also offer some “swag" like t-shirts or gadgets. 

In return you get (most of the time) an army of high quality security researchers that will deliver good vulnerability reports, including how to fix your security issues, everybody wins 🙂

Some popular bug bounty platforms right now are:

  * [BugCrowd][38]
  * [HackerOne][39]

## 9: Encourage a cybersecurity culture in the Startup

The success of the cybersecurity strategy in the organization depends pretty much on the people, you can not just spend a lot of money on security assets like Firewalls and Antivirus and expect everything to be magically safe, it's not possible because people are always the weakest part in the chain. Security is like a game and everybody need to play including high executives like CEOs and CTOs.

In order to have a culture of cybersecurity organizations have tried different things through the years, even punishing their employees, which is not very effective because people end hating security policies. In general people tend to care about security only when affects them directly but they also like rewards so there is a “new" trend in the **security community** about using gamification in which basically you reward your employees when they have a responsible security behaviour.

Those action might include:

  * Employees getting rewards when reporting phishing emails
  * Escort people without badge outside the facilities
  * Report suspicious USB drives or hardware that should not be there to the IT/Security department.
  * Enforce people to lock their workstation when not using them by sending emails (using the unlocked account) about free donuts for the whole floor/department/team :p

The idea of all this is to be fun while at the same time the organization become more secure against external threats.

## 10: Be transparent about Security issues and data breaches

![](/images/bigstock-Data-Breach-Word-Cloud-Collage-190228822-1067x800.jpg)

Your biggest fear became true, your Startup got hacked and your information is all over the Internet, If you followed all my advices chances are your sensitive information like passwords are encrypted, which is useless for the attackers, however you still have a moral (and in some places legal) duty, you need to notify your customers and employees about the data breach (according to **GDPR** [you have 72 hours to report a personal data breach after it's discovered][40]) basically every minute you wait is a minute attackers can invest into cracking and recovering the information so it's better to communicate the incident, so people can start acting accordingly (change passwords, cancel credit cards, etc).

If you decide to hide the breach and continue without doing anything eventually everybody is going to know about hack and your reputation will be irreversibly damaged (nobody will trust you anymore) so its better to be open with your customers an accept the failure, the shame will be momentary but you will do the right thing.

There is no such thing as a Silver bullet in **Cybersecurity**, It's not a matter of if you are going to be hacked or not, it's about when is going to happen and if your organization is going to be prepared, and this is true for all companies.

## Some final thoughts

Security people are often seen as blockers in the organization but I assure you, they have good intentions so please listen to them. Security is hard to implement and even harder to maintain so if you are the CEO/CTO/[Person with authority] of the startup consider to join the security team so you can experience first hand the whole process 🙂

Finally, all these advices are based on my personal opinion (I'm just a security enthusiast) so if you think I should add something else please leave it in the comments.

Happy hacking 🙂

 [1]: https://github.com/lightos/credmap
 [2]: https://en.wikipedia.org/wiki/Dictionary_attack
 [3]: https://www.alevsk.com/2016/06/platica-contrasenas-seguras/
 [4]: https://keepass.info/
 [5]: https://en.wikipedia.org/wiki/Multi-factor_authentication
 [6]: https://en.wikipedia.org/wiki/One-time_password
 [7]: https://support.google.com/accounts/answer/1066447?co=GENIE.Platform%3DAndroid&hl=en
 [8]: https://www.yubico.com/
 [9]: https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en
 [10]: https://authy.com/
 [11]: https://lastpass.com/auth/
 [12]: https://en.wikipedia.org/wiki/End-to-end_encryption
 [13]: https://en.wikipedia.org/wiki/Public_key_infrastructure
 [14]: https://keybase.io/
 [15]: https://telegram.org/
 [16]: https://signal.org/
 [17]: https://wire.com/en/
 [18]: https://cofense.com/
 [19]: https://www.trustedsec.com/social-engineer-toolkit-set/
 [20]: https://getgophish.com/
 [21]: https://github.com/topics/phishing
 [22]: https://www.openpgp.org/
 [23]: https://www.gnupg.org/
 [24]: https://en.wikipedia.org/wiki/Public-key_cryptography
 [25]: https://flowcrypt.com/
 [26]: https://en.wikipedia.org/wiki/Data_loss_prevention_software
 [27]: https://support.apple.com/en-us/HT204837
 [28]: https://support.microsoft.com/bn-bd/help/4028713/windows-10-turn-on-device-encryption
 [29]: https://www.maketecheasier.com/encrypt-hard-disk-in-ubuntu/
 [30]: http://opensecuritytraining.info/Training.html
 [31]: https://www.owasp.org/index.php/Main_Page
 [32]: https://www.owasp.org//images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf
 [33]: https://www.owasp.org/index.php/Mobile_Top_10_2016-Top_10
 [34]: https://www.microsoft.com/en-us/securityengineering/sdl/
 [35]: https://www.cybrary.it/course/secure-coding/
 [36]: https://safecode.org/training/
 [37]: https://en.wikipedia.org/wiki/Threat_model
 [38]: https://www.bugcrowd.com/
 [39]: https://www.hackerone.com/
 [40]: https://www.thesslstore.com/blog/gdpr-report-personal-data-breach/
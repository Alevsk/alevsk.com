---
title: Just enough cryptography for better securing your apps
author: Alevsk
type: post
date: 2020-07-12T12:32:05+00:00
url: /2020/07/just-enough-cryptography-for-better-securing-your-apps/
categories:
  - Ethical Hacking
  - IT News
  - Programming
  - Technology
  - Tips
tags:
  - capture the flag
  - Cryptography
  - ctf
  - hacking
  - Programming
  - programming

---
![](/images/71gdZuZQFZL._AC_SL1500_-532x800.jpg) 

I'm not a **cryptographer** myself but I have always admired their work because literally they make the Internet a better place by creating technology that allows us our right to privacy and cybersecurity plus I enjoy playing basic crypto [CTF challenges][1]. At my current job I'm a weird mixture between **Software developer** and **Information Security** guy (finally the best of two worlds) that means I work a lot with **security** and crypto related matters and I'm also very fortunate for  being able to work very close to a real cryptographer, so a couple months ago we were talking about security and I asked him if he could share some resources about **cryptography** but focusing on **Software Engineers**, meaning people without a heavy background in mathematics, this is what I learned.

If you are a Software Engineer curious about Information Security chances are you have crossed paths with a task that involves adding some kind of **security mechanisms** to protect data in your application, my friend explained me that in practice, cryptography is about choosing the right tool for the job and as a **Security Software Engineer** the most common tasks you will face are:

  * Encrypt a data blob or data stream
  * Exchange a secret key with a peer
  * Verify that some data blob or data stream is not modified
  * Verify that some data blob or data stream has been produced by someone specific.
  * Generate a secret key from another secret key
  * Generate a secret key from a (low-entropy) value – e.g. password

There are out there many cryptographic mechanisms that will make our lives easier when it comes to software engineering and we need to learn how to pick the right tool for the job

I'm not saying you should completely ignore the theory and jump directly into the practice, theory is important and you should learn it or at least be aware of the different types of cryptographic primitives, the most important classes/types are:

  * Pseudo-Random Permutation (PRP) – e.g. [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
  * Pseudo-Random Function (PRF) – e.g. **ChaCha**
  * Random Oracle (RO) – e.g. **SHA-256**

Modern cryptographic algorithms usually follow a more theory-based approach when it comes to achieve its goals and test its security, they usually do that by reducing the security relative to the primitives they use, it's very common to read things like: 


> The scheme X achieves the security goals A, B and C if the underlying primitive Y is in-fact a K.
  


Primitives usually have a condition in the form of a mathematical proof or very hard problems to solve e.g. [prime-factor](https://www.coursera.org/lecture/asymmetric-crypto/prime-factorization-problem-ITnwE) representation for **RSA** asymmetric primitive or the [discrete logarithm problem](https://en.wikipedia.org/wiki/Discrete_logarithm) for the [Diffie-Hellman key exchange algorithm](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange), therefore If you want to break a cryptographic scheme you will first need to break the assumptions used by its primitives, if no one can do that then it's safe to assume the cryptographic scheme is secure.

My point here is you need to understand what are the goals you want to achieve first, what is your requirement, that's the only way you can pick the right **cryptographic scheme** based on the primitives that will solve your problem.

## Key Derivation

Let's say you have an application that calculates the [hmac-sha256](https://en.wikipedia.org/wiki/HMAC) signature of a message using the password provided by a user as a key:

![](/images/hmac_password_wrong.png) 

This works but there's a problem with this approach, calculate **hmac-sha256** signatures its trivial, with the help of a good dictionary an **attacker** can easily brute force the user password and if he succeed on obtaining the original secret he can impersonate the user in your application


Therefore, in order to make the job of the attacker more expensive in terms of time, computation and memory resources, the recommended approach is to use a Key-derivation function ([KDF](https://en.wikipedia.org/wiki/Key_derivation_function)) or password-based key derivation function ([PBKDF](https://en.wikipedia.org/wiki/PBKDF2)) when deriving a key from a password 

![](/images/hmac_derivedkey_good.png)

When I learned this concept from my friend it was mind-blowing, In general you have to distinguish between deriving a secret key from a high-entropy source, like a **cryptographic key**, or from a low-entropy source, like a password. **PBKDF** usage is about trade-offs, try to hit a parameter such that the **PBKDF** is relatively cheap to compute for you in your scenario but expensive for the attacker that tries to brute-force the secret password.

```GDScript
func deriveKey(key []byte, salt []byte) string {
	derivedKey := pbkdf2.Key(key, salt, 4096, 32, sha1.New)
	return base64.StdEncoding.EncodeToString(derivedKey)
}

func main() {
	message := []byte("hello world")
	key := []byte("super secret key")
	fmt.Println(string(key), deriveKey(key, message))
	// super secret key UJS9n/48gSEHyVK8UZPcC6vKGpsyI6mNrWexmvdtCB4=
}
```

## Data Integrity

Preserving data integrity is a crucial part when working with information, the easiest way to achieve data integrity is by encrypting the data, however sometimes you don't want to do that because encrypting and decrypting data it's an expensive operation and you only want to preserve data integrity, then the most straightforward solution is **HMAC with a RO** – like **SHA-256**.

```GDScript
func computeHmac256(message []byte, key []byte) string {
	h := hmac.New(sha256.New, key)
	h.Write(message)
	return base64.StdEncoding.EncodeToString(h.Sum(nil))
}

func main() {
	message := []byte("hello world")
	key := []byte("super secret key")
	messageHmac := computeHmac256(message, key)
	fmt.Println(string(message), messageHmac)
	// hello world yFgx2zBmFCpq9N6JuGAMRnTBN5cUwTkHBtqcAyGR2bw=
}
```

## Encryption

**Symmetric cryptographic** schemes are better for encrypting a data blob or data stream vs **asymmetric schemes** due to performance advantages, the recommendation is to use Authenticated Encryption (**AE**) or Authenticated Encryption with Associated Data (**AEAD**). There are two main **AEAD** schemes used in practice: [AES-GCM](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) and [ChaCha20-Poly1305](https://en.wikipedia.org/wiki/Poly1305). Both belong to the same class of cryptographic objects: **AEAD**.

```GDScript
func encryptAES_GCM(key []byte, message []byte) string {
	block, _ := aes.NewCipher(key)
	nonce := make([]byte, 12)
	if _, err := io.ReadFull(rand.Reader, nonce); err != nil {
		panic(err.Error())
	}
	aesgcm, err := cipher.NewGCM(block)
	if err != nil {
		panic(err.Error())
	}
	ciphertext := aesgcm.Seal(nil, nonce, message, nil)
	return base64.StdEncoding.EncodeToString(ciphertext)
}

func main() {
	message := []byte("hello world")
	key := []byte("super secret key")
	fmt.Println(string(message), encryptAES_GCM(key, message))
	// hello world gBoJuHdAm5PjNGFdr+B/8Eq58IFZKcrzz6JQ
}
```

Github example: https://gist.github.com/Alevsk/0c296f230279bd399a244d4f7d1d7b84

Happy hacking 🙂

 [1]: https://www.alevsk.com/?s=ctf
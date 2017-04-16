# Web Security

![alt tag](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

This repository contains all assignments for the course "Web Security" (NWI-IPC026) given at the Radboud University.

Note: For most of the assignments you'll need WebScarab and WebGoat. WebScarab is a Java-Application. Therefore it is highly recommended to install Java. I use an Ubuntu 16.04 image inside a VirtualBox environment. To Install Java:

```
cs@cs-VirtualBox:~$ sudo add-apt-repository ppa:webupd8team/java
cs@cs-VirtualBox:~$ sudo apt-get update
sudo apt-get install oracle-java8-installer
```

## Assignment 1

Topics covered:

* How to work with WebScarab (intercepting proxy)
* How to work with WebGoat (vulnerable web application)
* HTTP Basics
* Code Quality: Discovering clues in the HTML
* Insecure Storage: Encoding Basics
* Parameter Tampering: Bypassing HTML Field Restrictions
* Parameter Tampering: Exploit Hidden Fields
* TamperData plugin

## Assignment 2

Topics covered:

* Sessions and HTTPS
* Browser behaviour of mixed HTTP/HTTPS content
* Session Hijacking
* Session Fixation
* Brute forcing Session Cookie values with JHijack (or python_fuzzer.py)
* HSTS (HTTP Strict Transport Security)
* Session ID cookie (Secure / Httponly)

## Assignment 3

Topics covered:

* Command Injection
* Path Traversal
* PHP Injection
* (blind, numeric, string) SQL injection
* Log Spoofing

## Assignment 4

Topics covered:

* Attacks on clients: Javascript, DOM, XSS
* XSS (Cross-Site Scripting)
* Stored XSS attacks
* Reflected XSS attaacks
* SOP (Single-Origin-Policy)
* Cookie Stealing

## Assignment 5

Topics covered:

* More attacks on clients: ClickJacking/UI redressing & CSRF
* Forced (aka forceful) browsing
* CSRF (Cross Site Scripting Request Forgery)
* Improper Error Handling - Fail Open Authentication Scheme
* Concurrency - Shopping Cart Concurrency Flaw
* Sanitisation of inputs (encoding, escaping, validation)
* Cerificate manipulation
* TLS tunneling

## Exam material

Exam material includes

* the material covered in the lectures (incl. the slides), incl. the examples in the demo web pages discussed in the lectures;
* If you want to use to book for some revision, this includes the material in Chapter 7 (Web Security), Chapter 5.1 (Network Security I - Network Security Concepts), and Chapter 1.1 (Fundamental Concepts).
* the WebGoat and other lab assignments: we are not going to ask tricky details, but you may be asked things about these assignments which should be easy to answer if you did these assignments.

As a checklist to help with revision: you should at least be able to explain

* what HTTP, HTTPS, URL/URI, HTML are for
* why browsers warn about mixed HTTP and HTTPS content
* the differences between GET vs POST requests
* the different ways of realising sessions, using cookies, using a session ID as parameter in the URL, or as a hidden parameter (form field) in GET/POST requests, possibilities to combine these (e.g. linking cookies to IP address)
* what dynamically created (server side) web pages and dynamic web pages (client side) are
* how Javascript can be used, possible in combination with the DOM
* what the SOP is, and which interactions prevents, and what the motivations behind these restrictions are
* how the attacks discussed in the lectures work, what the differences between (variants of these) attacks are, incl.

	* OS command injection
	* (blind) SQL injection
	* database command injection
	* path/file name injection aka path traversal attack
	* Remote and Local PHP File Inclusion
	* HTML injection as a simple form of XSS, just for defacing websites
	* XSS (reflected, stored, or DOM-based), eg to steal cookies, or carry out other actions in the victim's browser with the user's priviliges
	* CSRF
	* forced aka forceful browsing
	* URL obfuscation
	* SSL stripping, possibly in combination with fake certificate chains by abusing absence of the check for leaf nodes, self-signed certificates, or URL obfuscation, and things like punycode and HSTS as countermeasures
	* ClickJacking/UI redressing
	and what countermeasures there are to combat them, either client- or server-side, incl.
	* sanitizing input and/or output, aka input validation or output encoding/escaping, either client-side (ie. in the browser) or server-side
	* browser plugins to control cookies, disable scripting, do domain highlighting, use puny-code, warn about clickjacking, do output validation (aka sanatize) outgoing HTTP traffic, ...;
	* access control, sandboxing or more generally applying the principle of least principle;
	* specifically for SQL injection: parameterised queries & stored procedures, ...
	* specifically for UI redressing: frame-busting, X-frame options
* which risks to privacy there are on the web, incl.
	* IP addresses
	* (third-party) cookies
	* Flash cookies
	* Etags
	* web beacons
	* browser fingerprinting
	* leaking browser history
* how the mechanism above work, and possible countermeasures, notably cookie blockers.
* attacker models, the types of attackers, attack vectors they can employ, and some of the ways cyber criminals make their money.

The list above is not exhaustive: there can be questions on any material from the lectures or the lab exercises. You will not be expected to know the precise SQL syntax or HTML syntax for any of these attacks.
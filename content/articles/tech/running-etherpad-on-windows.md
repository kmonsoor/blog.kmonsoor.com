---
Title: Running Etherpad on Windows
Date: 2016-04-22
Tags: etherpad, collaborative, document, editing, etherpad-lite, windows, build-tools
Slug: running-etherpad-on-windows
Status: Published
Summary: Though it's not a big deal, but running Etherpad as hosted on Windows is troublesome. Here's how to make it predictable and easy.
---

Though it's not a big deal, but running Etherpad as hosted on Windows is troublesome. Here's how to make it predictable and easy.

What you'd need beforehand:

**1.** Properly install system-wide Node.js, and of course NPM with it. Get the latest-and-stable from here: https://nodejs.org/en/download/.
 After installing, check it from command prompt.
 ````
C:\users\alpha\> node -v  
v5.11.0
 
C:\users\alpha\> npm verison
{ npm: '3.8.6',
ares: '1.10.1-DEV',
http_parser: '2.7.0',
icu: '56.1',
modules: '47',
node: '5.11.0',
openssl: '1.0.2g',
uv: '1.8.0',
v8: '4.6.85.31',
zlib: '1.2.8' }
````
Version(s) in your output may not be same but nothing to worry.

 
**2.** Download and install latest Python 2.7 from [Python.org](https://www.python.org/downloads/). Please note that **Python2** is needed as system-default, NOT **Python 3**.  
 Check it by running Python interpreter from command-prompt.

````
C:\users\alpha\> python
Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**3.** Now, make sure you have **Microsoft Build Tools 2013** or newer properly installed on you system. Grab it here: http://go.microsoft.com/fwlink/?LinkID=320711.  
 If the given link don't work, look for it under `Tools for Visual Studio 2013` in https://www.visualstudio.com/downloads.
 
 Only after you have done these well, proceed to download `Etherpad-lite` from http://etherpad.org/#download.
 The download size should be over **50MB**.  
 Do **NOT** go for building from the source unless you must.
 
**Download** the zip, **unzip** it, **move** it to your desired folder, and then run `start.bat` in the folder.

You will never know how much time i just saved you ... ;)
 

---
Title: Install latest Python 3 on Linux CentOS 7
Date: 2018-07-07
Tags: Linux, centos, python, centos7, python3, software-development, coding
Slug: install-latest-python3-on-centos-7
Status: Published
Summary: Install the latest and greatest Python 3 on CentOS 7 systems 
---

## Why

Not all distro created equal.   
Some are created to join the space race, some are to hold unto the leagcy, some are cutting-edge, some are cutting edge. Some are born to boot-up IoT devices some are to push out heavy graphics.

That's the fun (albeit, power) of Linux.

![CentOS 7 logo](https://i.imgur.com/6ZFCdoM.jpg){: .noZoom}

CentOS 7 is a powerful and stable distro that runs on thousands (probably, millions) production-grade servers.  
In the matter of stability, it's a beast. However, it doesn't ship with Python 3, by default. You can install it via EPEL repository, or the below simple steps.

Also, take a note. The Python **2** comes with the system, which is probably 2.7.5, do **NOT** mess with it. Many system components rely on that specific version. If you need the latest versions of 2, use `virtualenv` or `pipenv`.

### Prepare your system

Start with installing pre-requisite utilities for compilation and development support.

```bash
$ sudo yum update && sudo yum groupinstall -y "development tools"  
$ sudo yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel \
       sqlite-devel readline-devel tk-devel gdbm-devel \
       db4-devel libpcap-devel xz-devel expat-devel
```

### Download latest Python source code from Python.org
```bash
$ wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tar.xz
$ tar xf Python-3.6.6.tar.xz
$ cd Python-3.6.6
```

### Enable performance optimizations (optional, but highly recommended)
```bash
$ ./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"  
$ ./configure --enable-optimizations
```

 
### Build and install
```bash
$ make
$ sudo make altinstall
```

Now, Python 3.6.6 is ready to be used in your system; located in `/usr/local/bin/python3.6`
```bash
$ which python3.6
/usr/local/bin/python3.6

$ python3.6
Python 3.6.6 (default, Jul 10 2018, 14:04:26)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

For convenience, you can create a symbolic-link with a shorter name. 
If you had system-installed Python3 (unlikely), **don't** do this, as some system-components may depend on that specific older version of Python 3.
```bash
$ sudo ln -s /usr/local/bin/python3.6 /usr/local/bin/python3
$ python3
Python 3.6.6 (default, Jul 10 2018, 14:04:26)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
``` 

## <del>Install wheel and pip</del>
You don't need to, because `Python 3.6.6` includes these necessary tools included.
```bash
$ pip3.6 -V
pip 10.0.1 from /usr/local/lib/python3.6/site-packages/pip (python 3.6)
$ wheel version
wheel 0.29.0
```



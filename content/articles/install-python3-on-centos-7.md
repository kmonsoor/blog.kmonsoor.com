---
Title: Install Latest Python 3 on Linux CentOS-7
Date: 2018-07-07
Tags: linux, centos, python
Slug: install-python3-on-centos-7
Status: Draft
Summary: Install latest and greatest Python 3 on CentOS 7 systems 
---

## Prepare your system

Start with installing pre-requisite utilities for compilation and development support

`
$ sudo yum update  
$ sudo yum groupinstall -y "development tools"  
$ sudo yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel
`

## Download latest Python source code from Python.org
`
$ wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tar.xz
$ tar xf Python-3.6.6.tar.xz
$ cd Python-3.6.6
$ ./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
`

## Enable performance optimizations (optional, but highly recommended)
`
$ ./configure --enable-optimizations
`
 
## Build and install
`
 $ make && make altinstall
`

## Install setuptools and wheel and, of course, `pip`
`
$ wget https://bootstrap.pypa.io/get-pip.py
$ python3.6 get-pip.py
`

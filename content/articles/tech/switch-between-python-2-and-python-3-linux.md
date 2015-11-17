Title: Linux: Switch between Python 2 and Python 3
Date: 2015-07-30 11:01
Author: kmonsoor
Category: configuration, Linux, Python
Tags: env-setup, linux, python
Slug: switch-between-python-2-and-python-3-linux
Status: draft

Update & upgrade the installation

+--------------------------------------------------------------------------+
| \$ sudo apt-get update                                                   |
| </p>                                                                     |
| <p>                                                                      |
| \$ sudo apt-get upgrade                                                  |
+--------------------------------------------------------------------------+

### Dev environment

2.  confirm proper installation of python 2.7 (2.7.8 is good to go)
3.  configure system to ensure that the default Python is Python 2. Fix
    the system link if needed

+--------------------------------------------------------------------------+
| \$ cd /usr/bin                                                           |
| </p>                                                                     |
| <p>                                                                      |
| \$ sudo ln -s -f python2 python                                          |
+--------------------------------------------------------------------------+



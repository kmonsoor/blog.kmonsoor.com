Title: pep8_tonizer on for Notepad++ :  Make your Python code PEP8-compliant on editor 
Date: 2014-05-02 17:01
Author: kmonsoor
Category: Coding, configuration, Internet, Linux, Python, software, web
Tags: coding, editor, extension, free, ide, notepad++, pep8, plugin, programming, programming style, python, styleguide, tips, unofficial, web, windows
Slug: pep8_tonizer-on-for-notepad-make-your-python-code-pep8-compliant-on-editor
Status: published

*[ Please take note that this is still in beta phase. In other words, it
still has issues.]*

This script can be used to make python code, that is being edited on
Notepad++,  to comply with infamous PEP8 coding style
 [<http://bit.ly/pep8>]  
By default, autopep8 only makes whitespace changes. So does this
script.

However, this script depends on following:

<!--more-->

**[Python Script for
Notepad++](http://npppythonscript.sourceforge.net)**

This create the runtime environment for executing python scripts on
Notepad++ objects. Install by downloading via:
  <http://npppythonscript.sourceforge.net/download.shtml>  
(better choose the \*.msi option)

**[autopep8](http://pypi.python.org/pypi/autopep8)**  
This is the main library module for checking & converting to
PEP8-complying code. It, in turn, depends on
[pep8](https://github.com/jcrocholl/pep8)package.  
Installing steps via pip:

-   *pip install --upgrade pep8*
-   *pip install --upgrade autopep8*

 

**Installation**

1.   Install**pep8**
2.   Install **autopep8**
3.   install **Python Script** for Notepad++
4.   download [**pep8\_tonizer.py**](http://bit.ly/pep8_tonizer) to a
    convenient location
5.   find & copy pep8.py & autopep8.py to \<Notepad++ install
    dir\>\\\\plugins\\PythonScript\\lib
6.   start notepad++
7.   Go to Menu \>\> Plugins \>\> Python Script
8.   click "New script"
9.   find & select "pep8\_tonizer.py"
10.  Good job, all set.

 

**Usage**

After opening / creating any python source file,

1.  Go to Menu \>\> Plugins \>\> Python Script \>\> Scripts
2.  Click "pep8\_tonizer.py"
3.  Whoa !

 

**TODO list**

1.  adding options for autopep8 style configurations, currently it works
    as default
2.  automate the setup processes(dependency check as well) as much as
    possible
3.  integrate the whole process into just 1 or 2 steps

 

hope, you will enjoy !

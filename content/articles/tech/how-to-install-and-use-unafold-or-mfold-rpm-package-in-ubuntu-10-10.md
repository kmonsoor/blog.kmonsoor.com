Title: How to install and use UNAFold or mfold rpm package in Ubuntu 10.10
Date: 2011-02-17 11:32
Author: kmonsoor
Category: Bioinformatics, Ubuntu, UNAFold, virus
Slug: how-to-install-and-use-unafold-or-mfold-rpm-package-in-ubuntu-10-10
Status: published

<div dir="ltr" style="text-align:left;">

I failed to install UNAFold/mfold in Ubuntu 10.10 as the supplied binary
package was in *rpm (RedHat)* format.
</p>
Ubuntu 10.10 can't use *rpm* files to install software directly.

After doing some online resource [I found
that](http://www.debianadmin.com/install-rpm-files-in-debian-and-ubuntu.html)
it is possible to convert *rpm* files to *deb*(Debian) format by using
another package alien.

<a name="more"></a>  
But alien isn't installed by default. So I used the command,  
\#**sudo apt-get install alien**

then checked the installation by command:   
\#**alien**

if it's okay, now to simply convert the UNAFold package:  
\#**sudo alien \~/Downloads/unafold-3.8-1.i386.rpm**

the converted one is named like 'unafold\_3.8-2\_i386.deb'

now to install this package:  
\#**sudo dpkg -i unafold\_3.8-2\_i386.deb**

after installation, you can run the \*.pl scripts
with appropriate input, like:  
\#**perl /usr/bin/UNAFold.pl  \~/s1.seq**

<p>

</div>

<div class="blogger-post-footer">

![](https://blogger.googleusercontent.com/tracker/3906022655385600084-1997703369966281990?l=kmonsoor.blogspot.com)

</div>

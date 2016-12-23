---
Title: How to install and use UNAFold or mfold rpm package in Ubuntu
Date: 2011-02-17
Updated: 2016-12-22
Tags: bioinformatics, algorithm, ubuntu, package
Slug: install-and-use-unafold-mfold-rpm-package-in-ubuntu
Status: Draft
Summary: I failed to install UNAFold/mfold in Ubuntu 10.10 as the supplied binary package was in rpm (RedHat) format. How to solve it?
---

[Please note that this post has been written quite a while ago. After that, it's not been updated.]

I failed to install UNAFold/mfold in Ubuntu 10.10 as the supplied binary package was in rpm (RedHat) format.

`Ubuntu 10.10` can't use rpm files to install software directly.

After doing some online resource, I found that it is possible to convert rpm files to deb(Debian) format by using another app, named `alien`.

But `alien` isn't installed by default. So I used the command,

    $sudo apt-get install alien

then checked the installation by command:
    
    $alien

if it goes okay, now to simply convert the UNAFold package:
    
    $sudo alien ~/Downloads/unafold-3.8-1.i386.rpm

the converted one is named like `unafold_3.8-2_i386.deb`

Now use this new package for installation
    
    $sudo dpkg -i unafold_3.8-2_i386.deb

after installation, you should be able to run the *.pl scripts with appropriate input, like:

    $perl /usr/bin/UNAFold.pl  ~/s1.seq

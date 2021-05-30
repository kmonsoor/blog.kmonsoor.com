---
Title: Install the latest Zsh on CentOS
Date: 2020-10-20
Tags: zsh, centos, linux, upgrade, server
Slug: install-latest-Zsh-on-CentOS
Status: Published
Summary: If you're looking forward to install the latest version of Zsh instead of the default old one, here you go.
---

As the **default** Zsh on CentOS is usually a older version, many cool stuffs are not possible on this Zsh, like installing 
[oh-my-zsh](https://ohmyz.sh/) or using [powerlevel10k](https://github.com/romkatv/powerlevel10k) cool prompt system, it's understandable 
if you'd like to have the latest Zsh on board.   
Easy peasy !! 

**Note**: Please remember to remove the "sudo" from the commands if you are already in "root" or sudo-er mode  

We'll be following these steps:

[TOC]

# Install the pre-requisites
We need GCC (C++ compiler) and other related stuffs for building Zsh from the source code.  

```bash
$ sudo yum groupinstall "Development tools"  
$ sudo yum install ncurses-devel
```

Now, check if GCC is installed properly, by  
`$ gcc -v`  

# Download the latest source
Now, we gonna get the latest code of Zsh.  
Please update the link (in the shown command) with the latest by checking [this web-folder](https://www.zsh.org/pub/).  
Don't forget to update the filename as well, if needed.
```bash
$ cd /usr/local/src
$ sudo curl -L https://www.zsh.org/pub/zsh-5.8.tar.xz \
-o zsh-5.8.tar.xz
```

# Build & Install
Unzip the file, "dig in" to the folder, and build & install from the source.   

```bash
$ sudo tar -xf zsh-5.8.tar.xz
$ cd zsh-5.8
$ sudo ./configure && sudo make && sudo make install
```

# Final steps
 Add Zsh to the login shells by adding '/usr/local/bin/zsh' on the last line of the config file, `/etc/shells`  

```bash 
$ sudo -e /etc/shells
# Please don't forget to replace 'kmonsoor' with your username
$ sudo chsh kmonsoor
```

Update the system's default symlink to the new Zsh version.  
```bash
$ sudo ln -sf /usr/local/bin/zsh /bin/zsh
$ zsh --version
``` 

It's always a good habit to clean up after doing stuffs.  ;)
```bash
$ sudo make clean
```
  
![voila](https://i.imgur.com/BEFIOXf.jpg)

# Related
Want to have a super, cool-looking command shell? Gotcha, fam. 
Check out my blog on **[How do I Pimp up My Terminal on Linux](https://blog.kmonsoor.com/pimp-up-my-terminal/)**.

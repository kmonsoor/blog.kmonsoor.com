---
Title: Install the latest Zsh on CentOS
Date: 2020-10-20
Updated: 2021-11-11
Tags: Linux, zsh, CentOS, upgrade, server, shell
Slug: install-latest-Zsh-on-CentOS
Status: Published
Summary: If you're trying to install the latest version of Zsh instead of the default old one, here you go.
---

As the **default** Zsh on CentOS is usually an older version, many cool things are not possible on this version of Zsh, like installing 
[oh-my-zsh](https://ohmyz.sh/) or using awesome [powerlevel10k](https://github.com/romkatv/powerlevel10k) prompt system, it's understandable if you'd like to have the latest Zsh on your system.
Easy peasy !! 

**Note**: Please remember to remove the `sudo` from the commands if you are already in "root" or sudo-er mode  

We'll be following these steps:

[TOC]

# Install the pre-requisites
We need GCC (C++ compiler) and other related stuffs for building Zsh from the source code.  

```shell-session
$ sudo yum groupinstall "Development tools"  
$ sudo yum install ncurses-devel
```

Now, check if GCC is installed properly, by  
```shell-session
$ gcc -v
```  

# Download the latest source
Now, we gonna get the latest code of Zsh.  
Please update the link (in the shown command) with the latest by checking [this web-folder](https://www.zsh.org/pub/).  
Don't forget to update the filename as well, if needed.

```shell-session
$ cd /usr/local/src
$ sudo curl -L https://www.zsh.org/pub/zsh-5.8.tar.xz \
-o zsh-5.8.tar.xz
```

# Build & Install
Unzip the file, "dig in" to the folder, and build & install from the source.   

```shell-session
$ sudo tar -xf zsh-5.8.tar.xz  # the actual version of the downloaded file might be different
$ cd zsh-5.8
$ sudo ./configure && sudo make && sudo make install
```

# Final steps
 Add Zsh to the login shells by adding '/usr/local/bin/zsh' on the last line of the config file, `/etc/shells`  

```shell-session
$ sudo -e /etc/shells
$ sudo chsh $USER
```

Update the system's default symlink to the new Zsh version.  
```shell-session
$ sudo ln -sf /usr/local/bin/zsh /bin/zsh
$ zsh --version
``` 

It's always a good habit to clean up after doing stuffs.  ;)
```shell-session
$ sudo make clean
```

That's it !

![voila](https://i.imgur.com/BEFIOXfm.jpg){: .noZoom}

# Related
Want to have a super, cool-looking command shell? Gotcha, fam. 
Check out my blog on **[Pimping up My Linux Terminal](https://blog.kmonsoor.com/pimp-up-my-terminal/)**.

---
If you find this post helpful, you can show your support [through Patreon](https://www.patreon.com/kmonsoor) or [Paypal](https://paypal.me/KhaledMonsoor/) or by [buying me a coffee](https://ko-fi.com/kmonsoor). *Thanks!*

---
Title: Install latest Zsh on CentOS
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

  

* Install the pre-requisites i.e. GCC and other related stuffs for building Zsh from source.  
`$ sudo yum groupinstall "Development tools"`  
`$ gcc -v  # Check if GCC is installed properly`  
`$ sudo yum install ncurses-devel`


* Download the latest source file of Zsh. Please update the link with the latest by checking [this web-folder](https://www.zsh.org/pub/).  
`$ cd /usr/local/src`  
`$ sudo curl -L https://www.zsh.org/pub/zsh-5.8.tar.xz -o zsh-5.8.tar.xz   # update the link & filename if needed` 

* Unzip the file, "dig in" to the folder, and build & install from the source.   
`$ sudo tar -xf zsh-5.8.tar.xz`  
`$ cd zsh-5.8`  
`$ sudo ./configure && sudo make && sudo make install`

* Add Zsh to the login shells by adding '/usr/local/bin/zsh' to last line of the config file, `/etc/shells`  
`$ sudo -e /etc/shells`  
`$ sudo chsh kmonsoor  # change it to your username`

* Update the system default symlink to the new Zsh version.  
`$ sudo ln -sf /usr/local/bin/zsh /bin/zsh`
`$ zsh --version`
 
* It's always a good habit clea up after doing stuffs.  
`$ sudo make clean`



![voila](https://i.imgur.com/BEFIOXf.jpg)
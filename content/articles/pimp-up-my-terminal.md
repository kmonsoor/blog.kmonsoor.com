---
Title: Pimping up My Linux Terminal
Date: 2021-03-31
Tags: Linux, Ubuntu, terminal, CLI, Zsh, "Oh My Zsh", shell, powerlevel10k
Slug: pimp-up-my-terminal
Status: Published
Summary: How do I pimp up my Linux terminal? A quick trip through Zsh, Oh-my-zsh, and other power tools to make the command-line-based workflow smooth and cool.
---

The purpose of this post is to be my quick, copy-paste source of the commands that I use to set up my terminal on a new *nix system.
However, if someone else finds it useful, that'd be some cherries on top.

This command prompt in the below image is the end goal.

![The end goal of this post](https://i.imgur.com/oZahIog.png)

Assuming, I'm on a standard pc/server with Ubuntu Linux and I have CLI access with `sudo`. For other Linux distros or *MacOS*, some commands might be slightly different.

Step-1: Confirm that Zsh is up-to-date
--------------------------------------
While on most of the Linux systems Zsh is present by default, on others that's not the case. So, let's make sure about it.

```shell-session
$ sudo apt install zsh
```

Confirm the version. `Oh-my-zsh` recommends Zsh to be `5.0.8` or higher.

```shell-session
$ zsh --version
zsh 5.8 (x86_64-ubuntu-linux-gnu)
```

Also, you gotta make sure that `git` (recommended v2.4.11 or higher) is also installed on the system.

  
  
Step-2: Install Oh-my-zsh, the fun "configuration" framework
------------------------------------------------------------
Install directly from the source.

```shell-session
$ sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

In the last step of this installation, it will ask to set Zsh as THE shell. Go ahead.

Now we have the default prompt from `Oh-my-zsh`. 

![After successful installation of Oh-my-zsh](https://i.imgur.com/HOVqqvi.png)

Now, let's pimp up the prompt. Shall we?
  
  
Step-3: Install `powerlevel10k`, a powerful prompt theme
--------------------------------------------------------

I love the powerful Zsh theme `powerlevel10k`. More on [why this theme](https://github.com/romkatv/powerlevel10k#features) is awesome.

Let's install it on top of `oh-my-zsh`.

```shell-session
$ git clone --depth=1 \
  https://github.com/romkatv/powerlevel10k.git \
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

Now, gotta set `ZSH_THEME="powerlevel10k/powerlevel10k"` in `~/.zshrc` by adding that manually in the file.


  
Step-4: Make sure the prompt looks like as you want
---------------------------------------------------
In this step, I'm gonna bring in my already open-sourced Zsh config file aka `.zshrc`. 

```shell-session
# deleting the current one & get my personal one from GitHub
$ rm .zshrc
$
$ wget https://raw.githubusercontent.com/kmonsoor/dot-files/master/.zshrc
```

I kept the powerlevel10k configs as comments so that Zsh doesn't complain if I use the config file early.
Have to set `ZSH_THEME="powerlevel10k/powerlevel10k"` in the `~/.zshrc` as well.

Otherwise, once the `powerlevel10k` theme will run for the first time by Zsh, a very friendly step-by-step prompt will run you through towards a desirable prompt for you. Also, whenever you want, you can invoke the config-wizard by executing `p10k configure` on the shell.

Now is the time to enable the changes by restarting Zsh and enjoy the new config and the powerful prompt.

```shell-session
$ exec zsh
```


Optional
--------
Also, I usually install this very useful, but external plugin `zsh-syntax-highlighting` for oh-my-zsh.

```shell-session
$ git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```
Don't forget to activate the plugin by including it in ~/.zshrc. For that, add `zsh-syntax-highlighting` inside the list of other plugins.

plugins=( plugin_a plugin_b zsh-syntax-highlighting)

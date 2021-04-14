---
Title: How I Pimp up My Terminal
Date: 2020-12-31
Tags: computing, linux, terminal, CLI
Slug: pimp-up-my-terminal
Status: Draft
Summary: How do I pimp up my Linux terminal? A quick trip through Zsh, Oh-my-zsh, and other power tools to make the command-line based workflow smooth and cool.
---

Basically, purpose of this post is to be my quick, copy-paste source of the commands that I use to set up my terminal.
But, if someone else finds it useful, that'd be cherry on top.

Assuming I'm on a standard Linux machine with Ubuntu and I have CLI access. For other Linux distros or MacOS, some commands might be slightly different.

Confirm that Zsh is up-to-date
------------------------------
While on some Linux system, Zsh is present by default, on some it's not the case. 

`$ sudo apt install zsh`

Confirm the version. Oh-my-zsh requires it to be `5.0.2` or higher.

`$ zsh --version`
`zsh 5.8 (x86_64-ubuntu-linux-gnu)`

Install Oh-my-zsh, the fun framework
------------------------------
Directly from the source.

`$ sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`


as the last step of this installation, it will ask to set Zsh as THE shell. Go ahead.

Now we have the default prompt from Oh-my-zsh. 

[image]

Now, let's pimp up the prompt. Shall we?

Strong Zsh theme powerlevel10k. More about [why this theme](https://github.com/romkatv/powerlevel10k#features).

`$ git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k`

Now, gotta set ZSH_THEME="powerlevel10k/powerlevel10k" in ~/.zshrc.
In this step, I'm gonna bring in my already open-sourced Zsh config file.

`$ rm .zshrc`
`$ wget https://raw.githubusercontent.com/kmonsoor/dot-files/master/.zshrc`

I kept the powerlevel10k config in comment, so Zsh doen't complain if i use the config file early.

Set ZSH_THEME="powerlevel10k/powerlevel10k" in ~/.zshrc.

Time to enjoy the new config and the powerful prompt.
`$ source .zshrc`

Optional
--------
Intsall my favorite, external plugin `fast-syntax-highlighting` for oh-my-zsh.

```
$ git clone https://github.com/zdharma/fast-syntax-highlighting.git \
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting
```

Don't forget to enable the changes by resstarting Zsh.
`$ exec zsh`

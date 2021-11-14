---
Title: Ubuntu - Update APT-GET Server to Use Fastest Mirror
Date: 2016-10-10
Tags:  ubuntu, mirror, apt-get, update, upgrade, fastest, server, apt-select
Slug:  ubuntu-update-apt-get-server-to-use-fastest-mirror
Summary:  Updating Ubuntu from it's default server takes too damn long. Give it a 10x boost.
Version: 1.1.0
Status: Published
---

## Prelude
By default, Ubuntu sets the update server pointing to its own (http://archive.ubuntu.com). It is the safest bet for Ubuntu. But, that's not the case for users, especially who are outside USA. To make it smoother as well as distribute the load, Ubuntu also provides a list of mirror sites. You can find the official mirror list [here](https://launchpad.net/ubuntu/+archivemirrors). 

However, it needs some configuration.


## On GUI
Yes, you can do the selection on Ubuntu using its GUI tool. But, the problem is it don't always work as you want.

> It works on geolocation, giving me the local server, which is waaaayy slower where I am. The network temporal distance is the important factor here, not spatial distance (http://askubuntu.com/a/9035/113604)

![Ubuntu-select-update-server-GUI](http://i.imgur.com/sCWr0zrl.png)

## so, what else do we have ?

I use a handy tool for this purpose to point me to the fastest server FOR ME. It's [apt-select](https://github.com/jblakeman/apt-select).

To install it, i found this method most hassle-free. You may also try `pip install` method described on the repo's README file.

```shell-session
$ git clone https://github.com/jblakeman/apt-select.git
```

That's it. Now to execute it, just run the "main" Python file.

```{.shell-session hl_lines="2"}
$ cd apt-select
$ ./apt-select.py -c -t 3 -m one-week-behind
```

We are choosing here the best 3 mirrors(due to `-t 3`) which are at most `one week behind` from the main Ubuntu server. For general purposes, that's good enough.

It will choose one using the latency & ping time, and also show servers' bandwidth. Then the tool asks you to select new mirror from the `3` options came up. Usually, stick to the top option, hence `1`. 
For example in my case, it shows:

```{.shell-session hl_lines="1"}
[khaled:~] $ apt-select -c -t 3 -m one-week-behind
Getting list of mirrors...done.
Testing latency to mirror(s)
[3/3] 100%
Getting list of launchpad URLs...done.
Looking up 3 status(es)
[3/3] 100%
1. mirror.dhakacom.com (current)
    Latency: 1.89 ms
    Org:     dhakaCom Limited
    Status:  Up to date
    Speed:   1 Gbps
2. mirror.dhakacom.com
    Latency: 1.96 ms
    Org:     dhakaCom Limited
    Status:  Up to date
    Speed:   1 Gbps
3. archive.ubuntu.com
    Latency: 205.23 ms
    Org:     Canonical Ltd.
    Status:  Up to date
    Speed:   100 Mbps
Choose a mirror (1 - 3)
'q' to quit 1
New config file saved to /home/khaled/sources.list
```

Then, the tool prepares a new `sources.list` file to replace the system's one with.

Now, replace the file with the new one which will be now used by the `apt-get *` commands. As it overwrites a system config file, you need to do with `sudo`.

```shell-session
$ sudo mv /etc/apt/sources.list /etc/apt/sources.list.backup && sudo mv sources.list /etc/apt/
```

That's it. Now, all you update/upgrade will be fetched from the newly selected mirror.

However, I highly recommend to run `update` once right away.

```shell-session
$ sudo apt-get update
```

Then, only if you want, run `upgrade`:

```shell-session    
$ sudo apt-get upgrade
```

--------------------------
## You may also like
 * [Open Source as-if You Gonna Die Tonight](https://blog.kmonsoor.com/open-source-as-if-you-gonna-die-tonight/?utm_source=related_footer&utm_keyword=coding)
 * [Pelican Static sites - SEO Optimization](https://blog.kmonsoor.com/pelican-how-to-make-seo-friendly/?utm_source=related_footer&utm_keyword=python)
 * [Generate ER diagram from a SQL-based database](https://blog.kmonsoor.com/generate-er-diagram-from-sql-database/?utm_source=related_footer&utm_keyword=coding)

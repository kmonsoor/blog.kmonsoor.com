---
Title: Deploying a short-link aka go-link server using only Caddyserver
Slug: deploying-golink-server-using-Caddy
Status: Published
Date: 2021-04-16
Updated: 2021-11-11
Category: Tech
Tags: caddy, webserver, url-shortener, Caddyfile, web-link, go-link
Summary: Yeah, there are tons of open-source, full-fledged link-shorteners. But, none were exactly what I wanted. Hence, the minimal approach only by utilizing an amazing webserver, `Caddy`. Here we go ...
---

Before I go into any details, please note that I've used the term "shortlink-server" instead of "url-shortener" because the difference is significant for this post.
A url-shortener takes a long url, and gives a short url, then redirects any requests for the shortened link to its longer counterpart. On the contrary, shortlink-server takes both the long and short url as inputs, then only does the redirect-ion part.

Backstory
---------

If I wanted a fantastic, personal url-shortener or "go link" server, there are many excellent solutions out there, which are not only free or open-source but full-fledged as well for personal or public usage. Instead, I wanted some "service" that would "resolve" my personal, short links. I have been using bit.ly for a long time for its customizable "short-half" part, but the problem with bit.ly is -- for some God-forsaken reason -- blocked by the Bangladeshi govt. So, I needed a replacement to be appropriately "glocal".
There are many free (unbranded) and commercial (branded) options as well, but I wanted something that would be resolved via my hosted service (and personal domain) and as cheap as possible. So, basically solution for a poor nerd :D

Before jumped into this solution, I tried (deployed & tested) few others myself, mainly [kellegous/go](https://github.com/kellegous/go), [kutt.it](kutt.it) and [adamyi/golinks](https://github.com/adamyi/golinks). But, all of them "too featureful" for my needs.

![Simple, on-prem short-link server using Caddy webserver](https://i.imgur.com/4nZbnUE.png)

What I wanted is to be able to:

* resolve only my custom shortlinks (hence, no need for url-shortener)
* not a public, internet-facing service (hence, any frontend, authentication, email verification etc. would be overkill )
* minimal setup (if possible, no webapp at all)

Given my previous experience with `Caddy` webserver, which is an amazing one([why?](https://caddyserver.com/docs/)), I had a gut feeling that Caddy has something for me -- under the sleeve -- to meet my minimal set of requirements. Thankfully, I managed to find it.

I believe NGINX, currently the most popular webserver, has some kind of similar mechanism as well. But, I'm not an expert, and once I was genuinely intimidated by its config file syntax. YMMV.

What you gonna need?
--------------------

* your own domain which will be the root of the shortlinks. While sub-domained URL like `go.company-name.com/*` is quite common, if you have some short domain, like you.co/*, only for this purpose, that's fine as well.
* A web-host server or public-facing instance with its own, **public IPv4 address**.
* working knowledge of Linux

Step-1: Point your subdomain to the right place
-----------------------------------------------

* Find out what's the **puplic IPv4 address** of your instance that'll act as the webserver. It's usually on the cloud management dashboard.
* make sure that, regardless of your cloud architecture (e.g. VPC, subnet, firewall etc.), the SSL port (`:443`) of the instance is reachable from the public internet.
* now go to your domain name registrar (or, DNS management provider which in my case is Cloudflare). There, you need to point shortlink subdomain (`go.`)to the webserver's I.P. address. In DNS terms, you'll be creating a CNAME entry on the domain's nameserver table.

You can do this step as the last one. But for some reason, I prefer it to do first. Because sometimes, [DNS propagation](https://blog.cloudflare.com/never-deal-with-dns-propagation-again/) takes some time. But, once my web service is up and running, I like to see the result instantaneously. ;)

Step-2: Install Caddy, a mighty webserver
-------------------------------------------

Depending on your host OS (Ubuntu 20.04 LTS in my case), you need to [install the `Caddy` webserver](https://caddyserver.com/docs/install). While there are some hacky solutions to run, I think running `Caddy` as a background service is the simplest to manage.
In fact, the documentation of Caddy is excellent, so I'd better leave that part to you.

After running with the default config(`Caddyfile`), (in Ubuntu's case, located as `/etc/caddy/Caddyfile`), it should show a status somewhat like the below image. Please note that, in many cases, if running without `sudo`, Caddy cannot attach itself with the SSL port (`:443`), which is necessary for serving `https://`.  So, check for that error message in the "status" log.

![Caddy service on Ubuntu](https://i.imgur.com/cfS5nvZ.png?1)

_**PS:** By the way, want your console and command prompt to look 🚀 like mine? Here's the guide: [How do I pimp up my terminal on Linux](https://blog.kmonsoor.com/pimp-up-my-terminal/)_

Step-3: Tell Caddy your short-links to redirect
-----------------------------------------------

Now, it's time to configure Caddy to actually do the job.

Caddy has its native `redir` "directive" to redirect incoming web-request from one to another. While the `map` directive is relatively new, it makes the config file, i.e., Caddyfile, look elegant in case you have (or will have in the long run) a long list of short-links.

Here's mine, which is working nicely ...  

```
# /etc/caddy/Caddyfile

go.kmonsoor.com {   # replace it your web-url root

    map {path} {redirect-uri} {
        /blog    https://blog.kmonsoor.com
        /photos  https://photos.kmonsoor.com

        /resume     https://drive.google.com/file/d/1nMS3i1ai6nsI70zZ7NFnNQ_XmvAa4GOl
        /resume-doc https://docs.google.com/document/d/1ECx1Yr8Jzz9I3S5VcoKnZQz56oIht2XaM5gSNetcWag

        /rickrolled    https://www.youtube.com/watch?v=dQw4w9WgXcQ
        
        # will add new ones here like the above
        # ...
    }

    # this below code is required to actually make the above `map` work

    @hasRedir expression `{redirect-uri} != ""`
    redir @hasRedir {redirect-uri}

    # code below is to set the default response if the requested shortlink isn't here
    respond "Thas's an unknown short URL ... :("  
}
```

Note: Don't forget to restart the `caddy` service to let the new config to take effect.

Step-4: Profit
----------------

Yeah, that's it. Now, add some own personal stuff with some cool short-links, and proudly share with the world.

What's next ?
-------------

I'm thinking that given the very low workload my shortlink resolver needs — unless I'm becoming an overnight internet sensation — using a server instance only for this purpose is overkill. My next goal is to have the same service using some "serverless" function or using the "[worker on the edge](https://developers.cloudflare.com/workers/examples/redirect)" thing from Cloudflare. Let's see ;)

**Update** Now, actually done it. Here is the link: [Free short-link server "on edge" using Cloudflare Worker K.V.](https://blog.kmonsoor.com/golink-server-using-cloudflare-worker-kv/)

---
If you find this post helpful, you can show your support [through Patreon](https://www.patreon.com/kmonsoor) or [Paypal](https://paypal.me/KhaledMonsoor/) or by [buying me a coffee](https://ko-fi.com/kmonsoor). *Thanks!*
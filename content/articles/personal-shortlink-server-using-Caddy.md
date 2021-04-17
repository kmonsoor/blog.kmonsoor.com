---
Title: Personal short-link server using only Caddyserver
Date: 2021-04-16
Tags: caddyserver, url-shortener, Caddyfile, web-link
Slug: personal-shortlink-server-using-Caddy
Status: Published
Summary: Yeah, there are tons of open-source, full-fledged link-shorteners. But, none were exactly what I wanted. Hence, the minimal approach only ulitizing the amazing webserver, `Caddy`. Here, we go ...
---

Before I go into any details, please note that I've used the term "shortlink-server" instead of url-shortener because the difference is significant for this post. 
A url-shortener takes a long url, and gives a short url, then redirects any requests for the shortened link to its long counterpart. On the contrary, shortlink-server takes both the long and short url, then only do the redirect-ion part.

  
  
Backstory
---------
If I wanted an amazing, personal url-shortener or "go link" server, there are many amazing solutions out there, which are not only free or open-source, but full-fledged as well for personal or public usage. Rather, I wanted some "service" that will "resolve" my personal, short links. I have been using bit.ly for a long time for its customizable "short-half" part, but the problem with bit.ly is -- for some God forsaken reason -- blocked by the Bangladeshi govt. So, I needed a replacement to be properly "glocal".
There are many free (unbranded) and commercial (branded) option as well, but I wanted something that will be resolved via my hosted service (and personal domain) and as cheap as possible. So, basically solution for a poor nerd :D

Before jumped into this solution, I tried (deployed & tested) few others myself, mainly [kellegous/go](https://github.com/kellegous/go), [kutt.it](kutt.it) and [adamyi/golinks](https://github.com/adamyi/golinks). But, all of them too featureful for my needs. 


What I wanted is to be able to:

 * resolve only my custom shortlinks (hence, no need for url-shortener)
 * not a public, internet-facing service (hence, any frontend, authentication and email verification would be overkill )
 * minimal setup (if possible, no webapp at all)

Given my previous experience with `Caddy` webserver, which is an amazing one([why?](https://caddyserver.com/docs/)), I had a gut feeling that Caddy has something for me -- under the sleeve -- to meet my minimal set of requirements. Thankfully, I managed to find it.

I believe NGINX, currently the most popular webserver, has some kind of similar mechanism as well. But, I'm not an expert and once I was genuinely intimidated by its config file syntax. YMMV.

What you gonna need?
--------------------

 * your own domain which will be the root of the shortlinks. While sub-domained URL like `go.yourname.com/*`is quite common, if you have some short domain, like you.co/*, only for this purpose, that's fine as well.
 * A webhost server or public-facing instance with its own, **public** IPv4 address.
 * working knowledge of Linux


Step-1: Point your subdomain to the right place
-----------------------------------------------

 * Find out what's the **pulic IPv4 address** of your instance that'll act as the webserver. It's usually on the cloud management dashboard.
    * make sure that, regardless of your cloud architecture (e.g. VPC, subnet, firewall etc), the SSL port (`:443`) of the instance is reachable from the public internet.
 * now go to your domain name registrar (or, DNS management provider which in my case is Cloudflare). There, you need to point shortlink subdomain (`go.`)to the webserver's IP address.

Actually, you can do this step at the last. But for some reason, I prefer it to do it first. Because sometimes, [DNS propagation](https://blog.cloudflare.com/never-deal-with-dns-propagation-again/) takes some time. But, once my webservice is up and running, I like to see the result instaneously. ;)

Step-2: Install Caddy, the mighty webserver
-------------------------------------------
Depending on your host OS (mine is Ubuntu 20.04 LTS), you need to install the `Caddy` webserver. While there are some hacky solutions to run, I think running Caddy as a background server is the simplest to manage.
In fact, the documentation of Caddy is excellent, I'd better leave that part to you. 

After running with the default config(`Caddyfile`) which is in Ubuntu's case located as `/etc/caddy/Caddyfile`, it should have status somewhat like the below image. Please note that, in many cases, if running without `sudo` Caddy cannot attach itself with the SSL port (`:443`) which is neccessary for serving `https://`.  So, check for that error message in the "status" log.

![Caddy service on Ubuntu](https://i.imgur.com/cfS5nvZ.png?1)

***P.S.** By the way, want your console and command prompt to look 🚀 like mine? Here's the guide: [How do I pimp up my terminal on Linux](https://blog.kmonsoor.com/pimp-up-my-terminal/)*

Step-3: Tell Caddy your short-links to redirect
-----------------------------------------------
Now, it's time to configure Caddy to actually do the job.

Caddy has it's native `redir` "directive" to redirect incoming web-request from one to another. While the `map` directive is relatively new, it makes the config file i.e. Caddyfile look elegant in case you have (or, will have in the long run) long list of short-links.


Here's mine which is working ...  


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

Step-4: Profit !
----------------
Yeah, that's it. Now, add some own personal stuffs with some cool shortlinks, and proudly share with the world.


What's next ?
-------------
I'm thinking that given the very low workload my shortlink resolver needs, unless I'm becoming an overnight internet sensesation, using an instance for this purpose is an overkill. My next goal is to have the same service using some "serverless" function or using the "[worker on the edge](https://developers.cloudflare.com/workers/examples/redirect)" thing from Cloudflare. Let's see ;)

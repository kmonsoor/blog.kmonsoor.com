---
Title: Personal short-link server using only Caddyserver
Date: 2020-08-22
Tags: caddyserver, url-shortener, Caddyfile, web-link
Slug: personal-shortlink-server-using-only-Caddyserver
Status: Draft
Summary: Yeah, there are tons of open-source, full-fledged link-shorteners. But, none were exactly what I wanted. Hence, the minimal approach only ulitizing the amazing webserver, `Caddy`. Here, we go ...
---

Before I tell you anything at all, please note that I've used the term "shortlink-server" instead of url-shortener because the difference is significant; at least for this post.

Backstory
---------
If I wanted an amazing, personal url-shortener or "go link" server, there are many amazing solutions out there, which are not only free or open-source, but full-fledged as well for personal or public usage. Rather, I wanted some "service" that will resolve my personal, short links. I have been using bit.ly for a long time, but problem is it is -- for some God forsaken reason -- blocked by the Bangladeshi govt. So, I needed a replacement to "glocal".
There are many free (unbranded) and commercial (branded) option as well, but I wanted something that will be resolved via my hosted service and as cheap as possible. So, basically solution for a poor, nerd :D

Before jumped into this solution, I tried (deployed & tested) few others myself, mainly [kellegous/go](https://github.com/kellegous/go), [kutt.it](kutt.it) and [adamyi/golinks](https://github.com/adamyi/golinks). But, all of them too featureful for my needs. 

What I wanted is able to:
 * resolve only my custom shortlinks (hence, no need for url-shortener)
 * not a public, internet-facing service (hence, any frontend, authentication and email verification would be overkill )
 * minimal setup (if possible, no webapp at all)

Given my previous experience with `Caddy` webserver, which is an amazing one([why?](https://caddyserver.com/docs/)), I knew Caddy has something for me under the sleeve to meet my minimal set of requirements. Thankfully, I managed to find it.


What you gonna need?
--------------------
 * your own domain which will be the root of the shortlinks. While sub-domained URL like `go.yourname.com/*`is quite common, if you have some short domain, like you.co/*, only for this purpose, that's fine as well.
 * A webhost server or public-facing instance with its own, public IPv4 address.
 * working knowledge of Linux


Step-1: Point your subdomain to the right place
-----------------------------------------------

Step-2: Install Caddy, your mighty webserver
--------------------------------------------

Step-3: Tell Caddy your short-links to redirect
-----------------------------------------------


Here's mine which is working ...

```
go.kmonsoor.com {

    map {path} {redirect-uri} {
        /blog    https://blog.kmonsoor.com
        /photos  https://photos.kmonsoor.com

        /resume     https://drive.google.com/file/d/1nMS3i1ai6nsI70zZ7NFnNQ_XmvAa4GOl
        /resume-doc https://docs.google.com/document/d/1ECx1Yr8Jzz9I3S5VcoKnZQz56oIht2XaM5gSNetcWag

        /rickrolled    https://www.youtube.com/watch?v=dQw4w9WgXcQ
        
        # will add new ones here like the above
        # ...
    }

    @hasRedir expression `{redirect-uri} != ""`
    redir @hasRedir {redirect-uri}

    respond "Thas's a short URL that we don't know of ... :("  # default response if the requested shortlink isn't here
}
```

Step-4: Profit !
----------------


What's next ?
-------------
I'm thinking that given the very low workload my shortlink resolver needs, unless I'm becoming an overnight internet sensesation, using an instance for this purpose is an overkill. My next goal is to have the same service using some serverless "function" or using the "[worker on the edge](https://developers.cloudflare.com/workers/examples/redirect)" thing from Cloudflare. Let's see ;)
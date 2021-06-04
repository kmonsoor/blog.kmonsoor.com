---
Title: Creating a free short-link server "on edge" using Cloudflare KV with Worker
Date: 2021-05-25
Tags: cloud, computing, url-shortener, url-forwarder, Cloudflare, Cloudflare Worker, Cloudflare KV, Workers KV, on edge, free, go-link
Slug: on-edge-shortlink-server-cloudflare-kv-worker
Status: Published
Summary: Among quite a few ways to implement a url-forwarder, here I'm going to show you how to use free-tier Cloudflare Worker (& KV) to create an in-house, on-edge, no-webserver url-forwarder
---

Among quite a few ways to implement a url-forwarder, here I'm going to show you how to use free-tier Cloudflare Worker (& KV) to create an in-house, on-edge, **no-webserver** url-forwarder.

For example,

* `/latest` (by which I mean `go.yourdomain.co/latest`) may point to `https://www.yourcompany.com/about/news` which is a public page
* `/hr-help` may point to `https://www.company-internal.com/intranet/portal/docs/hr/contact.html` which is an internal human resources help portal
* `/cnypromo` may point to `https://shop.yourcompany.com/sales/promotions/?marketing-promo=2021-cny` which is a temporary sales promotions page targeting the shoppers during the Chinese new year of 2021.

Please note that using the setup & code below , it'll be possible resolve shortlinks via a single sub-domain, e.g. `go.your-domain.co/latest`, or `go.your-domain.co/cnypromo`, but it's totally possible (with changing the code) to resolve/re-direct via any number of domains (your own, of course) towards any other public or private URL, and all sorts of novelties. However, for brevity's sake, I'm going to discuss the first one, single sub-domain usecase.

To setup a short-URL resolver via proper KV+Worker combination, we'll go through these steps:

[TOC]

# Pre-requisites
 * The DNS resolver for the root domain (in the example below, `kmonsoor.com`) needs to be Cloudflare. Because the core of the solution, the "worker", runs on the nearest (from the user) edge of Cloudflare using a common KV (key-value) mapping.
 * Write permission to the DNS configuration as you'd need to create a new AAAA DNS record.
 * Some knowledge of Javascript(ES6), as we gonna write the worker in that language.


# Create the short-link map as a KV

We'll start the setup by creating the short-link map, the list between the short-link segments that you (or, someone in your org) define and the actual URLs they needed to point to.

Find the KV stuff in the `Workers` section. From the screenshot, please ignore the "Route" section for now.  

![Find the KV stuff in the Workers section](https://i.imgur.com/b2Rk45u.png)

  * you'd need to create a KV "Namespace". Name the namespace as you seem makes sense. I named it `REDIRECTS` (in all caps just as convention, not required). 
  * List the short-links & their respective target URLs. From the examples in the intro, the keys `latest`, `hr-help`, `cnypromo` etc. would be in as the "key", and the target full links as the respective "value".
  * Remember NOT to start the short part with '/'. In the code, it'll be taken care of.


![Create the short-link map as a KV](https://i.imgur.com/jkC8bSr.png)

Once you've listed all your desired (short-link, target-link) combinations, now we have a KV on CLoudflare. However, it's not referencable from your Worker code, not yet. Hence the next step.

# Mapping a KV to a Worker variable

Now, we gonna map the previously created KV to a variable that can be referenced from our Workeer code. Please note that though I used diffrent names, but it can be same as well. Also note that a single KV can be accessed by multiple workers, and vice versa, a single Worker can reference multiple KVs.

![Mapping a KV to a Worker variable](https://i.imgur.com/lb7G9si.png)


# Handling a route with webworker


![Handling a route with webworker](https://i.imgur.com/KohHRfR.png)


# Create the Worker

Now, we going to write Workercode that runs on V8-runtime on an nearest(from the requesting user) edge location of Cloudflare to complete its functionality and deliver it to the user. Tn this case, that would be to redirect user's requested address to the mapped one by you, in the KV namespace above.

![Creating a worker](https://i.imgur.com/eNfZNyN.png)

The code editor looks like this:  

![The code editor for Cloudflare worker](https://i.imgur.com/pb9AE9v.png)

If you rather prefer to copy-paste, please feel free to do it from the below GitHub Gist.

<div class="gist">
<script src="https://gist.github.com/kmonsoor/dc9f96660423c96471f8574ba018d867.js"></script>
</div>

Once done, it should look like ...
![created webworker](https://i.imgur.com/XSdKB56.png)

# Pointing a DNS record to the Worker

![Pointing a DNS record to it](https://i.imgur.com/62bk7pe.png)

Voila ! Now, test some of the short-urls that you've mapped via the KV. Enjoy !
Watch out for the target usage though [against the limit](https://developers.cloudflare.com/workers/platform/limits#worker-limits).  
I think you'll be fine ;)

# Next improvements

In future, I may work on a generic `Go/Link` type resolver as a browser extension. 

# Related
 * If you want to do this url-direction **on your own webserver, but only using webserver**, try this: [Personal short-link server using only Caddyserver](https://blog.kmonsoor.com/personal-shortlink-server-using-Caddy/)

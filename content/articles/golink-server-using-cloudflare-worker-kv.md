---
Title: Create a free go-link server "on edge" using Cloudflare Worker KV
Slug: golink-server-using-cloudflare-worker-kv
Status: Published
Date: 2021-06-06
Updated: 2021-11-11
Image: https://i.imgur.com/MjIS5gDl.png
Tags: cloud, computing, url-shortener, url-forwarder, Cloudflare, Cloudflare Worker, Cloudflare KV, Workers KV, on edge, free, go-link
Summary: Among quite a few ways to implement a go-link server (i.e., url-forwarder, short-url server, etc.), I will show how to use free-tier Cloudflare Worker (& KV) to create an in-house, on-edge, **no-webserver** go-link server.
Description: I'm going to show you how to use free-tier Cloudflare Worker (& KV) to create an in-house, on-edge, **no-webserver** go-link server (a.k.a short-url server).
---

Among quite a few ways to implement a go-link server (i.e., url-forwarder, short-url server, etc.), I'm going to show you how to use free-tier Cloudflare Worker (& KV) to create an in-house, on-edge, **no-webserver** go-link server.

For example, the short-link for this article is [go.kmonsoor.com/golink-kv](https://go.kmonsoor.com/golink-kv)  

![overall structure](https://i.imgur.com/MjIS5gD.png)

* `/latest` (by which I mean `go.yourdomain.co/latest`) may point to `https://www.yourcompany.com/about/news` which is a public page
* `/hr-help` may point to `https://www.company-internal.com/long-link/hr/contact.html`, which is company's internal human-resources help portal
* `/cnypromo` may point to `https://shop.yourcompany.com/sales/promotions/?marketing-promo=2021-cny` which is a temporary sales promotions page targeting the shoppers during the Chinese new year of 2021.

Please note that using the setup and the code below, it'll be possible to resolve short-links via a **single** sub-domain, e.g., `go.your-domain.co`. However, it's possible (with some modification of the code) to resolve/redirect via *any number of domains* (your own, of course) towards any other public or private URL, and all sorts of novelties. However, for brevity's sake, I will discuss the first one, a single sub-domain usecase.

To set up a go-link server or short-URL resolver via a proper KV+Worker combination, we'll go through these steps:

[TOC]

# Pre-requisites
 * The DNS resolver for the **root** domain (in the example below, *`kmonsoor.com`*) needs to be Cloudflare. Because the core of the solution, the "worker", runs on the nearest (from the user) edge of Cloudflare using a standard KV ("key, value") list.
 * Write permission to the DNS configuration as you'd need to add a new AAAA DNS record.
 * Some knowledge of Javascript(`ES6`), as we are going to write the "worker" in that language.


# Create the short-link map as a KV

We'll start the setup by creating the short-link map, the list between the short-link segments that you (or someone in your org) define, and the actual URLs they need to point to.

Find the KV stuff in the `Workers` section. From the screenshot, please ignore the "Route" section for now.  

![Find the KV stuff in the Workers section](https://i.imgur.com/b2Rk45u.png)

  * you'd need to create a Worker KV "Namespace". Name the namespace as you seem fit. I named it `REDIRECTS` (in all caps just as a convention, not required). 
  * List the short links & their respective target URLs. From the examples in the intro, the keys `latest`, `hr-help`, `cnypromo` etc. would be in as the "key", and the target full links as the respective "value".
  * Remember NOT to start the short part with '/'. It'll be taken care of in the code.


![Create the short-link map as a KV](https://i.imgur.com/jkC8bSr.png)

Once you've listed all your desired (short-link, target-link) combinations, now we have a KV on Cloudflare. However, it's not referencable from your Worker code, not yet. Hence the next step.

# Mapping a KV to a Worker variable

Now, we will map the previously created KV to a variable that can be referenced from our Worker code. Please note that though I used different names, it can be the same as well. Also, note that multiple Workers can access a single KV, and vice versa is also true; a single Worker can reference multiple KVs.

![Mapping a KV to a Worker variable](https://i.imgur.com/lb7G9si.png)


# Handling a route with webworker


![Handling a route with webworker](https://i.imgur.com/KohHRfR.png)


# Create the Worker

Now, we will write Worker-code that runs on `V8` runtime on the nearest (from the requesting user) "edge" location of Cloudflare, to execute the code and deliver the result(s) to the user. In this case, that would be to redirect user-requested address to the mapped one (by you, in the KV namespace above).

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
Finally, we need to point a DNS record that'll redirect all requests to your re-soutign sub-domain (e.g. `go.your-domain.com`) to the Cloudflare Worker that we just created.

According to the Cloudflare docs, the DNNS record must be an AAAA record, pointing to the IPv6 address `100::`. The "Name" here is the "sub-domain" part of your choice, which is better be short, to rightfully serve our goal here.  
  
![Pointing a DNS record to it](https://i.imgur.com/62bk7pe.png)

Voila ! Now, test some of the short-urls that you've mapped via the KV. Enjoy !
Watch out for the target usage though. [Here's the limit](https://developers.cloudflare.com/workers/platform/limits#worker-limits).  
  
I think you'll be fine, unless you're some celebrity ;)

# Next step

As the next step, I'm thinking to create a generic `Go/Link` resolver browser extension. Then, someone can set their own default domain or company domain of choice as short-domain host. In that case, entering just `go/hr-help` on the browser will take to `https://www.company-internal.com/.../hr/contact.html` that we have discussed at the beginning (remember the example case of an internal human resources help portal?).

# Related
If you want to do this url-direction **on your server, but only using webserver**, try this: [Personal short-link server using only Caddyserver](https://go.kmonsoor.com/golink-caddy)

---
If you find this post helpful, you can show your support [through Patreon](https://www.patreon.com/kmonsoor) or by [buying me a coffee](https://ko-fi.com/kmonsoor). *Thanks!*

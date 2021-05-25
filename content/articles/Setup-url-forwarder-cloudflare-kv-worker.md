---
Title: Creating a free short-link server "on edge" using Cloudflare KV with Worker
Date: 2021-05-25
Tags: cloud, computing, url-shortener, url-forwarder, Cloudflare, Cloudflare Worker, Cloudflare KV, Workers KV, on edge, free
Slug: on-edge-shortlink-server-cloudflare-kv-worker.md
Status: Draft
Summary: Among quite a few ways to implement a url-forwarder, here I'm going to show you how to use free-tier Cloudflare Worker (& KV) to create an in-house, on-edge, no-webserver url-forwarder
---

Among quite a few ways to implement a url-forwarder, here I'm going to show you how to use free-tier Cloudflare Worker (& KV) to create an in-house, on-edge, **no-webserver** url-forwarder.

Pre-requisites
==============
* The DNS resolver for the root domain needs to be Cloudflare. Because the core of the solution, the "worker" runs on the edge of Cloudserver using a common KV(key-value) mapping.
* Write access to the DNS configuration as you need to create a new AAAA DNS record.
* Some knowledge of Javascript, as we gonna write the worker in JS


Create the short-link map as a KV
---------------------------------

![Create the short-link map as a KV](https://i.imgur.com/jkC8bSr.png)


Mapping a KV to a Worker variable
---------------------------------
![Mapping a KV to a Worker variable](https://i.imgur.com/lb7G9si.png)

![created webworker](https://i.imgur.com/XSdKB56.png)


Handling a route with webworker
-------------------------------

![Handling a route with webworker](https://i.imgur.com/KohHRfR.png)


The webworker
-------------
Here comes the worker code that runs on V8-runtime on an nearest(from the requesting user) edge location of Cloudflare to complete the functionality and deliver it to the user. Tn this case, that would be to redirect user's requested address to the mapped one by you, in the KV above.

[The code editor for Cloudflare worker](https://i.imgur.com/pb9AE9v.png)

If you rather prefer to copy-paste, please feel free.

<script src="http://gist-it.appspot.com/https://gist.github.com/kmonsoor/dc9f96660423c96471f8574ba018d867#file-url-forwarder-worker-cloudflare-js"></script>


Pointing a DNS record to it
---------------------------

![Pointing a DNS record to it](https://i.imgur.com/62bk7pe.png)

Voila ! Now, test some of the short-urls that you've mapped via the KV. Enjoy !
Watch out for the target usage though [against the limit](https://developers.cloudflare.com/workers/platform/limits#worker-limits).  
I think you'll be fine ;)
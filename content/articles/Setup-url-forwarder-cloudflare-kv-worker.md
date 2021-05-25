---
Title: Creating a free short-link server "on edge" using Cloudflare KV with Worker
Date: 2021-05-25
Tags: cloud, computing, url-shortener, url-forwarder, Cloudflare, Cloudflare Worker, Cloudflare KV, Workers KV, on edge, free
Slug: on-edge-shortlink-server-cloudflare-kv-worker.md
Status: Draft
Summary: Among quite a few ways to implement a url-forwarder, here I'm going to show you how to use free-tier Cloudflare Worker (& KV) to create an in-house, on-edge, no-webserver url-forwarder
---

Among quite a few ways to implement a url-forwarder, here I'm going to show you how to use free-tier Cloudflare Worker (& KV) to create an in-house, on-edge, **no-webserver** url-forwarder.



Create the short-link map as a KV
---------------------------------
[Create the short-link map as a KV](https://i.imgur.com/jkC8bSr.png)


Mapping a KV to a Worker variable
---------------------------------
[Mapping a KV to a Worker variable](https://i.imgur.com/lb7G9si.png)

[created webworker](https://i.imgur.com/XSdKB56.png)


Handle a route with webworker
-----------------------------
[Handling a route with webworker](https://i.imgur.com/KohHRfR.png)


Pointing a DNS record to it
---------------------------
[Pointing a DNS record to it](https://i.imgur.com/62bk7pe.png)
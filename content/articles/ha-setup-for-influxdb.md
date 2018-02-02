---
Title: HA(High-Availablity) Setup for InfluxDB
Date: 2017-09-09
Tags: influxdb, influx-relay, haproxy, monitoring, computing, time-series, database, open-source, reliability 
Slug: the-great-title-slug
Status: Draft
Summary: Create a robust, highly-available, time-series database setup with open-source version of InfluxDB
---

HA setup for InfluxDB
=====================

Currently, from version 0.9, you cannot create InfluxDB cluster from the open-sourced free edition. Only commercially available InfluxDB Enterprise can do that for now. That stirred up the early-adopter enthusiast users, especially for their usage in professional setups. They complained that InfluxData, company behind InfluxDB, is trying to milk the OSS solution for profit.

I can't blame InfluxData guys much, as they gotta pay their bills too. So far, we the users of OSS systems couldn't show much promise about commercial realities of the projects. Bearing OSS future only depending on donations, patreons or enterprise sponsorship is far too rare and unpredictable, even for the projects that many successful organizations heavily rely on.

Anyways, InfluxDB then promised, and later introduced `Influx Relay` as a complimentary consolation for missing HA parts of InfluxDB. You can get the details here and here about that. 


## Premise

For my needs, I have to try to create a reliable HA(high-availablility) setup  from available free options, hence InfluxDB and the relay. It's definitely far from a InfluxDB-cluster in terms of robustness or ease of setup, but it's gets the job done, at least for me.

I needed a setup to receive system-stats from at least 500+ instances and to store them for a while; but without breaking the bank in bills from AWS. Meaning I could ask for and use only couple of instances for my solution.

Here were my trade-offs.
  *  Not too many instances for this purpose. Neither, any of the heavyweight lifters e.g. AWS' M3-xlarge etc. To use only what's necessary. 
  *  To satisfy the budget, hence avoiding pay-per-use solutions as far as it is possible.
  *  Solutions must not be crazy complex, so that handover to the devOps team be smooth.
  *  Reading the data would be too rarely w.r.t. writing. The related Grafana dashboards will be only used to investigate issues by a handful of people.
 

## Overall Design

### Write

From a birds' eye view, I decided to use two instances to run parallelly, hosting InfluxDB on them independently and then send exactly same data over to them for storing. This scheme mostly look like [RAID-1 systems](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_1).

That brings up couple of challenges.
* None of the agents I used on the sender side could multiplex output. Meaning they were able to send data to single destination, not multuple. 
	On the Windows front, I've used `Telegraf` which is able randomly switch between pre-listed destinations, but not multiple at-once. 
	In the case of Linux hosts, I used `Netdata` which is excellent on its own right, but unable to send stats to multiple destinations.
  Here comes `Influx-relay`. It can receive time-series data-stream from hosts on a TCP or UDP port, buffer for a while, and then re-send those received and buffered data to multiple receive ends which can either be an InfluxDB instance or another listening Influx-relay instances. This chaining can broaden the relaying scheme even further. However, for my purpose, this relay-chaining was not necessary. Rather, from relay, i am sending data to the separate InfluxDB instances, running on two separate instances.

* Now that I partially multiplexed the output, my hosts (senders) still are able to send to one destination. So, I need a proxy as well as a load-balancer. For a while, I was torn between NGINX and HAProxy. Both were new to  me.
  However, for couple of reasons, I went for HAProxy.  Firstly, I have no need for HTTP session management. Secondly, as I wanted to keep my UDP for later, HAProxy was perfectly capable for that. NGINX has the support recently, maturity was a concern. Also, configuring NGINX seems little intimating (which I know not so true). Last but not least, and for what its worth, out-of-the-box, HAProxy's stat page carries much more in-depth information than that of free-version of NGINX.
	Upon receiving the stats stream, HAProxy was supposed to send that to different Influx-relays in load-balanced fashion.
	So, here's my rough plan. 

collector-agent --> HAProxy --> (50/50 load-balanced) --> Influx-relay --> (multiplexed)  -->  2 InfluxDB instances

Now, each of the received data is to go to both the InfluxDB, or at least one in case of failure (or, overload) of any the relays or Influx instances.
Also, I have chosen to keep Influx-relays deployed as Dockerized, and kept HAProxy and InfluxDB instances running as native services. Of course, you can Dockerize HAProxy and InfluxDB, too.  

### Read

As I've already noted in the "" section that reading the data, meaning to fetch data to visualize on Grafana end, will happen rarely and sporadically; only to investigate alarms or any other client-side performance issues. So, the read requests, reaching HAProxy end, needed not much routing, other than directly to InfluxDB itself. Still, to better distribute the load I decided to load-balance it 50/50 basis.

### Ports

As all the READ requests are routed though HAProxy running on each of the instances, to the external world only HAProxy's port should be opened for this purpose. 
On the other hand, for WRITE requests, InfluxDBs  are receiving data from relays, one of its own instance and other one on other instance, so InfluxDB should listen on its own port for WRITE requests only. But, this must be accessible only from own VPS zone, but not open to the outside world.
In case of HAProxy as well as InfluxDB you can use the default ports, obviously, which is 8086 & 8088 respectively. Or, you can choose to go for other ports (security through obfuscation). Your call. In this writing, I'll go with the defaults.

### Authentication, SSL

You can configure SSL with your own server certificates through the HAProxy configs. You can even go for SSL from the relays to InfluxDB writes. If your sender hosts are connecting to your HAProxy through public internet, you should at least go for password-based authentication, better to utilize SSL. However, for brevity's sake, I'll skip them in this post.

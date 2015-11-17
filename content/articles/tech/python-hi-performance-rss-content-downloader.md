Title: Python fun #5 :  Hi-performance RSS Content Downloader
Date: 2014-04-15 19:45
Author: kmonsoor
Category: Coding, Python
Tags: content, downloader, feed, multiple, parallel, python, RSS
Slug: python-hi-performance-rss-content-downloader
Status: published

***[Disclaimer:*** In [Python](https://www.python.org/) world, I am just
a noobie. Sharing my experience along the way of learning. I am more
than happy to hear from you.]

I just [completed a content
downloader](https://gist.github.com/kmonsoor/10727871) which grabs links
from a given RSS feed, and then downloads all the linked contents
simultaneously. "Bandwidth is your only limit" ;)

It DON'T work on Windows. Yet.

<!--more-->

For the downloading part, it primarily depends on the
[URLGrabber](http://urlgrabber.baseurl.org) library which in turn depend
on [PycURL](http://pycurl.sourceforge.net/) library. On the other hand,
for parallelism and other staffs it depends on Python's built-in
libraries, e.g.
[Multiprocessing](https://docs.python.org/2/library/multiprocessing.html),
[XML
parsing](https://docs.python.org/2/library/xml.etree.elementtree.html‎),
[URLlib2](https://docs.python.org/2.7/library/urllib2.html‎).

You can even use proxy settings, bandwidth-control, FTP's user/password
etc.

Here it goes:

http://gist.github.com/kmonsoor/10727871

As, Wordpress.com don't allow GitHub code embedding, you have to click
the link to check this out.

Thanks !

 

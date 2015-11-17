Title: [UX] Should my blank query (on a site) return any result ?  [yet to complete]
Date: 2013-12-17 01:21
Author: kmonsoor
Category: idea, UX, web
Tags: natural, query, search, smartnesss, user-friendly, UX, web2
Slug: ux-what-should-blank-query-return
Status: published

While i was going through some site, i was looking for something. Okay,
i admit it was a job site.I wanted to begin from ALL results then filter
it down. So, I just hit "Search" without giving any query.

Should it return me with all or nothing?

I raised a question in [UX forum of
StackExchange](http://ux.stackexchange.com/questions/49080/what-should-be-fetched-if-someone-search-with-blank-queries)
(u know StackOverflow, right ?!) about that. What should be the smart
approach to the classic UX problem? What is the current trend? What it
should be ?

**My Question was:**

> Almost all site include a "Search" facility. It can be a job site,
> blog, photography-sale, or forum.
>
> usual format is like:
>
> ![mockup](http://i.stack.imgur.com/mnQOP.png)
>
> [download bmml
> source](http://ux.stackexchange.com/plugins/mockups/download?image=http%3a%2f%2fi.stack.imgur.com%2fmnQOP.png) –
> Wireframes created with [Balsamiq
> Mockups](http://www.balsamiq.com/products/mockups)
>
> **The Question is:**
>
> If user keep the input box empty, and hit ENTER (or click "Search"
> button), what should (s)he get ?
>
> What would be the ***smartest*** UX approach ?
>
> 1.  return **ALL** e.g. Google jobs site
> 2.  return **NOTHING**, and notify user to enter search term
> 3.  bring up the dedicated **search page** e.g. this site
> 4.  return the **HOT items** right now on the site
> 5.  return the **MOST\_SEARCHED** items, or
> 6.  return some **RANDOM items**
> 7.  does NOTHING
>
> Is there any ***standard***, ***de facto***, or research findings on
> this concern?

It started a lot of views (400 hits on first day) as well as answers,
comments opinion. I got the point that it rang some bell.

**I believe now that it's an classic question.**

i also did some fact-finding along the way. What is the approach of the
leading web sites around the globe ?

**Google / Bing**: "Google and Bing handle this and their flow is to
just ignore the search request if there is no search value entered and
keep the user in the same page." (Thanks, @Mervin on StackExchange)

**Amazon**: return back to homepage with an extra
"*/ref=nb\_sb\_noss\_null"* in the link

**Google Jobs**: returns ALL, sorted by "logging-location" and
reverse-chrono. Page navigation says "Page 1 of many"

**Chrome Web Store**: just does nothing on pressing ENTER

**Gmail**: It is quite interesting. While in inbox, pressing "search"
does nothing. But when user gives *blank*in advanced search, it (IMO,
rightfully returns **ALL Mails**) with a notif. as *"Invalid search
query - returning all mail."*

[![gmail blank query
message](http://i.stack.imgur.com/ZTTnx.png)](http://i.stack.imgur.com/ZTTnx.png)

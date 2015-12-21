Title: Pelican blog : Create a prefilled MarkDown(*.md) post
Date:  2015-12-21 0:44
Modified:  2015-12-21 0:44
Tags: pelican, blog, new post, pre-filled, automation
Slug: pelican-create-a-prefilled-markdown-post
status: published
Summary: While creating a blog post using Pelican, don't type the boring staff again and again ...

I use this Python script to jump-start a new post. Nothing fancy, but useful.  
Especially, if you are like me; hate to do same staff repeatedly.  
  
Clone this script in your blog's working folder on your pc. Once and forever.

```
$ git clone https://gist.github.com/942d661b4666ddce352f.git
```

Now, whenever you create a new post, run it like:

```
$ python2 ./pelican_new_MD_post_template.py 'your new blog post title'
```

Then, it will create a empty post in `./content/articles/` folder, by default.  
Now, edit that post and blog away.


Here's the script:

[gist:id=942d661b4666ddce352f]
  
  
Thanks for being here. Got any improvement suggestions? Plz let me know by comment on either here or on the Github gist.
Title: Open Source as-if You Gonna Die Tonight
Date: 2015-12-22
Modified: 2015-12-23
Tags: coding, open-source, OSS, death, bus-factor, truck-factor, source-control, software, personal, projects
Slug: open-source-as-if-you-gonna-die-tonight
status: published
Summary: You should open-source as-if you gonna die tonight. Literally.

***[ To keep the spirit of this post honest, I am going to publish this blog, immidiately. No __draft__-ing. This post will be, I hope, under continuous improvement.  
This post is [available for edit on GitHub](https://github.com/kmonsoor/blog.kmonsoor.com/edit/master/content/articles/tech/open-your-source-as-if-you-gonna-die-tonight.md), currently in its version 0.0.5 ]***



**Yes, I mean it. Literally.**

I see too many post/comments/blogs, in different meeting-places for techies e.g. hackernews, reddit, etc., which say the same thing: 

> "I am working on ***something*** which I will open-source/publish
> ***someday*** after taking it ***somewhere***."

See the ambiguous sense in the words?  

Unless the code/script/blog you are working on is something sensitive which will make a mess published a "draft" form, you should not wait for "someday". Or if you have thousands of subscribers to your blog ;)

Or if you decided that you will ***never*** publish it in public - that's an entirely different story.

If it is something of your company's code-base, commit it in your remote branch, so that your last 19 days of work isn't just gone just because you are "gone".

**As human, we are far more fragile than we think.**

I am not talking about publishing a physical book using a printing press. In that scenario, writers were supposed to write the perfect words, then type it using type-writer to avoid any handwriting-related gotchas. Then it went to the reviewer, then proofreader, then the typesetter makes a block character-by-character. Then comes printing on the paper. The writer had to be sure what he is writing about, ABSOLUTELY. Else, each of the *2000* copies of the *first-edition* would have the same mistakes.

I am also not talking about pushing the critical code in the `production` server. That stuff should go through rigorous coding practices, code-reviews, testing etc.


Aside from those cases, **this is 2015** - How much does each `git push origin gh-pages` cost? How much each WordPress post update cost? Or, a single GitHub gist?

Publishing your stuff is free, no matter how many times you update it.

**So, why do we think about the paradigm of the printing press when we think of "publishing"?**



Frequently shared confusions (FSQ)
------------------------------------
 * **What if this, my thing, is just plain crap ?**  
 **A.** Are you sure? You never know for sure. Throw it in the wild. If it is really crap, nobody will remember or hold you responsible for it. How many crappy DaVinci paintings you know? I guess, ***none.*** But the [Mona Lisa](https://en.wikipedia.org/wiki/Mona_Lisa) didn't just appear from thin air. Did it?
   
 *  **This is my toy(or pet) project.**  
 **A.** Don't be that selfish kid from the school who don't let others touch it just because. If you are having fun building something why not let others join in the fun?
   
 * **This is a one-off script on this ancient *COBOL* platform, no one is going to need it. Ever.**  
 **A.** You never know. You are a human. You can't imagine what people gonna need. Throw it in a [gist](https://gist.github.com/), just include a suitable title. Add in some comments if you please. May be couple of years later, your script will save someone's job, and he can still put food on the table. You never know.  
   
 * **If I publish this now some genius with free time will steal my idea and make it something grand without me.**  
 **A.** Unless you are a big hot-shot with a ground-breaking idea, no one will even notice it. Most _genius'_ mind is already filled with their own to-do list. Even if they take your idea, let them. Move on. 
 Don't be a muddy pond, rather be like a river. Rivers don't dry off due to peasants "stealing" some water.  
   
 * **I haven't collected my thoughts enough to make this post a grand one yet.**  
 **A.** Don't think too high yourself. Let others do that for you.  
 No project is born grand, and no great man born great. Your contributions is what goes ahead. You the person? Not so much. Time passed along "Romeo & Juliet", but Shakespeare is dead and gone.  
 
 * **I am special. My words/code should be special, perfect, coherent like a pearl-necklace.**  _(yes, we all feel like that, we just don't acknowledge it publicly.)_  
 **A.** No, you are not. You are not a special unique snowflake. See the previous answer.
 
 * **Who the \*\*\*k are you to tell me what to do?**  
 **A.** It's not about me, I am nobody. Just a open-source enthusiast who wants to see more and more open-source projects, scripts, blog-posts which haven't gone to grave with their mortal creators. I'm just sharing my own thoughts about it.
 **It is your code on your own personal-pc, after all.**
  
  
Why should I open my source(post/thoughts/etc) tonight?
--------------------
 * You can literally die tonight. 
 Then all of your pet-projects are just gone. 'Cause probably none in your family is in coding business or they aren't sure about your intention. 
  
 * Tomorrow morning, your mind will just drift-away.  
 What is a vivid idea tonight that could impact thousands of people's lives, tomorrow morning will become a faded, will-do-it-someday idea. One month after tonight, you probably will probably be oblivious about your own idea, draft, script, code.

 * It's a mind-trick to force ourselves to work on something to avoid public shame. We feel obliged to correct errata that is in public, but something hidden away in a private, hidden, local folder we don't have to feel bad about. 
  
  
  
To avoid embarrassment
----------------------------
 * Make sure your audience (or colleagues for that matter) know the content's status. Put a "prelude" section mentioning the half-done condition. Better yet, use some [version number](http://semver.org/).
  
 * Make your genereal idea clear. For code, point out what it is and what it is supposed to do. For a blog, present the basic idea at least, even if it is not with perfect grammer.
  
  
How infrastructure can improve
--------------------
Open-source mainstream hosting platforms e.g. Github, Bitbucket, GitLab etc. could have a **"Open the source"** trigger-switch for individual projects where a software developer can enable the trigger with some condition like:

  * "**Open the source**" if I don't login GitHub for `1 year` (which means I am dead or I've gone crazy trying to remember GitHub)
  * "**Open the source**" on a pre-set date e.g. `2020-02-20`
  
  
  
_[dear reader, thanks a lot for reading up to here. I am sure there are many points missing on this post. Also, as English is not my first language, hence there must some misused words or phrase. But you get the idea. Please comment/criticise/point out the missing stuff. I will try to discuss, update, correct that.]_

---------------------------------------


## Contributors

|                                               	|                          	|
|-----------------------------------------------	|--------------------------	|
| [Khaled Monsoor](https://github.com/kmonsoor) 	| initial author, maintainer           	|
| [Wayne Werner](https://github.com/waynew)     	| editor (v.0.0.3 --> v.0.0.4) 	|

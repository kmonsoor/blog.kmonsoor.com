Title: Se7en Deadly Sins to Do in Python code
Date: 2015-08-10 17:05
Modified: 2015-11-21 00:05
Tags: best practices, code quality, debugging, programming, python, software development, software documentation, worst practices
Slug: seven-deadly-sins-in-python-code
Status: published
Summary: There are a lot of ways someone can make his (or her) Python code extremely difficult for himself and his fellow developers to work with and maintain. However, some are quite destructive by virtue. These ones are in my top-list.


### Prelude

I have used the word "deadly" to express the potential to diminish the productivity of a Python programmer or his fellow teammate(s) who will work on the same code. Please take all these with quite a bit of salt, due to my limited expertise & limited experience with different types of projects based on Python.*

*7* is just a catchy number. And, of course, this top list is subject to change along with my experience.  
You are also most welcome to suggest your own-finding to make into this list.
  
  
  
There are a lot of ways someone can make his (or her) Python code extremely difficult for himself and his fellow developers to work with and maintain. However, some are quite destructive by virtue. These ones are in my top-list.

### **1. The `try: except: pass` trio**

You know about design patterns, right ? At least, you know a little bit.  
  
From [Wikipedia](https://en.wikipedia.org/wiki/Software_design_pattern),

> Design patterns can speed up the development process by providing tested, proven development paradigms. 
  
> Effective software design requires considering issues that may not become visible until later in the implementation. Reusing design patterns helps to prevent subtle issues that can cause major problems, and it also improves code readability for coders and architects who are familiar with the patterns.

  
Now, think of the complete opposite of design-pattern. It is called *anti-pattern* which silently "destroys" efficiency in code. The below pattern can be considered the most deadly anti-pattern in Python code.  
[Aaron Maxwell](http://redsymbol.net/) called it [most diabolical](https://realpython.com/blog/python/the-most-diabolical-python-antipattern/) or "evil" anti-pattern.

```python
try:
    subtle_buggy_operation()   # possibly with I/O or DB operation
except:
    pass
```
  
  
You thought to save some development time by "pass"ing them by. But, it will take hours, if not days, to find possible bugs, inside the block, later as all the exceptions are masked by the "pass" and the error location will be somewhere else outside this `try:except` block which may look like the most innocent code.

Again, quoting from Aaron ...

> In my nearly ten years of experience writing applications in Python, both individually and as part of a team, this pattern has stood out as the single greatest drain on developer productivity and application reliability, especially over the long term.
  
  
  
### **2. Wildcard imports i.e. `from module import *` **
  
This one single practice can render a nice (clean) module into a nightmare. According to a core Python developer [David Goodger](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#importing),
  
>  Wild-card imports are from the dark side of Python.
>  
>  **Never!**
>  
>  The `from module import *` wild-card style leads to namespace pollution. You'll get things in your local namespace that you didn't expect to get. You may see imported names obscuring module-defined local names. You won't be able to figure out where certain names come from. Although a convenient shortcut, this should not be in production code.
>
>  **Moral:** don't use wild-card imports!

Also, in light of [Yoda's mythical conversation](http://www.yodaquotes.net/)s, David writes:

> LUKE: Is from module import * better than explicit imports?  
> YODA: No, not better. Quicker, easier, more seductive.  
> LUKE: But how will I know why explicit imports are better than the wild-card form?  
> YODA: Know you will when your code you try to read six months from now.  

If you use this practice in between inter-connected modules in a mid-sized project, worry not. You'll start to get errors due to circular references soon enough.

Sounds funny ?
  
  
  
### **3. Thinking that `try:except:else` construct is not a natural control flow in Python**

If you are coming from Java(or, similar) world, I understand your confusion. However, Python adopted this construct so much different than Java. It helps to realize Python's philosophy [Ask for Forgiveness than Permission](https://docs.python.org/2/glossary.html#term-eafp), aka "EAFP paradigm".

Trying to avoid this will result in messy, unpythonic code. As this [great answer on StackOverflow](http://stackoverflow.com/a/16138864/617185), by a core Python developer, Raymond Hettinger, on this matter where he nicely portrays the philosophy behind it.

Quoting him :

> In the Python world, using exceptions for flow control is common and normal. Even the Python core developers use exceptions for flow-control and that style is heavily baked into the language (i.e. the iterator protocol uses *StopIteration* to signal loop termination). In addition, the try-except-style is used to prevent the race-conditions inherent in some of the "look-before-you-leap" constructs.  

> For example, testing `os.path.exists` results in information that may be out-of-date by the time you use it. Likewise, `Queue.full` returns information that may be stale. The `try:except:else` style will produce more reliable code in these cases. In some other languages, that rule reflects their cultural norms as reflected in their libraries. The "rule" is also based in-part on performance considerations for those languages.

Also, consider checking out [this Q&A on StackOverflow](http://stackoverflow.com/a/180974/617185) on the same premise.
  
  
  
### **4. Making everything a Class aka Overusing classes**

What I am referring to is [this talk by Jack Diederich](https://www.youtube.com/watch?v=o9pEzgHorH0) on PyCon 2012. You should watch this couple of times and then once in every week.  
His summary is like ... **Stop** creating classes, and modules in every now and then. Before creating one, think hard. Probably, what you need is writing just a function.

[Zen of Python](https://www.python.org/dev/peps/pep-0020/) described it as below.
Read it again, again, and again.

> * Beautiful is better than ugly.
> * Explicit is better than implicit.
> * Simple is better than complex.
> * Flat is better than nested.
> * Readability counts.
> * If the implementation is hard to explain, it's a bad idea.

Though the below is a perfectly valid class, it is a perfect example case of b\*\*\*sh\*t classes:

```python
class Greeting(object):
    def __init__(self, greeting='hello'):
        self.greeting = greeting

    def greet(self, name):
        return '%s! %s' % (self.greeting, name)

greeting = Greeting('hola')
print greeting.greet('bob')
```
  
It is doing exactly same as:

```python
def greet(greeting, target):
    return '%s! %s' % (greeting, target)
```

He also showed a practical example how he simplified (aka re-factored) an API's complete code, consisting:

 *  1 Package, 22 Modules,
 *  20 Classes,
 *  660 Source Lines of Code

into this below, a grand total of 8 lines. Yes, just 8 lines !!!

```python
MUFFIN_API = url='https://api.wbsrvc.com/%s/%s/'
MUFFIN_API_KEY = 'SECRET-API-KEY'

def request(noun, verb, **params):
    headers = {'apikey' : MUFFIN_API_KEY}
    request = urllib2.Request(MUFFIN_API % (noun, verb), \
                              urllib.urlencode(params), headers)
    return json.loads(urllib2.urlopen(request).read())
```

**Moral:**
  
 * Stop re-inventing the wheel, 
 * use more of built-in library functions, 
 * use much-less own long chains of class-hierarchy. 
  
Still want to see a worst scenario of creating classes? Check this out:
  
```python
class Flow(object):
    """Base class for all Flow objects."""
    pass

class Storage(object):
    def put(self, data): _abstract()
    def get(self): _abstract()

def _abstract(): raise NotImplementedError
```

Yes, this is a real piece of code from Google API client code. (which, in total, has *10,000 SLOC, 115 modules, 207 classes*). Whereas [someone did implemented the same](https://github.com/jackdied/python-foauth2), well maybe not extremely robust, but in *135 SLOC, 3 classes* in total.

You see the point, right? Guido did. [Check his comment.](https://plus.google.com/+JackDiederich/posts/iPiqWHjwcf3)

![guido-google-comment]({filename}/images/articles/guido-google-comment.jpg)
  
  
  
### **5. Saving time by not writing any documentation or inline comments**

If you don't write comments with your semi-obfuscated code, and no docstrings as well saving time and meeting deadlines, stay assure that within a short period you'll hate yourself when you will not remember what (& why) you did something while reading your own code.

Today or tomorrow, you will leave the company. And, that code will haunt all the members of your team who will come across this code-like zombies; unless they totally cut-off-the-head(e.g. replace) of your code. 
  
There is just no excuse that you don't do "documentation" except you just don't care. If you would care, you would not only write minimal doc-strings and comments on complex code-sections, but also name your functions, methods, variables to reflect the purpose of the component to make them "self-documented".

Here is a nice guide to properly [documenting your Python code.](http://docs.python-guide.org/en/latest/writing/documentation/)

However, there will still be deniers out there ...

![code-quality](https://googledrive.com/host/0B_IybRcQsDwaTGduUi1jR3h6aDQ/blog/code_quality.png)
                * source: https://xkcd.com/1513/ *
  
  
  
### **6. Avoiding Unit-tests (and doc-tests) until the doomsday comes**
  
Yes, the judgement day will come.  
It will happen on the production server, with customer's downtime due to a "completely" manually-tested new feature, which will break something "almost" unrelated.

Yes, your company can lose millions and [can be out of business.](http://dougseven.com/2014/04/17/knightmare-a-devops-cautionary-tale/) Maybe after some sleep-less night of the development team, the "bug" would have found out.

Maybe, this whole mess could be simply avoided if the developer wrote his/her modules' [unit-test](https://docs.python.org/2/library/unittest.html) as well as [doctests](https://docs.python.org/2/library/doctest.html) for the functions or methods. And, after implementing the feature he would have run the tests once across the project. The online book Dive-in-Python has an excellent introduction on `unittest`. Also, you can start with [Hitchhiker's guide's introduction](http://docs.python-guide.org/en/latest/writing/tests/#unittest).
  
  
  
### **7. Mixing `TAB` and `SPACE` in the same file**

You will need no more reason to curse yourself just a while after. It will haunt you whenever you'll need to open the source-code in any editor other than your usual one. And, for others, "oh my! I can't literally even...".

While Python**3** will simply refuse to interpret this "half-breed" file, in Python**2**, the interpretation of TAB is as if it is converted to spaces using 8-space tab stops. So while executing, you may have no clue how a specific-line is being executed as part of which code-block.

For any code that you think someday someone else will read or use, to avoid confusion, you should stick with [PEP-8](http://legacy.python.org/dev/peps/pep-0008/#tabs-or-spaces), or your team-specific coding style. PEP-8 strongly discourage mixing TAB and Space in a same file.

Also, check out this [Q&A on StackExchange.](http://programmers.stackexchange.com/a/197839/74557)

> ​1. The first downside is that it quickly becomes a mess.
   
> ... Formatting should be the task of the IDE. Developers have already enough work to care about the size of tabs, how much spaces will an IDE insert, etc. The code should be formatted correctly, and displayed correctly on other configurations, without forcing developers to think about it.  


Also, [remember this](http://www.secnetix.de/olli/Python/block_indentation.hawk)

> Furthermore, it can be a good idea to avoid tabs altogether, because the semantics of tabs are not very well-defined in the computer world, and they can be displayed completely differently on different types of systems and editors.   
Also, tabs often get destroyed or wrongly converted during *copy-paste* operations, or when a piece of source code is inserted into a web page or other kind of markup code.
  
  
  

### **Fin**

That's all for now. That's my list. This list hopes to evolve with my experience and expertise as well as the ever-changing collective wisdom of all the Python community.
  
What's your take on the worst "un-pythonic" nightmares in Python code?  Please feel free to share your 2-cents.

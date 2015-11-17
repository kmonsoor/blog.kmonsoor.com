Title: Python: Some Performance Scores
Date: 2014-01-27 15:20
Author: kmonsoor
Category: Coding, Python, software
Tags: coding, improvement, micro-optimization, performance, python, tips, tricks, tweak
Slug: python-some-performance-scores
Status: published

I just finished reading [Sebastian Raschka's analytic discussion of
Pyhton
tweaks](http://sebastianraschka.com/Articles/2014_python_performance_tweaks.html "Sebastian Raschka's analytic discussion of Pyhton tweaks") where
the author tested with Python version: ***3.3.3***

Now, as I am a huge "fan" of Pythonic 1-liners, I made a summary of the
article containing 1-liner-analysis-result.

**Adding elements to dictionaries**  
Adding keys "By exploiting thrown KeyError exceptions via an try-except
loop" is slightly(\~1.2x) faster than "(first,) checking if a key
already exists in the Python dictionary using if-else loop"

<!--more-->

**Filtering lists via (simple) conditional statements**  
List comprehension is \~1.5x faster than typical if-else loop, and
\~1.8x faster than "list(filter(lambda..." combination.

**Creating lists using function calls**  
Using built-in map() method is \~3.4x faster than the for-loop, and \~
1.5x faster than list comprehension approach.

> "So the bottom line of this analysis is that list comprehensions are
> ideal to create lists using simple evaluations via if-statements, and
> the in-built map() is the way to go for creating lists via function
> calls."

**Concatenating strings**

> "The .join() method is \~ 23x faster than the usage of the + operator
> to concatenate strings!"

**Assembling strings**  
Using the + operator to format(& concate) strings performs similar as
'%' string formatting operator.

However, the format() function is, relatively, extremely slower (\~10x).

Thanks for reading. For further digging, you can also find all the
details from the author in this Github repository:
<https://github.com/rasbt/python_efficiency_tweaks>

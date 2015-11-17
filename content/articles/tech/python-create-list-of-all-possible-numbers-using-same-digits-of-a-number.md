Title: Python fun #4:  Create sorted list of all possible numbers using same digits (of a number)
Date: 2014-01-31 15:00
Author: kmonsoor
Category: Coding, Python
Tags: coding, combination, fun, itertools, list, permutation, python, tuple
Slug: python-create-list-of-all-possible-numbers-using-same-digits-of-a-number
Status: published

Let's say the number is 123.

Then the statement:  
[code language="python"]  
[int(''.join(x)) for x in permutations(list(str(123)))]  
[/code]  
will create a sorted list of all possible numbers using '1','2' and
'3'.  
which is, [123, 132, 213, 231, 312, 321]

### What it is doing

The part, **permutations(list(str('123'** is creating a permutated tuple
list of splitted string '123'.  
And the **int(''.join(x))** is converting each tuple to back to
Integer.

However, you need to  
[code language="python"]  
import permutations from itertools  
[/code]

so, the generalized version would be:  
[code language="python"]  
import permutations from itertools  
[int(''.join(x)) for x in list(permutations(list(str(n))))]  
[/code]

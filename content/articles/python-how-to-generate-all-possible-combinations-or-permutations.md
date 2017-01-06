---
Title: Python - How to Create All Possible Combinations (a.k.a Permutations)
Date: 2014-01-31
Updated: 2016-12-22
Tags: python, coding, syntax, combination
Status: published
Slug: python-how-to-generate-all-possible-combinations-or-permutations
Version: 1.1.1
Summary: Let's say we have a string, or number. And, we want to generate all the combinations of all the characters of the string or the number
---

Let's say the number is 123.

Then the statement:
```python
[int(''.join(x)) for x in permutations(list(str(123)))]
```
will create a sorted list of all possible numbers using '1','2' and '3'.
which is, [123, 132, 213, 231, 312, 321]

### What it is doing
The part, `permutations(list(str('123'` is creating a [permutated](https://en.wikipedia.org/wiki/Permutation) [tuples'](https://en.wikipedia.org/wiki/Tuple) list of splitted string '123'.
And the `int(''.join(x))` is converting each tuple to Integer.

However, of course, you need to `import permutations from itertools`.

so, the generalized version would be:

```python
from itertools import permutations
[int(''.join(x)) for x in list(permutations(list(str(n))))]
```

Python is fun. Isn't it?

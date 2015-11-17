Title: Python fun #2 :  Input directly from a text file to a List (in 1 statement)
Date: 2014-01-04 23:56
Author: kmonsoor
Category: Coding, Python
Tags: coding, file, fun, list, programming, python, tips, tricks, tuple
Slug: python-fun-2-input-directly-from-a-text-file-to-a-list
Status: published

Assuming the text file(names.txt) has the data as strings separated by
comma

> L = list(eval(open('names.txt').readlines()[0]))

**what it is doing?**

It is inputting the whole file as a single string. It outputs a
[**Tuple**](http://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences).

The [list()](http://www.tutorialspoint.com/python/list_list.htm) method
converting that into a nice
[**List**](http://docs.python.org/2/tutorial/datastructures.html).

You can use it by changing slightly according to your input file format.

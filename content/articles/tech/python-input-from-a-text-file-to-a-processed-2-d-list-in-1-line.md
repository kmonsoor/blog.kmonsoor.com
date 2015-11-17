Title: Python fun #3 : Directly Input from a text file to a processed 2-D list (in 1 statement)
Date: 2014-01-18 21:50
Author: kmonsoor
Category: Coding, Python
Tags: 2d, fun, interesting, list, one-liner, python, smart, stackoverflow, table, text-input
Slug: python-input-from-a-text-file-to-a-processed-2-d-list-in-1-line
Status: published

Suppose you have input file like
this([triangle.txt](https://projecteuler.net/project/triangle.txt)) to
use as input ...

[code language="python"]  
with open('triangle.txt') as f:  
D = [[int(w) for w in line.split()] for line in f]  
[/code]

This will create a nice table-like 2-D list, i.e. a list of lists. The
member list(s) can be of variable size. You can modify the* int(w) for w
in line.split()* part to incorporate your processing.

<!--more-->

### History

For solving this [problem](http://projecteuler.net/problem=67), I was
using this below code segment; so, i raised a [question on
StackOverflow](http://stackoverflow.com/q/21184445/617185) requesting a
smart one-liner. That's how, I got the above 1-liner Python code.

My dumb code(yet, right) was:  
[code language="python"]  
f=open("triangle.txt")  
A=[]  
for i in range(100):  
A.append((f.readline()).strip())

// processing  
D=[]  
for i in range(100):  
D.append((A[i]).split())  
for i in range(100):  
for j in range(len(D[i])):  
D[i][j]= int(D[i][j])  
[/code]

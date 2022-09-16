#coding:utf-8
"""
 Write a Python program to create a new deque with three items and iterate over the deque's elements. Go to the editor
Sample Output:
a
e
i
o
u"""
from collections import deque
dq=deque('aeiou')
print(dq)
for i in dq:
    print(i)
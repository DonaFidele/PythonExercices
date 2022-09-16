#coding:utf-8
"""Write a Python program to add more number of elements to a deque object from an iterable object. Go to the editor
Sample Output:
Even numbers:
deque([2, 4, 6, 8, 10])
More even numbers:
deque([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])"""
from collections import deque
tpl=(1,2,3)
dq=deque(tpl)
print(dq)
dq.extend((5,6,4,8,7))
print(dq)
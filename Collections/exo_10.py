#coding:utf-8
"""Write a Python program to remove all the elements of a given deque object. Go to the editor
Sample Output:
Original Deque object with odd numbers:
deque([1, 3, 5, 7, 9])
Deque length: 5
Deque object after removing all numbers- deque([])
Deque length:0"""
from collections import deque
tpl=(1,2,3)
dq=deque(tpl)
print(dq)
dq.clear()
print(dq,len(dq))
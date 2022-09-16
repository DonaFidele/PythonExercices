#coding:utf-8
"""
Write a Python program to create a deque from an existing iterable object. Go to the editor
Sample Output:
Original tuple:
(2, 4, 6)
<class 'tuple'>
Original deque:
deque([2, 4, 6])
New deque from an existing iterable object:
deque([2, 2, 4, 6, 8, 10, 12])
<class 'collections.deque'>"""
from collections import deque
tpl=(2, 4, 6)
dq=deque(tpl)
print(dq)
dq.appendleft(2)
dq.append(8)
dq.append(10)
dq.append(12)
print(dq)
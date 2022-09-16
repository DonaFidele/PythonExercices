#coding:utf-8
"""Write a Python program to create a deque and append few elements to the left and right, then remove some elements from the left, right sides and reverse the deque. Go to the editor
Sample Output:
deque(['Red', 'Green', 'White'])
Adding to the left:
deque(['Pink', 'Red', 'Green', 'White'])
Adding to the right:
deque(['Pink', 'Red', 'Green', 'White', 'Orange'])
Removing from the right:
deque(['Pink', 'Red', 'Green', 'White'])
Removing from the left:
deque(['Red', 'Green', 'White'])
Reversing the deque:
deque(['White', 'Green', 'Red'])"""
from collections import deque
dq=deque(['Red', 'Green', 'White'])
print(dq)
dq.appendleft("Pink")
print(dq)
dq.append("Pink")
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)
dq.reverse()
print(dq)

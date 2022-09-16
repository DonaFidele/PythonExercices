#coding:utf-8
"""  Write a Python program to rotate a Deque Object specified number (negative) of times. Go to the editor
Sample Output:
Deque before rotation:
deque([2, 4, 6, 8, 10])
Deque after 1 negative rotation:
deque([4, 6, 8, 10, 2])
Deque after 2 negative rotations:
deque([8, 10, 2, 4, 6])"""
from collections import deque
nums = (2, 4, 6, 8, 10)
dq=deque(nums)
print(dq)
dq.rotate(-1)
print(dq)
dq.rotate(-2)
print(dq)
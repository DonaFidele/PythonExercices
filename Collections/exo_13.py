#coding:utf-8
""" Write a Python program to rotate a Deque Object specified number (positive) of times. Go to the editor
Sample Output:
Deque before rotation:
deque([2, 4, 6, 8, 10])
Deque after 1 positive rotation:
deque([10, 2, 4, 6, 8])
Deque after 2 positive rotations:
deque([6, 8, 10, 2, 4])"""
from collections import deque
nums = (2, 4, 6, 8, 10)
dq=deque(nums)
print(dq)
dq.rotate()
print(dq)
dq.rotate(2)
print(dq)
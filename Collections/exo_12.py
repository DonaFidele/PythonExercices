#coding:utf-8
""" Write a Python program to count the number of times a specific element presents in a deque object. Go to the editor
Sample Output:
Number of 2 in the sequence
5
Number of 4 in the sequence
4"""
from collections import deque
nums = (2,9,0,8,2,4,0,9,2,4,8,2,0,4,2,3,4,0)
dq=deque(nums)
print(dq.count(2))
print(dq.count(4))
#coding:utf-8
"""Write a Python program to find the most common element of a given list. Go to the editor
Sample Output:
Original list:
['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python']
Most common element of the said list:
Python"""
from collections import deque,Counter
Original_list=['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python']
print(max(Counter(Original_list)))
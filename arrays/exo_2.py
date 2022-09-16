#coding:utf-8
"""Write a Python program to append a new item to the end of the array. Go to the editor
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Append 11 at the end of the array:
New array: array('i', [1, 3, 5, 7, 9, 11])"""
from array import *
a=array('i',[1,2,3,4,5])
a.append(6)
print(a)

#coding:utf-8
"""Write a Python program to insert a new item before the second element in an existing array. Go to the editor
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Insert new value 4 before 3:
New array: array('i', [1, 4, 3, 5, 7, 9])"""
from array import *
Original_array= array('i', [1, 3, 5, 7, 9])
Original_array.insert(1,4)
print(Original_array)
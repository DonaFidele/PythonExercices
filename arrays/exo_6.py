#coding:utf-8
"""Write a Python program to get the number of occurrences of a specified element in an array. Go to the editor
Sample Output:
Original array: array('i', [1, 3, 5, 3, 7, 9, 3])
Number of occurrences of the number 3 in the said array: 3"""
from array import *
a=array('i', [1, 3, 5, 3, 7, 9, 3])
print(a.count(3))
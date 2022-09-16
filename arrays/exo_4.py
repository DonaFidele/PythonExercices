#coding:utf-8
"""Write a Python program to get the length in bytes of one array item in the internal representation. Go to the editor
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Length in bytes of one array item: 4"""
from array import *
a=array('i',[1,2,3,4,9])
print(a.itemsize)

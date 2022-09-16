#coding:utf-8
"""
Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents and also find the size of the memory buffer in bytes. Go to the editor
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Current memory address and the length in elements of the buffer: (139741883429512, 5)
The size of the memory buffer in bytes: 20"""
from array import *
a=array('i',[1,2,3,4,9])
print(a.buffer_info())
print(a.buffer_info()[1] * a.itemsize)
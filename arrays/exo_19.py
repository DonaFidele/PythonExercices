#coding:utf-8
""" Write a Python program to get an array buffer information. Go to the editor
Sample Output:
Array buffer start address in memory and number of elements.
(140023105054240, 2)"""
from array import *
Original_array= array('i', [10,20,30,40,50])
print(Original_array.buffer_info())
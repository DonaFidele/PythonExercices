#coding:utf-8
"""Write a Python program to convert an array to an ordinary list with the same items. Go to the editor
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Convert the said array to an ordinary list with the same items:
[1, 3, 5, 3, 7, 1, 9, 3]"""
from array import *
Original_array= array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print(Original_array.tolist())

#coding:utf-8
""" Write a Python program to remove the first occurrence of a specified element from an array. Go to the editor
Sample Output:
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Remove the first occurrence of 3 from the said array:
New array: array('i', [1, 5, 3, 7, 1, 9, 3])"""
from array import *
Original_array= array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Original_array.remove(Original_array[1])
print(Original_array)
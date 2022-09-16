#coding:utf-8
""" Write a Python program to remove a specified item using the index from an array. Go to the editor
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Remove the third item form the array:
New array: array('i', [1, 3, 7, 9])"""
from array import *
Original_array= array('i', [1, 3, 5, 7, 9])
Original_array.remove(Original_array[2])
print(Original_array)
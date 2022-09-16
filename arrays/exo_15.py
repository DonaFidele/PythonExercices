#coding:utf-8
""" Write a Python program to find the first duplicate element in a given array of integers. Return -1 If there are no such elements. Go to the editor
Sample Output:
4
-1
1"""
from array import *
def test(an_array):
    for i in an_array:
        if an_array.count(i)>=2:
            return i
        return -1

print(test([4, 3, 5, 3, 7, 4, 9, 3]))
print(test([1, 3, 5, 7, 9]))
print(test([1, 3, 5, 3, 7, 1, 9, 3]))
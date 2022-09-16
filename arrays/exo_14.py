#coding:utf-8
"""Write a Python program to find whether a given array of integers contains any duplicate element. Return true if any value appears at least twice in the said array and return false if every element is distinct. Go to the editor
Sample Output:
False
True
True"""
from array import *
def test(an_array):
    for i in an_array:
        print (an_array.count(i)>=2)
    
test([1, 3, 5, 3, 7, 1, 9, 3])
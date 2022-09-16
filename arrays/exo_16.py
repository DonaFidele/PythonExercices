#coding:utf-8
""" Write a Python program to check whether it follows the sequence given in the patterns array. Go to the editor
Pattern example:
For color1 = ["red", "green", "green"] and patterns = ["a", "b", "b"]
the output should be samePatterns(color1, patterns) = true;
For color2 = ["red", "green", "greenn"] and patterns = ["a", "b", "b"]
the output should be samePatterns (strings, color2) = false."""
from array import *
def test(an_array):
    for i in an_array:
        if an_array.count(i)>=2:
            return i
        return -1

print(test([4, 3, 5, 3, 7, 4, 9, 3]))
print(test([1, 3, 5, 7, 9]))
print(test([1, 3, 5, 3, 7, 1, 9, 3]))
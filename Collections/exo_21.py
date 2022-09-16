#coding:utf-8
""" Write a Python program to count most and least common characters in a given string. Go to the editor
Sample Output:
Original string:
hello world
Most common character of the said string: l
Least common character of the said string: h"""
from collections import Counter
string="hello world"
print(max(Counter(string),key=Counter(string).get))
print(min(Counter(string),key=Counter(string).get))
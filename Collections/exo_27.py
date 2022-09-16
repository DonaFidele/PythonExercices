#coding:utf-8
"""Write a Python program to remove duplicate words from a given string use collections module. Go to the editor
Sample Output:
Original String:
Python Exercises Practice Solution Exercises
After removing duplicate words from the said string:
Python Exercises Practice Solution"""
from collections import Counter
def remove_duplicate(str):
    return [k for k,v in Counter(str.split()).items()]
print(*remove_duplicate("Python Exercises Practice Solution Exercises"))
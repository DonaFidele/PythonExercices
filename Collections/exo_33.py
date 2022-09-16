#coding:utf-8
""" Write a Python program to count the number of students of individual class. Go to the editor
Sample Output:
Counter({'VI': 3, 'V': 2, 'VII': 1})"""
from collections import Counter
def count_occurrence(tuple):
    return Counter(a[0] for a in tuple)

print(count_occurrence((('V', 1),('VI', 1),('V', 2),('VI', 2),('VI', 3),('VII', 1))))
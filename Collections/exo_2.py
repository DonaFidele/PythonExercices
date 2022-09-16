#coding:utf-8
"""
Write a Python program to find the most common elements and their counts of a specified text. Go to the editor
Original string: lkseropewdssafsdfafkpwe
Most common three characters of the said string:
[('s', 4), ('e', 3), ('f', 3)]"""
from collections import Counter
str="lkseropewdssafsdfafkpwe"
print(Counter(str).most_common(3))
#coding:utf-8
"""
 Write a Python program to check if a nested list is a subset of another nested list. 
Original list:
[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
[[1, 3], [13, 15, 17]]
If the one of the said list is a subset of another.:
True
Original list:
[[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
[[[3, 4], [5, 6]]]
If the one of the said list is a subset of another.:
True
Original list:
[[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
[[[3, 4], [5, 6]]]
If the one of the said list is a subset of another.:
False
"""

print(all(i in [[[1, 2], [2, 3]], [[3, 4], [5, 6]]] for i in [[[3, 4], [5, 6]]]))

#coding:utf-8
"""
Write a Python program to sort a given list of lists by length and value using lambda. Go to the editor
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value:
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]"""

liste=[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
maximum_length=sorted(liste, key=lambda x: (len(x) ,x ))
print(maximum_length)
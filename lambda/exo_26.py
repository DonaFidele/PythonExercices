#coding:utf-8
"""
Write a Python program to find the list with maximum and minimum length using lambda. Go to the editor
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])"""

liste=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
maximum_length=max(sorted(liste, key=lambda x:len(x)),key=len)
minimum_length=min(sorted(liste, key=lambda x:len(x)),key=len)
print(f"List with maximum length of lists:{len(minimum_length),minimum_length}")
print(f"List with minimum length of lists:{len(maximum_length),maximum_length}")
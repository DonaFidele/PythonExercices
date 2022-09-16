#coding:utf-8
"""Write a Python program to insert items into a list in sorted order. Go to the editor
Expected Output:
Original List:
[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
Sorted List:
[14, 25, 36, 36, 45, 47, 48, 68, 69, 78]"""
import bisect
Original_list=[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
Original_list.insert(1,3)
print(Original_list)
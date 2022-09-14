#coding:utf-8
"""
Write a Python program to find intersection of two given arrays using Lambda. Go to the editor
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]
"""
def test(array1,array2):
    r=list(filter(lambda x:x in array1,array2))
    return r

print(test([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]))
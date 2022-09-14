#coding:utf-8
"""
Write a Python program to find index position and value of the maximum and minimum values in a given list of numbers using lambda. Go to the editor
Original list:
[12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
Index position and value of the maximum value of the said list:
(5, 89)
Index position and value of the minimum value of the said list:
(3, 10.11)"""
def position_max_min(nums):
    max_result = max(enumerate(nums), key=(lambda x: x[1]))
    min_result = min(enumerate(nums), key=(lambda x: x[1]))
    return max_result,min_result
print(position_max_min([12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]))
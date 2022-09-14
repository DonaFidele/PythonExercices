#coding:utf-8
"""
Write a Python program to check whether a specified list is sorted or not using lambda. Go to the editor
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
True
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
False"""
def is_sort_list(nums, key=lambda x: x):
    for i, e in enumerate(nums[1:]):
        if key(e) < key(nums[i]): 
            return False
    return True

print(is_sort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17]))
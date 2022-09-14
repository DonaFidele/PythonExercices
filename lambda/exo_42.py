#coding:utf-8
"""Write a Python program to calculate the product of a given list of numbers using lambda. Go to the editor
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Product of the said list numbers:
3628800
list2: [2.2, 4.12, 6.6, 8.1, 8.3]
Product of the said list numbers:
4021.8599520000007"""

import functools 
def remove_duplicates(nums):
    result = functools.reduce(lambda x, y: x * y, nums, 1)
    return result
nums1 = [1,2,3,4,5,6,7,8,9,10]
nums2 = [2.2,4.12,6.6,8.1,8.3]
print("list1:", nums1)
print("Product of the said list numbers:")
print(remove_duplicates(nums1))
print("\nlist2:", nums2)
print("Product of the said list numbers:")
print(remove_duplicates(nums2))
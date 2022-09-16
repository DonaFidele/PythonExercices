#coding:utf-8
""" Write a Python program to break a given list of integers into sets of a given positive number. Return true or false. Go to the editor
Sample Output:
Original list: [1, 2, 3, 4, 5, 6, 7, 8]
Number to devide the said list: 4
True
Original list: [1, 2, 3, 4, 5, 6, 7, 8]
Number to devide the said list: 3
False"""
import collections as clt
def check_break_list(nums, n):
    coll_data = clt.Counter(nums)
    for x in sorted(coll_data.keys()):
        for index in range(1, n):
            coll_data[x+index] = coll_data[x+index]  - coll_data[x]
            if coll_data[x+index] < 0:
                return False
    return True

nums = [1,2,3,4,5,6,7,8]
n = 4
print("Original list:",nums)
print("Number to devide the said list:",n)
print(check_break_list(nums, n))
nums = [1,2,3,4,5,6,7,8]
n = 3
print("\nOriginal list:",nums)
print("Number to devide the said list:",n)
print(check_break_list(nums, n))

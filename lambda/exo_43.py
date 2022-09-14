#coding:utf-8
"""
Write a Python program to multiply all the numbers in a given list using lambda. Go to the editor
Original list:
[4, 3, 2, 2, -1, 18]
Mmultiply all the numbers of the said list: -864
Original list:
[2, 4, 8, 8, 3, 2, 9]
Mmultiply all the numbers of the said list: 27648
"""
from functools import reduce 
def mutiple_list(nums):
    result =  reduce(lambda x, y: x*y, nums)
    return result

print(mutiple_list([4, 3, 2, 2, -1, 18]))
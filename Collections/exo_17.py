#coding:utf-8
"""Write a Python program to find the majority element from a given array of size n using Collections module. Go to the editor
Sample Output:
10"""
import collections
def test(nums):
    count_ele=collections.Counter(nums)
    return count_ele.most_common()[0][0]

print(test([10,10,20,30,40,10,20,10]))
#coding:utf-8
"""
Write a Python program to check a given list of integers where the sum of the first i integers is i. Go to the editor
Input:
[0, 1, 2, 3, 4, 5]
Output:
False
Input:
[1, 1, 1, 1, 1, 1]
Output:
True
Input:
[2, 2, 2, 2, 2]
Output:
False
"""
def test(nums):
    return all([sum(nums[:i]) == i for i in range(len(nums))])

print(test([1, 1, 1, 1, 1, 1]))
print(test([2, 2, 2, 2, 2]))
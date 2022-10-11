#coding:utf-8
"""Write a Python program to get the sum of a non-negative integer. Go to the editor
Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9"""

def Sum(num):
    num=str(num)
    if len(num)==1:
        return num[0]
    else:
        return int(num[0]) + int(Sum(int(num[1:])))
print(Sum(345))
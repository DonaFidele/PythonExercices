#coding:utf-8
"""
Write a Python program to returns sum of all divisors of a number. Go to the editor
Test Data:
If number = 8
If number = 12
Expected Output:
7
16"""

def sum_divisor(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum
print(sum_divisor(8))
print(sum_divisor(12))
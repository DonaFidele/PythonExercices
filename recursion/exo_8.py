#coding:utf-8
"""Write a Python program to calculate the harmonic sum of n-1. Go to the editor
Note: The harmonic sum is the sum of reciprocals of the positive integers.
Example :
harmonic series"""

def harmonicSum(n):
    
    
    if n<2 :
        return 1
    else:
        return 1/n+harmonicSum(n-1)

print(harmonicSum(10))
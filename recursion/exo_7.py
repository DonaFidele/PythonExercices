#coding:utf-8
"""Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0). Go to the editor
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30"""
def Sum(n):
    
    if n==0 :
        return 0
    else:
        return n+Sum(n-2)

print(Sum(6))
print(Sum(10))
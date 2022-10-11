#coding:utf-8
"""
 Write a Python program to calculate the difference between the squared sum of first n natural numbers and the sum of squared first n natural numbers.(default value of number=2). Go to the editor
Test Data:
If sum_difference(12)
Expected Output :
5434
"""
def difference_square(n=2):
    squared_sum=0
    sum_squared=0
    for i in range(1,n+1):
        squared_sum+=i
        
        sum_squared+=i**2
    squared_sum=squared_sum**2
    return abs(squared_sum-sum_squared)

print(difference_square(12))
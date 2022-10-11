#coding:utf-8
"""Write a Python program to calculate the geometric sum of n-1. Go to the editor
Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.
Example :
harmonic series"""
def geometric_sum(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)
 
print(geometric_sum(7))
print(geometric_sum(4))
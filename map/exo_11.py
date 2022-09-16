#coding:utf-8
# Write a Python program to compute the sum of elements of a given array of integers, use map() function
from array import array
nums = array('i', [1, 2, 3, 4, 5, -15])
print(sum(map(lambda x:x,nums)))
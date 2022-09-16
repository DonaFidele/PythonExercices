#coding:utf-8
# Write a Python program to find the ration of positive numbers, negative numbers and zeroes in an array of integers.
from array import array
nums = array('i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
positive_nums=list(filter(lambda x:x>0,nums))
negative_nums=list(filter(lambda x:x<0,nums))
zero_num=list(filter(lambda x:x==0,nums))
print(positive_nums,negative_nums,zero_num)
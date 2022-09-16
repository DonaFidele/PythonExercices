#coding:utf-8
#Write a Python program to count the same pair in two given lists. use map() function
from operator import eq
nums1 = [1,2,3,4,5,6,7,8]
nums2 = [2,2,3,1,2,6,7,9]
print(sum(map(eq,nums2,nums1)))
#coding:utf-8
#Write a Python program to convert a given list of integers and a tuple of integers in a list of strings. 
nums1 = [6, 5, 3, 9]
nums2 = (0, 1, 7, 7)
print(list(map(lambda x:str(x),nums1)))
print(tuple(map(lambda x:str(x),nums2)))
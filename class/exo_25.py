#coding:utf-8
#Write a Python program to get the class name of an instance in Python. 
import itertools
x = itertools.cycle('ABCD')
print(type(x).__name__)

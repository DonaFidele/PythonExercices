#coding:utf-8
"""
Write a Python program to check whether a specified value is contained in a group of values. 
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""

def specified_value(liste,value):
    return value in liste

print(specified_value([1, 5, 8, 3],3))
print(specified_value([1, 5, 8, 3],-1))
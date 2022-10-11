#coding:utf-8
""" Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. Go to the editor

"""
import re
regex=re.compile(r"([0-9]{1,3})")
result=regex.findall("Exercises number 1, 12, 13, and 345 are important")
for i in result:
    print(i)
    


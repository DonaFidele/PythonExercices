#coding:utf-8
# Write a Python program to import built-in re module and display the namespace of the said module. 
import re
for name in re.__dict__:
    print(name)
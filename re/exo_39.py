#coding:utf-8
#Write a Python program to remove multiple spaces in a string. 

import re
def remove_space(str):
    return re.sub(' +',' ',str)
print(remove_space("Write a      Python      program to remove   multiple spaces"))
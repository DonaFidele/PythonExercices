#coding:utf-8
#Write a Python program to separate and print the numbers and their position of a given string. 
import re
strings="The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
for i in re.finditer('\d+',strings):
    print(i.group(0),"\nIndex position:",i.start())

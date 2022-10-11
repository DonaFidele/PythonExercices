#coding:utf-8
# Write a Python program to find all five characters long word in a string. 
import re
strings="The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
for i in re.findall(r'\w{5}',strings):
    print(i)
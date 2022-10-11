#coding:utf-8
# Write a Python program to find all words starting with 'a' or 'e' in a given string.
import re 
strings="The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
result=re.findall('[ae]\w+',strings)
for i in result:
    print(i)
#coding:utf-8
# Write a Python program to abbreviate 'Road' as 'Rd.' in a given string. 
import re
strings="Write a Python program to abbreviate 'Road' as 'Rd.'"
print(re.sub("Road","Rd",strings))
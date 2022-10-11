#coding:utf-8
#Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon. 
import re
text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", text,count=2))
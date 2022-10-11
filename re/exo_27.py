#coding:utf-8
#Write a Python program to separate and print the numbers of a given string. 
import re
strings="Ten 10, Twenty 20, Thirty 30"
result=re.findall('\d+',strings)
for i in result:
    print(i)
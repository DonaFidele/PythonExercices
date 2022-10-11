#coding:utf-8
#Write a Python program to do a case-insensitive string replacement. 
import re
text = "PHP Exercises"
print("Original Text: ",text)
redata = re.compile(re.escape('php'), re.IGNORECASE)
new_text = redata.sub('php', 'PHP Exercises')
print("Using 'php' replace PHP") 
print("New Text: ",new_text)
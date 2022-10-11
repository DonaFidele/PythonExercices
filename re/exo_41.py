#coding:utf-8
# Write a Python program to remove everything except alphanumeric characters from a string. 
import re
def remove_space(str):
    return re.sub('[\W_]','',str)
print(remove_space("Write a   (-è_)   Python     _|[{}] program to remove  -*/4 multiple spaces"))

#coding:utf-8
#Write a Python program to remove newline characters from a file. 
import re
with open('file','r+') as f:
    w=f.read()
    w1=re.sub(r'\n','',w)
    f.write(w1)
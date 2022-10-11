#coding:utf-8
#Write a Python program to copy the contents of a file to another file

with open('file','r') as f:
    dataCopy=f.read()

with open ('fileCopy','w') as f1:
    f1.write(dataCopy)
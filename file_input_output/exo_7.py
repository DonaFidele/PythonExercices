#coding:utf-8
#Write a Python program to read a file line by line store it into an array.
a=[]
with open("file",'r') as f:
    for line in f:
        a.append(line)
        print(a)
#coding:utf-8
# Write a Python program to read a file line by line store it into a variable. 
with open("file",'r') as f:
    store=f.readlines()
    print(store)
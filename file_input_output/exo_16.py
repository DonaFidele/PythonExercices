#coding:utf-8
#Write a Python program to assess if a file is closed or not.
with open("file" , 'r') as f:
    f.read()
print(f.closed)

f1=open('fichier.txt','r') 
print(f1.closed)

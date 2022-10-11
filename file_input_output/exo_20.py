#coding:utf-8
#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt. 
import string
    
for letters in string.ascii_uppercase:
    filename=letters+'.txt'
    f=open(filename,'w')
    f.write('')
    
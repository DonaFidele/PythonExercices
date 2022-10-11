#coding:utf-8
#Write a Python program to match if two words from a list of words starting with letter 'P'. 
import re
liste=["Papa Ptyui",'fghj rth']
for i in liste:
    if re.match("(P\w+)\s(P\w)",i):
        print(i)
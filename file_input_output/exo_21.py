"""#coding:utf-8
#Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line. 

import string
def write_letters(n):
    with open('f.txt','w') as f:
        alphabet = string.ascii_uppercase
        f.writelines([alphabet[i:i+n]+'\n' for i in range(0,26,n)])

write_letters(4)"""
file = open("file1", "r")
c=file.readlines()
print(c)



file.close()
#coding:utf-8
#Write a Python program to get the file size of a plain file. 

import os
file_size=os.stat('test.txt')
print(file_size.st_size)
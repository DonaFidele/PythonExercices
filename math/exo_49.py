#coding:utf-8
"""
Write a Python program to generate random integers in a specific numerical range. Go to the editor

Expected Output :

24 12 72 13 56 80
"""
import random
for i in range(6):
    print(random.randrange(i,100),end=' ')
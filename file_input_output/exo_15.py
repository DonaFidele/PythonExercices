#coding:utf-8
#Write a Python program to read a random line from a file. 
import random
with open("file" , 'r') as f:
    lines=f.read().splitlines()
    print(random.choice(lines))
#coding:utf-8
#Write a Python program to create a list of random integers and randomly select multiple items from the said list. Use random.sample()
import random,string
print(random.sample(range(100),10))
print(random.sample(string.ascii_letters,10))
print(random.sample(range(100),10))

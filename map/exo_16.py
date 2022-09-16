#coding:utf-8
#Write a Python program to convert a given list of strings into list of lists using map function.

color = ['Red', 'Blue', 'Black', 'White', 'Pink'] 
print(list(map(lambda x:list(x),color)))
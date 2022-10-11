#coding:utf-8
#Write a python program to convert snake case string to camel case string. 
import re
def snake_to_carmel(str):
    return ''.join(x.capitalize() or '_' for x in str.split('_'))
print(snake_to_carmel('python_exercises'))
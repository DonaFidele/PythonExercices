#coding:utf-8
#Write a Python program to convert a given list of tuples to a list of strings using map function. Go to the editor

colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(list(map(lambda x:'  '.join(x),colors)))
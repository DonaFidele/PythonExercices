#coding:utf-8
#Write a Python program to check whether a file exists.

from os.path import exists
def check_file (path):
    return exists(path)

print(check_file('main.txt'))
print(check_file('exo_41.py'))
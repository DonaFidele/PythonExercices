#coding:utf-8
#Write a Python program to remove a key from a dictionary.

def remove_key(dic,k):
    del dic[k]
    return dic 

print(remove_key({'a':1,'b':2,'c':3,'d':4},'b'))
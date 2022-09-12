#coding:utf-8
#Write a Python program to check a dictionary is empty or not.

def dicEmpty(dic):
    if len(dic)==0:
        return True
    return False

print(dicEmpty({}))
print(dicEmpty({1:1}))
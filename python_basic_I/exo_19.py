#coding:utf-8
#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

def newString(word):
    if word[:2]=='Is':
        return word
    else :
        return 'Is'+word

print(newString('IsMe'))
print(newString('Me'))
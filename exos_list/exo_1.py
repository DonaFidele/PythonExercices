#coding:utf-8
#Write a Python program to sum all the items in a list. 

def sum(liste):
    somme=0
    for i in liste:
        somme+=i
    return somme

print(sum([1,2,3,5]))
#coding:utf-8
# Write a Python program to multiply all the items in a list.

def multiply(liste):
    somme=1
    for i in liste:
        somme*=i
    return somme

print(multiply([1,2,3,5]))

#une autre modification
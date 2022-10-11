#coding:utf-8
#Write a Python program to calculate the sum of a list of numbers.

def Sum(liste):
    
    if len(liste)==1:
        return liste[0]
    else:
        return liste[0] + Sum(liste[1:])
print(Sum([2, 4, 5, 6, 7]))
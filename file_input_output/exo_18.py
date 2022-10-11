#coding:utf-8
""" Write a Python program that takes a text file as input and returns the number of words of a given text file. Go to the editor
Note: Some words can be separated by a comma with no space."""

with open('fichier.txt','r' ) as f:
    som=0
    lines=f.read().split()
    for word in lines:       
        som+=1
print(som)



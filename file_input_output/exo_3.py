#coding:utf-8
#Write a Python program to append text to a file and display the text. 

with open("file",'a+') as f:
    f.write("\n j'ajoute cette phrase")
    print(f.read())
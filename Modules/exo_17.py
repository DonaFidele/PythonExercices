#coding:utf-8
#Write a Python program to create a shallow copy of a given list. Use copy.copy
import copy
a_liste=[1,2,3,4]
list_copy=copy.copy(a_liste)
a_liste+="foo"
print(a_liste,list_copy)
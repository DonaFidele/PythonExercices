#coding:utf-8
#Write a Python program to create a deep copy of a given list. Use copy.copy
import copy
a_liste=[1,2,3,4]
list_copy=copy.deepcopy(a_liste)
a_liste+="foo"
print(a_liste,list_copy)
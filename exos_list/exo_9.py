#coding:utf-8
#Write a Python program to clone or copy a list
import copy
def copy_list (liste):
    liste_copy=liste[:]
    return liste_copy

print(copy_list( ['Green', 'White', 'Black']))
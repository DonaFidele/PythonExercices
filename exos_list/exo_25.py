#coding:utf-8
#Write a Python program to select an item randomly from a list.
import random
def choice(liste):
    return random.choice(liste)

print(choice(['Green', 'White', 'Black']))
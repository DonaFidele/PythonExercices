#coding:utf-8
#Write a Python program to shuffle and print a specified list. 
import random
def shuffle_list(list):
    random.shuffle(list)
    return list

print(shuffle_list(['Green', 'White', 'Black']))
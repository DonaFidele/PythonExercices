#coding:utf-8
#Write a Python program access the index of a list.

def index_list(list):
    for index , value in enumerate(list):
        print(index, value)

index_list(['Green', 'White', 'Black'])
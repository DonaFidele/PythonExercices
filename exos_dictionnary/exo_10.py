#coding:utf-8
#Write a Python program to sum all the items in a dictionary.

def sum_item(dic):
    return sum(x for x in dic.values())

print(sum_item({1:5,2:5}))
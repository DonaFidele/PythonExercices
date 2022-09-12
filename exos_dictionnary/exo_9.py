#coding:utf-8
#Write a Python script to merge two Python dictionaries.

def merge_dics(dic1,dic2):
    dic1.update(dic2)
    return dic1
print(merge_dics( {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}, {15:15}))
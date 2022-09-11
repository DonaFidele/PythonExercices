#coding:utf-8
#Write a Python program to sort a list of nested dictionaries.

def sorted_liste(list):
    return sorted(list,key=lambda x:x['key']['subkey'])

print(sorted_liste([{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]))
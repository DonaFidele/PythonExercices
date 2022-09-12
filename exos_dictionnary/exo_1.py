#coding:utf-8
#Write a Python script to sort (ascending and descending) a dictionary by value.

def sorted_dict_ascending(dictionaries):
    return sorted(dictionaries.items())

def sorted_dict_descending(dictionaries):
    return sorted(dictionaries.items())[::-1]

print(sorted_dict_ascending({0: 10, 1: 20, 2: 30}))
print(sorted_dict_descending({0: 10, 1: 20, 2: 30}))
#coding:utf-8
# Write a Python program to sort a given dictionary by key.

def sorted_dict(dic):
    return sorted(dic.items())

print(sorted_dict({'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}))
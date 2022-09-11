#coding:utf-8
# Write a Python program to remove duplicates from a list.

def remove_duplicates(liste):
    return list(set(liste))

print(remove_duplicates([(2, 5), (1, 2), (4, 4),(4,4), (2, 3), (2, 1)]))
#coding:utf-8
# Write a Python program to check a list is empty or not. 

def list_empty_or_not(liste):
    if len(liste)>0:
        return True
    return False

print(list_empty_or_not([(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]))
print(list_empty_or_not([]))
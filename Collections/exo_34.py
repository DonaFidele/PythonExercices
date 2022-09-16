#coding:utf-8
"""Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order. Go to the editor
Sample Output:
Afghanistan 93
Albania 355
Algeria 213
Andorra 376
Angola 244
In reverse order:
Angola 244
Andorra 376
Algeria 213
Albania 355
Afghanistan 93"""
from collections import OrderedDict
def count_occurrence(dicts):
    dico=OrderedDict(dicts.items())
    for k,v in dico.items():
        print(k,v)
    print("\n")
    for k,v in reversed(dico.items()):
        print(k,v)
    
count_occurrence( {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244})
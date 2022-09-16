#coding:utf-8
"""Write a Python program to group a sequence of key-value pairs into a dictionary of lists. Go to the editor
Sample Output:
[('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]"""
from collections import defaultdict
def count_occurrence(liste):
    dico=defaultdict(list)
    for k,v in liste:
        dico[k].append(v)
    return [(x,y) for x,y in dico.items()]
    
print(count_occurrence([('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]))
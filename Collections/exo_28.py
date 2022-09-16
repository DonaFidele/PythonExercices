#coding:utf-8
"""Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. Use collections module. Go to the editor
Sample Output:
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})"""
from collections import defaultdict
def remove_duplicate(liste):
    dicts=defaultdict(list)
    for k,v in liste:
        dicts[k].append(v)
    return dicts
print(remove_duplicate([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]))
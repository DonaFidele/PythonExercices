#coding:utf-8
"""Write a Python program to find the class wise roll number from a tuple-of-tuples. Go to the editor
Sample Output:
defaultdict(<class 'list'>, {'V': [1, 2], 'VI': [1, 2, 3], 'VII': [1]})"""

from collections import Counter,defaultdict
def count_occurrence(tuple):
    dicts=defaultdict(list)
    for k,v in tuple:
        dicts[k].append(v)
    return dicts

print(count_occurrence((('V', 1),('VI', 1),('V', 2),('VI', 2),('VI', 3),('VII', 1))))
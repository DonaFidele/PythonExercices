#coding:utf-8
"""
Write a Python program to combine two dictionary adding values for common keys. 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
"""

def combine_values(dic1,dic2):
    
    for k ,v in dic2.items():
        if k not in dic1.keys():
            dic1[k]=v
            
        else:
            dic1[k]=dic1[k]+dic2[k]
    return dic1

print(combine_values({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400}))
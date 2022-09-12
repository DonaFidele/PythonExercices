#coding:utf-8
"""
Write a Python program to find the largest number where commas or periods are decimal points. 
Input:
['100', '102,1', '101.1']
Output:
102.1
"""
def test(liste):
    return max(float(i.replace(',','.'))for i in liste)

print(test(['100', '102,1', '101.1']))
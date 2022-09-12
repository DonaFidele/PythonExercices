#coding:utf-8
"""
Write a Python program to select a string from a given list of strings with the most unique characters. 
Input:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Output:
abcdefhijklmnop
Input:
['Green', 'Red', 'Orange', 'Yellow', '', 'White']
Output:
Orange
"""

def test(liste):
    return max([i for i in liste if len(''.join(list(set(i))))==len(i) ],key=len)

print(test(['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']))
print(test(['Green', 'Red', 'Orange', 'Yellow', '', 'White']))
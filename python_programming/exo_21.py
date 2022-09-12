#coding:utf-8
"""
Write a Python program to check, for each string in a given list, whether the last character is an isolated letter or not. Return True or False. Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
[False, False, False, False]
Input:
['ca t', 'car', 'fea r', 'cente r']
Output:
[True, False, True, True]
"""

def test(liste):
    return[word[-2:-1]==" " for word in liste]
print(test(['ca t', 'car', 'fea r', 'cente r']))
#coding:utf-8
"""
Write a Python program to split a given string (s) into strings if there is a space in the string, otherwise split on commas if there is a comma, otherwise return the list of lowercase letters with odd order (order of a = 0, b = 1, etc.) Go to the editor
Input:
a b c d
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['a', 'b', 'c', 'd']
Input:
a,b,c,d
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['a', 'b', 'c', 'd']
Input:
abcd
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['b', 'd']
"""

def test(strg):
    if ' ' in strg:
        return strg.split(' ')
    elif ',' in strg:
        return strg.split(',')
    else:
        return [strg[i] for i in range(len(strg)) if i%2!=0]
print(test("a b c d"))
print(test("a,b,c,d"))
print(test("abcd"))
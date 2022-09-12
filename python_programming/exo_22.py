#coding:utf-8
"""
Write a Python program to compute the sum of the ASCII values of the upper-case characters in a given string. Go to the editor
Input:
PytHon ExerciSEs
Output:
373
Input:
JavaScript
Output:
157
"""
def test(strs):
    return sum(map(ord,filter(str.isupper,strs)))
print(test('PytHon ExerciSEs'))


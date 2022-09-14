#coding:utf-8
"""
  Write a Python program to remove the characters which have odd index values of a given string.
"""
def test(string):
    string_l=list(string)
    return ''.join([v for i,v in enumerate(string_l) if i%2!=0])
print(test("Python"))
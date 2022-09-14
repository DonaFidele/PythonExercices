#coding:utf-8
"""
  Write a Python program to change a given string to a new string where the first and last chars have been exchanged. 
"""
def test(string):
    return string[-1]+string[1:-1]+string[0]
print(test("Python"))
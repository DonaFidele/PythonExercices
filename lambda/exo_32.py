#coding:utf-8
"""
Write a Python program to count float number in a given mixed list using lambda. Go to the editor
Original list:
[1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
Number of floats in the said mixed list:
3"""
liste=[1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
result=len(list(filter(lambda x:isinstance(x,float),liste)))
print(result)
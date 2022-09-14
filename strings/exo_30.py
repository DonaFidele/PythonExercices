#coding:utf-8
"""Write a Python program to print the following floating numbers upto 2 decimal places."""

def test(flt):
    return str(flt).split('.')[0]+'.'+str(flt).split('.')[1][:2]
print(test(3.12345))
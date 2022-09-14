#coding:utf-8
#Write a Python program to print the following floating numbers with no decimal places. 

def test(flt):
    return str(flt).split('.')[0]
print(test(3.12345))
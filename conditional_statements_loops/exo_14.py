#coding:utf-8
"""
Write a Python program that accepts a string and calculate the number of digits and letters. Go to the editor
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2
"""
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)
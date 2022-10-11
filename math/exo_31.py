#coding:utf-8
"""
Write a Python program to convert a binary number to decimal number. Go to the editor

Expected Output :

Input a binary number: 101011                                           
The decimal value of the number is 43

"""

def binary_to_decimal():
    b_num = list(input("Input a binary number: "))
    value = 0

    for i in range(len(b_num)):
        digit = b_num.pop()
        if digit == '1':
            value = value + pow(2, i)
    return value
print(binary_to_decimal())


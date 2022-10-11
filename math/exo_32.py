#coding:utf-8
"""
 Write a Python program to print a complex number and its real and imaginary parts. Go to the editor

Expected Output :

Complex Number:  (2+3j)                                                          
Complex Number - Real part:  2.0                                                 
Complex Number - Imaginary part:  3.0"""

def complex_number (num):
    a=num.split("+")
    for i in a:
        if i[-1]=='j':
            print(f"Imaginary part:{float(i[:-1])}")
        else:
            print(f"Real part:{float(i[::])}")
complex_number("2j+3")
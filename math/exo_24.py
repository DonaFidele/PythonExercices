#coding:utf-8
"""
Write a Python program to convert a float to ratio. Go to the editor

Expected Output :

21/5 
"""
from fractions import Fraction
value=4.2
print(Fraction(value).limit_denominator())
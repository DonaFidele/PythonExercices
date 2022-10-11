#coding:utf-8
"""
Write a Python program to display the fraction instances of the string representation of a number. Go to the editor

Sample data : '0.7', '2.5', '9.32', '7e-1'

Expected Output :

 0.7 = 7/10                                                                  
 2.5 = 5/2                                                                  
9.32 = 233/25                                                                  
7e-1 = 7/10"""
from fractions import Fraction
print(Fraction(0.7).limit_denominator())
print(Fraction(2.5).limit_denominator())
print(Fraction(9.32).limit_denominator())

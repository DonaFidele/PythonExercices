#coding:utf-8
"""
Write a Python program to add, subtract, multiply and divide two fractions. Go to the editor

Expected Output :

2/3 + 3/7 = 23/21                                                                
2/3 - 3/7 = 5/21                                                                 
2/3 * 3/7 = 2/7                                                                  
2/3 / 3/7 = 14/9 
"""
from fractions import Fraction
print(f"2/3 + 3/7 = {Fraction(2,3)+Fraction(3,7)}")
print(f"2/3 - 3/7 ={Fraction(2,3)-Fraction(3,7)}")
print(f"2/3 * 3/7 ={Fraction(2,3)*Fraction(3,7)}")
print(f"2/3 / 3/7 ={Fraction(2,3)/Fraction(3,7)}")
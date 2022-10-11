#coding:utf-8
"""
Write a Python program to calculate the discriminant value. Go to the editor
Note: The discriminant is the name given to the expression that appears under the square root (radical) sign in the quadratic formula.
Test Data:
The x value : 4
The y value : 0
The z value : -4
Expected Output:
Two Solutions. Discriminant value is : 64.0"""

def discriminant():
    a = float(input('The a: '))
    b = float(input('The b: '))
    c = float(input('The c: '))
    discriminant=b**2-(4*a*c)
    if discriminant > 0:
        print('Two Solutions. Discriminant value is:', discriminant)
    elif discriminant == 0:
        print('One Solution. Discriminant value is:', discriminant)
    elif discriminant < 0:
        print('No Real Solutions. Discriminant value is:', discriminant)

discriminant()
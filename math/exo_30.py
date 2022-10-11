#coding:utf-8
"""
Write a Python program to find the roots of a quadratic function. Go to the editor

Expected Output :

Quadratic function : (a * x^2) + b*x + c                                
a: 25                                                                   
b: 64                                                                   
c: 36                                                                   
There are 2 roots: -0.834579 and -1.725421
"""
from math import sqrt
def roots_quadratic():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    discriminant=b**2 - 4*a*c
    if discriminant > 0:
        num_roots = 2
        x1 = (((-b) + sqrt(discriminant))/(2*a))     
        x2 = (((-b) - sqrt(discriminant))/(2*a))
        print("There are 2 roots: %f and %f" % (x1, x2))
    elif discriminant == 0:
        num_roots = 1
        x = (-b) / 2*a
        print("There is one root: ", x)
    else:
        num_roots = 0
        print("No roots, discriminant < 0.")
        exit()

print(roots_quadratic())
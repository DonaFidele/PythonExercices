#coding:utf-8
"""
Write a Python program to calculate the area of regular polygon. Go to the editor

Expected Output :

Input number of sides: 4                                                
Input the length of a side: 25                                          
The area of the polygon is:  625.0000000000001
"""

from math import tan, pi
def area_of_regular_polygon():
    n_sides = int(input("Input number of sides: "))
    s_length = float(input("Input the length of a side: "))
    return n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))

print(area_of_regular_polygon())
#coding:utf-8
"""
Write a Python program to find the maximum and minimum numbers from the specified decimal numbers. Go to the editor

Decimal numbers : 2.45, 2.69, 2.45, 3.45, 2.00, 0.04, 7.25

Expected Output :

Maximum:  7.25                                                                  
Minimum:  0.04
"""
def max_min(liste):
    return f"Maximum :{max(liste)}\nMinimum :{min(liste)}"

print(max_min([2.45, 2.69, 2.45, 3.45, 2.00, 0.04, 7.25]))
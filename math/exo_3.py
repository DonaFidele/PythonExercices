#coding:utf-8
""" Write a Python program to calculate the area of a trapezoid. Go to the editor
Note : A trapezoid is a quadrilateral with two sides parallel. The trapezoid is equivalent to the British definition of the trapezium. An isosceles trapezoid is a trapezoid in which the base angles are equal so.
Test Data:
Height : 5
Base, first value : 5
Base, second value : 6
Expected Output: Area is : 27.5"""
def trapezoid_area(base1,base2):
    height=float(input("height: "))
    return ((base1+base2)*height)/2

print(trapezoid_area(5,6))
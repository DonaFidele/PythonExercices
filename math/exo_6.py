#coding:utf-8
"""
Write a Python program to calculate surface volume and area of a sphere. Go to the editor
Note: A sphere is a perfectly round geometrical object in three-dimensional space that is the surface of a completely round ball.
Test Data:
Radius of sphere : .75
Expected Output :
Surface Area is : 7.071428571428571
Volume is : 1.7678571428571428
"""

pi=22/7
def sphere_area():
    radian = float(input('Radius of sphere: '))
    return  4 * pi * radian **2

def sphere_volume():
    radian = float(input('Radius of sphere: '))
    return  (4/3) * (pi * radian ** 3)

print("Surface Area is: ",sphere_area())
print('\n')
print("Volume is: ",sphere_volume())
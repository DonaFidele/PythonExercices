#coding:utf-8
"""Write a Python program to calculate surface volume and area of a cylinder. Go to the editor
Note: A cylinder is one of the most basic curvilinear geometric shapes, the surface formed by the points at a fixed distance from a given straight line, the axis of the cylinder.
Test Data:
volume : Height (4), Radius(6)
Expected Output:
Volume is : 452.57142857142856
Surface Area is : 377.1428571428571
"""
pi=22/7
def cylinder_area():
    height = float(input('Height of cylinder: '))
    radian = float(input('Radius of cylinder: '))
    return  pi * radian * radian * height

def cylinder_volume():
    height = float(input('Height of cylinder: '))
    radian = float(input('Radius of cylinder: '))
    return  ((2*pi*radian) * height) + ((pi*radian**2)*2)

print("Surface Area is: ",cylinder_area())
print('\n')
print("Volume is: ",cylinder_volume())
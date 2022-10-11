#coding:utf-8
"""
 Write a Python program to calculate the area of the sector. Go to the editor
Note: A circular sector or circle sector, is the portion of a disk enclosed by two radii and an arc, where the smaller area is known as the minor sector and the larger being the major sector.
Test Data:
Radius of a circle : 4
Angle measure : 45
Expected Output:
Sector Area: 6.285714285714286
"""

pi=22/7
def sector_area():
    radius = float(input('Radius of Circle: '))
    angle = float(input('angle measure: '))
    if angle >= 360:
        return "value error\nAngle is not possible"
    return  (pi*radius**2) * (angle/360)

print("Sector Area: ",sector_area())

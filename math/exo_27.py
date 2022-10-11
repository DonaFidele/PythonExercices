#coding:utf-8
"""
 Write a Python program to calculate the distance between two points using latitude and longitude. Go to the editor

Expected Output :

Input coordinates of two points:                                        
Starting latitude: 23.5                                                 
Ending longitude: 67.5                                                  
Starting latitude: 25.3                                                 
Ending longitude: 69.5                                                  
The distance is 284.73km."""

from math import radians, sin, cos, acos

print("Input coordinates of two points:")
slat = radians(float(input("Starting latitude: ")))
slon = radians(float(input("Ending longitude: ")))
elat = radians(float(input("Starting latitude: ")))
elon = radians(float(input("Ending longitude: ")))

dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
print("The distance is %.2fkm." % dist)

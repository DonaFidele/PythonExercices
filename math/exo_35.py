#coding:utf-8
#Write a Python program to convert Polar coordinates to rectangular coordinates.
import cmath
def Polar_coordinates_to_rectangular_coordinates(num,num2):
    cn = complex(3,4)
    print("Polar Coordinates: ",cmath.polar(cn))
    cn1 = cmath.rect(2, cmath.pi)
    print("Polar to rectangular: ",cn1)


Polar_coordinates_to_rectangular_coordinates(3,4)
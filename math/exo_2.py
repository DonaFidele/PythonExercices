#coding:utf-8
"""Write a Python program to convert radian to degree. Go to the editor
Test Data:
Radian : .52
Expected Result : 29.781818181818185"""
pi=22/7
radian = float(input("Input radians: "))
degree = radian*(180/pi)
print(degree)
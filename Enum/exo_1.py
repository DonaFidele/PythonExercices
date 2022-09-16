#coding:utf-8
#Write a Python program to create an Enum object and display a member name and value.

from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3

print(Color.red.name)
print(Color.red.value)
print(Color(3))
print(Color.green)
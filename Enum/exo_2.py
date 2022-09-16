#coding:utf-8
"""Write a Python program to iterate over an enum class and display individual member and their value. Go to the editor
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672"""
from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3
for data in Color:
    print(data.name,"=",data.value)
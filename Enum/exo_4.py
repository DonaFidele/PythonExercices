#coding:utf-8
"""Write a Python program to get all values from an enum class. Go to the editor
Expected output:
[93, 355, 213, 376, 244, 672]"""
import enum 
class Color(enum.IntEnum):
    red = 8
    green = 2
    blue = 3
print([data.value for data in Color])
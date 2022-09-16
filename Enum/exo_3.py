#coding:utf-8
"""Write a Python program to display all the member name of an enum class ordered by their values. Go to the editor
Expected Output:
Country Name ordered by Country Code:
Afghanistan
Algeria
Angola
Albania
Andorra
Antarctica"""
import enum 
class Color(enum.IntEnum):
    red = 8
    green = 2
    blue = 3
print('\n'.join('  ' + c.name for c in sorted(Color)))
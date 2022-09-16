#coding:utf-8
"""Write a Python program to merge more than one dictionary in a single expression. Go to the editor
Sample Output:
Original dictionaries:
{'R': 'Red', 'B': 'Black', 'P': 'Pink'} {'G': 'Green', 'W': 'White'}
Merged dictionary:
{'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White'}
Original dictionaries:
{'R': 'Red', 'B': 'Black', 'P': 'Pink'} {'G': 'Green', 'W': 'White'} {'O': 'Orange', 'W': 'White', 'B': 'Black'}
Merged dictionary:
{'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}"""
from collections import ChainMap
color1 = { "R": "Red", "B": "Black", "P": "Pink" }
color2 = { "G": "Green", "W": "White" }
color3 = { "O": "Orange", "W": "White", "B": "Black" }
print(dict((ChainMap(color1,color2,color3))))
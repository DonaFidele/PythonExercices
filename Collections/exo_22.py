#coding:utf-8
"""Write a Python program to insert an element at the beginning of a given OrderedDictionary. Go to the editor
Sample Output:
Original OrderedDict:
OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])
Insert an element at the beginning of the said OrderedDict:
Updated OrderedDict:
OrderedDict([('color4', 'Orange'), ('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])"""
from collections import OrderedDict
color_orderdict = OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')]) 
color_orderdict.update({'color4':'Orange'})
color_orderdict.move_to_end('color4',last=False)
print(color_orderdict)
#coding:utf-8
"""
 Write a Python program to sort a given list of strings(numbers) numerically using lambda. Go to the editor
Original list:
['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
Sort the said list of strings(numbers) numerically:
['-500', '-12', '0', '4', '7', '12', '45', '100', '200']"""

liste=['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
result=sorted(liste,key=lambda x:(int(x)>0, int(x)))
print(result)
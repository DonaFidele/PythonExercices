#coding:utf-8
"""Write a Python program to append items from a specified list. Go to the editor
Sample Output:
Items in the list: [1, 2, 6, -8]
Append items from the list:
Items in the array: array('i', [1, 2, 6, -8])"""
from array import *
a_liste=[1, 2, 6, -8]
a=array('i',[])
a.fromlist(a_liste)
print(a)
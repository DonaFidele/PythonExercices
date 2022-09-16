#coding:utf-8
"""Write a Python program to convert an array to an array of machine values and return the bytes representation. Go to the editor
Sample Output:
Bytes to String:
b'w3resource'
"""
from array import *
a=array('l', ['w','3','r','e','s','s','o','u','r','c','e','s'])
print(a.tostring())
#coding:utf-8
"""
'builtins' module provides direct access to all 'built-in' identifiers of Python.
Write a python program which import the abs() function using the builtins module, display the documentation of abs() function and find the absolute value of -155. 
"""
import builtins
print(dir(builtins.abs(-155)))
print(builtins.abs(-155))
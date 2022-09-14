
#coding:utf-8
"""
 Write a Python program to check whether a given string is number or not using Lambda. Go to the editor
Sample Output:
True
True
False
True
False
True
Print checking numbers:
True
True
"""
is_number=lambda x: True if x.isnumeric() else False
print(is_number('2'))
#print(is_number(2))
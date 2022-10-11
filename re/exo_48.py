#coding:utf-8
"""
Write a Python program to remove the parenthesis area in a string.
Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
Expected Output:
example
w3resource
github
stackoverflow
"""

import re
regex=re.compile(r'\(.com\)|[\[\],"]')
result=regex.sub('','["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]')

print(result)
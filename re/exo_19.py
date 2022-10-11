#coding:utf-8
"""  Write a Python program to search some literals strings in a string. Go to the editor
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'

"""
import re
regex=re.compile("fox|dog|horse")
if regex.findall('The quick brown fox jumps over the lazy dog.'):
    print('found')
else:
    print("Not found")

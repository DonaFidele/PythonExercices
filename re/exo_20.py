#coding:utf-8
"""Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs. Go to the editor

Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'"""
import re
regex=re.compile("fox")
result=regex.search('The quick brown fox jumps over the lazy dog.')
print(result.start(),"to",result.end())
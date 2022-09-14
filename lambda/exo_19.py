#coding:utf-8
"""
Write a Python program to find all anagrams of a string in a given list of strings using lambda. Go to the editor
Orginal list of strings:
['bcda', 'abce', 'cbda', 'cbea', 'adcb']
Anagrams of 'abcd' in the above string:
['bcda', 'cbda', 'adcb']"""

liste=['bcda', 'abce', 'cbda', 'cbea', 'adcb']
result=list(filter(lambda x: set(x)==set('abcd') , liste))
print(result)
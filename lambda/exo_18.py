#coding:utf-8
"""
Write a Python program to find palindromes in a given list of strings using Lambda. Go to the editor
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']"""
liste=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
result=list(filter(lambda x:x[:len(x)//2]==x[len(x)//2+1:] , liste))
print(result)
#coding:utf-8
"""
 Write a Python program that sum the length of the names of a given list of names after removing the names that starts with an lowercase letter. Use lambda function. Go to the editor
Result:
16"""

sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
print("Result:")
print(len(''.join(sample_names)))
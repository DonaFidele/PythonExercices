#coding:utf-8
"""
 Write a Python program to extract specified size of strings from a give list of string values using lambda. Go to the editor
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8
After extracting strings of specified length from the said list:
['practice', 'solution']"""
def test(liste, size):
    result = list(filter(lambda e: len(e) == size, liste))
    return result
print(test(['Python', 'list', 'exercises', 'practice', 'solution'],8))
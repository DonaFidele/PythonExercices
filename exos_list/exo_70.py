#coding:utf-8
"""
Write a Python program to find the items starts with specific character from a given list. 
Expected Output:
Original list:
['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
Items start with a from the said list:
['abcd', 'abc', 'acjd']
Items start with d from the said list:
['dagfa']
Items start with w from the said list:
[]
"""

def items_starts_with(liste,lettre):
    return [x for x in liste if x[0]==lettre]

print(items_starts_with(['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd'],'a'))
print(items_starts_with(['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd'],'d'))
print(items_starts_with(['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd'],'w'))
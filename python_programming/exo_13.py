#coding:utf-8
"""
 Write a Python program to find the strings in a given list, starting with a given prefix. 
Input:
[( ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
Output:
['dog', 'donut']
"""

def test(liste,prefix):
    return [ i for i in liste if i[:len(prefix)]==prefix]

print(test(('cat', 'dog', 'shatter', 'donut', 'at', 'todo'),"do"))
print(test(('cat', 'car', 'fear', 'center'),"ca"))
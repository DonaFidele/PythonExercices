#coding:utf-8
"""
 Write a Python program find the strings in a given list containing a given substring. Go to the editor
Input:
[(ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']
Input:
[(oe,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
[]
"""
def test(liste,prefix):
    return [ i for i in liste if prefix in i]

print(test(('cat', 'dog', 'shatter', 'donut', 'at', 'todo'),"do"))
print(test(('cat', 'car', 'fear', 'center'),"ca"))
print(test(('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''),"oe"))
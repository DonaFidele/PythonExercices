#coding:utf-8
"""
Write a Python program find the longest string of a given list of strings. Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
center
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
shatter
"""
def test(liste):
    return max(liste,key=len)
print(test(['cat', 'car', 'fear', 'center']))
print(test(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']))
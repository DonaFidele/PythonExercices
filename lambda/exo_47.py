#coding:utf-8
"""Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings. Go to the editor
Original list:
[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
Sort the said mixed list of integers and strings:
[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']"""
liste=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
result=sorted(liste,key=lambda x:(isinstance(x, str), x))
print(result)
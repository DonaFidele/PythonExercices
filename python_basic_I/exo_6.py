#coding:utf-8
"""
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

numbers=input("Entry a sequence of comma-separated numbers \n")
print(f"Liste:{numbers.split(',')} \nTuple:{tuple(numbers.split(','))}")
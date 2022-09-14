#coding:utf-8
"""
 Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result. Go to the editor
Sample Output:
25
48
"""

r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))
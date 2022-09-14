
#coding:utf-8
"""
Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""
def count_number(string):
    return {i:string.count(i) for i in string}
print(count_number('google.com'))
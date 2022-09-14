#coding:utf-8
"""
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""

def test(string):
    if len(string)>2:
        return string[:2]+string[-2:]
    elif len(string)==2:
        return string*2
    else:
        return  "Empty String"
print(test('w3resource'))
print(test('w3'))
print(test('w'))
#coding:utf-8
"""
. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""
def test(string):
    if string[-3:]=='ing':
        return string+'ly'
    elif len(string)>=3:
        return string+'ing'   
    else :
        return string
    

print(test('abc'))
print(test('string'))
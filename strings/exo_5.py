#coding:utf-8
"""
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""
def test(string1,string2):
    return string2[:2]+string1[2:]+" "+string1[:2]+string2[2:]
print(test('abc', 'xyz'))
#coding:utf-8
"""
. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'
"""

def test(string):
    return string[0]+ string[1:].replace(string[0],"$")
print(test('restart'))
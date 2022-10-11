#coding:utf-8
"""
Write a Python class to reverse a string word by word. Go to the editor
Input string : 'hello .py'
Expected Output : '.py hello'"""

class ReverseString:
    def reversed(self,str):
        str=str.split()
        return ' '.join(str[::-1])

print(ReverseString().reversed('hello .py'))
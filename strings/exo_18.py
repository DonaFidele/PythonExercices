#coding:utf-8
"""
Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string. Go to the editor
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt
"""

def test(str):
	if len(str)>3:
        return str[:3]
    return str
    

print(test("Python"))
print(test("Exercices"))
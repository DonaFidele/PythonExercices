#coding:utf-8
"""
 Write a Python program to count repeated characters in a string. Go to the editor
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
"""
def test(str):
	return  {i:str.count(i) for i in str}
    

print(test("Python"))
print(test("Exercices"))
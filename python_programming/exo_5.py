#coding:utf-8
"""Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings. Go to the editor
Input:
['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
Output:
True
Input:
['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
Output:
True
"""

def test(liste):
    return liste[len(liste)-2] in liste[len(liste)-1] and liste[len(liste)-2] != liste[len(liste)-1]

print(test(['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
print(test(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']))
print(test(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']))
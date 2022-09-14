#coding:utf-8
"""
 Write a Python program to find the values of length six in a given list using Lambda. Go to the editor
Sample Output:
Monday
Friday
Sunday
"""
def test(liste):
    return list(filter(lambda x :len(x)==6,liste))

print(test(['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']))
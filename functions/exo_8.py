#coding:utf-8
"""Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]"""
def set_list(liste):
    new_liste=[]
    for i in liste:
        if i not in new_liste:
            new_liste.append(i)
    return new_liste

print(set_list([1,2,3,3,3,3,4,5]))
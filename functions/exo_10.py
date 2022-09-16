#coding:utf-8
"""Write a Python program to print the even numbers from a given list. Go to the editor
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]"""
def even_num(liste):
    new_list=[]
    for i in liste:
        if i%2==0:
            new_list.append(i)
    return new_list
print(even_num( [1, 2, 3, 4, 5, 6, 7, 8, 9]))

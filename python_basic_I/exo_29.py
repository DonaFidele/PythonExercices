#coding:utf-8
"""
Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""
color_list1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color_list_3=[]

def setListe(color_list1,color_list_2):
    for colors in color_list1:
        if colors not in color_list_2:
            color_list_3.append(colors)
    return color_list_3

print(setListe(color_list1,color_list_2))
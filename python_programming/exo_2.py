#coding:utf-8
"""
 Write a Python program that accept a list of integers and check the length and the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said list. Go to the editor
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True
Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False
"""
def count_number(liste):
    return len(liste)==8 and liste.count(liste[4])==3

print(count_number([19, 19, 15, 5, 5, 5, 1, 2]))
print(count_number([19, 15, 5, 7, 5, 5, 2]))
print(count_number([11, 12, 14, 13, 14, 13, 15, 14]))
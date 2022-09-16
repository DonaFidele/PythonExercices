#coding:utf-8
"""Write a Python program to compare two unordered lists (not sets). Go to the editor
Sample Output:
False"""
from collections import Counter
def compare_liste(liste1,liste2):
    return Counter(liste1)==Counter(liste2)
    
print(compare_liste([20, 10, 30, 10, 20, 30],[30, 20, 10, 30, 20, 50]))
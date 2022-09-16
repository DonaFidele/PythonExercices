#coding:utf-8
""" Write a Python program to count the occurrence of each element of a given list. Go to the editor
Sample Output:
Original List:
['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
Count the occurrence of each element of the said list:
Counter({'Red': 2, 'Orange': 2, 'Black': 2, 'Green': 1, 'Blue': 1, 'White': 1})
Original List:
[3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
Count the occurrence of each element of the said list:
Counter({3: 4, 5: 4, 8: 4, 0: 3, 9: 1, 1: 1, 2: 1})"""
from collections import Counter,defaultdict
from itertools import chain 
def count_occurrence(liste):
    return Counter(liste)

print(count_occurrence(['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']))
print(count_occurrence([3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]))

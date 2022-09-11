#coding:utf-8
"""
. Write a Python program to find the list with maximum and minimum length. 
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])
Original list:
[[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
List with maximum length of lists:
(3, [3, 5, 7])
List with minimum length of lists:
(1, [0])
Original list:
[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
List with maximum length of lists:
(4, [1, 34, 5, 7])
List with minimum length of lists:
(1, [12])
"""

def max_liste(liste):
    return len(max(liste,key=len)),(max(liste,key=len))

def min_liste(liste):
    return len(min(liste,key=len)),(min(liste,key=len))

print("MAXIMUM")
print(max_liste([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))
print(max_liste([[0], [1, 3], [5, 7],[3, 5, 7], [9, 11]]))
print(max_liste([[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]))

print("\nMINIMUN")
print(min_liste([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))
print(min_liste([[0], [1, 3], [5, 7],[3, 5, 7], [9, 11]]))
print(min_liste([[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]))
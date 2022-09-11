#coding:utf-8
"""Write a Python program to insert an element at a specified position into a given list. 
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
After inserting an element at kth position in the said list:
[1, 1, 12, 2, 3, 4, 4, 5, 1]
"""

def insertion(liste,element,position):
    liste[position]=element
    return liste

print(insertion([1, 1, 2, 3, 4, 4, 5, 1],12,2))

#coding:utf-8
"""
Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples. Go to the editor
Original list of tuples:
[(1, 2), (2, 3), (3, 4)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[3, 5, 7]
Original list of tuples:
[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[9, -1, 7, 8]
"""

def test(liste):
    return [sum(i) for i in liste]
print(test([(1, 2), (2, 3), (3, 4)]))
print(test([(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]))
#coding:utf-8
""" Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda. Go to the editor
Original Matrix:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
Sort the said matrix in ascending order according to the sum of its rows
[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
Original Matrix:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
Sort the said matrix in ascending order according to the sum of its rows
[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]"""
def sort_matrix(M):
    result = sorted(M, key=lambda x: sum(x)) 
    return result
print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))
#coding:utf-8
"""
Write a Python program to remove all elements from a given list present in another list using lambda. Go to the editor
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]
Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]"""

def index_on_inner_list(list1, list2):
    result = list(filter(lambda x: x not in list2, list1))
    return result

print(index_on_inner_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[2, 4, 6, 8]))
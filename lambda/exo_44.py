#coding:utf-8
"""
 Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda. Go to the editor
Original Tuple:
((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
Average value of the numbers of the said tuple of tuples:
(30.5, 34.25, 27.0)
Original Tuple:
((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
Average value of the numbers of the said tuple of tuples:
(25.5, -18.0, 3.75)"""
def average_tuple(nums):
    result = tuple(map(lambda x: sum(x) / float(len(x)), zip(*nums)))
    return result
print(average_tuple(((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))))
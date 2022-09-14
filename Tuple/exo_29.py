#coding:utf-8
"""Write a Python program to convert a given tuple of positive integers into an integer. Go to the editor
Original tuple:
(1, 2, 3)
Convert the said tuple of positive integers into an integer:
123
Original tuple:
(10, 20, 40, 5, 70)
Convert the said tuple of positive integers into an integer:
102040570
"""
def test(tuple):
    return "".join([str(i) for i in tuple ])

print(test((10, 20, 40, 5, 70)))
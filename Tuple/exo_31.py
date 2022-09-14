#coding:utf-8
"""
Write a Python program to compute element-wise sum of given tuples. Go to the editor
Original lists:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Element-wise sum of the said tuples:
(6, 9, 8, 6)"""

def test(tuple1,tuple2,tuple3):
    return tuple([tuple1[x]+tuple2[x]+tuple3[x] for x in range(len(tuple3))])

print(test((1, 2, 3, 4),(3, 5, 2, 1),(2, 2, 3, 1)))
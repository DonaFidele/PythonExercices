#coding:utf-8
"""
Write a Python program to find the maximum and minimum values in a given list of tuples using lambda function. Go to the editor
Original list with tuples:
[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
Maximum and minimum values of the said list of tuples:
(74, 62)"""
liste=[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
result=max(liste,key=lambda x:x[1])[1],min(liste,key=lambda x:x[1])[1]
print(result)
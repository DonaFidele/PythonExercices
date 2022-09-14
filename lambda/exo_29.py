#coding:utf-8
"""
Write a Python program to find the maximum value in a given heterogeneous list using lambda. Go to the editor
Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum values in the said list using lambda:
5"""
def max_val(list_val):
     max_val = max(list_val, key = lambda i: (isinstance(i, int), i))  
     return(max_val)

list_val = ['Python', 3, 2, 4, 5, 'version'] 
print("Original list:")
print(list_val)
print("\nMaximum values in the said list using lambda:")
print(max_val(list_val))
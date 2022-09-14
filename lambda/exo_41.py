#coding:utf-8
"""Write a Python program to reverse strings in a given list of string values using lambda. Go to the editor
Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']"""

def reverse_str(liste):
    return list(map(lambda x:x[::-1],liste))

print(reverse_str(['Red', 'Green', 'Blue', 'White', 'Black']))
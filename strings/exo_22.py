#coding:utf-8
"""Write a Python program to sort a string lexicographically. """
def lexicographi_sort(s):
    return sorted(s, key=str.upper)

print(lexicographi_sort('w3resource'))
print(lexicographi_sort('quic10kGbrown'))
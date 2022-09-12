#coding:utf-8
"""Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Go to the editor
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True
"""

def count_number(liste):
    return liste.count(19)==2 and liste.count(5)>=3

print(count_number([19, 19, 15, 5, 3, 5, 5, 2]))
print(count_number([19, 19, 5, 5, 5, 5, 5]))
print(count_number([19, 15, 15, 5, 3, 3, 5, 2]))
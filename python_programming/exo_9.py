#coding:utf-8
"""Write a Python program to find list integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries. Go to the editor
Input:
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
Output:
True
Input:
[1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
Output:
False
Input:
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
Output:
False
"""

def test(liste):
    return all([liste[i] != liste[i + 1] for i in range(len(liste)-1)]) and len(set(liste)) == 4

print(test([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]))
print(test([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]))
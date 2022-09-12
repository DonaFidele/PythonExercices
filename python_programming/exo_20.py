#coding:utf-8
"""
Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers. Go to the editor
Input:
[1, 2, 3, 4, 5, 6]
Output:
Increasing.
Input:
[6, 5, 4, 3, 2, 1]
Output:
Decreasing.
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
Not a monotonic sequence!
"""

def test(liste):
    for i,v in enumerate(liste):
        if v<liste[i+1] and abs(v-liste[i+1])==1:
            return "Increasing"
        elif v>liste[i+1] and abs(v-liste[i+1])==1:
            return "Decreasing"
        else:
            return "Not a monotonic sequence!"

print(test([1, 2, 3, 4, 5, 6]))
print(test([6, 5, 4, 3, 2, 1]))
print(test([19, 19, 5, 5, 5, 5, 5]))
#coding:utf-8
"""
 Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
"""
def count_pair(liste):
    pair=0
    for i in liste:
        if i%2==0:
            pair+=1
    return pair

def count_impair(liste):
    impair=0
    for i in liste:
        if i%2!=0:
            impair+=1
    return impair

print(count_pair((1, 2, 3, 4, 5, 6, 7, 8, 9) ))
print(count_impair((1, 2, 3, 4, 5, 6, 7, 8, 9) ))
#coding:utf-8
"""
Write a Python program to check whether the given strings are palindromes or not. Return True, False. 
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]
"""

def palindrome(liste):
    return [i[::]==i[::-1] for i in liste]
   

print(palindrome(['palindrome', 'madamimadam', '', 'foo', 'eyes']))
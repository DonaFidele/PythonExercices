#coding:utf-8
"""
Write a Python program that accept some words and count the number of distinct words. Print the number of distinct words and number of occurrences for each distinct word according to their appearance. Go to the editor
Input number of words: 5
Input the words:
Red
Green
Blue
Black
White
5
1 1 1 1 1"""
from collections import Counter
n = int(input("Input number of words: "))
list_words=[]
for i in range(n):
    list_words.append(input().strip())
print(len(list_words))
for w in list_words:
    print(Counter(w.split())[w],end=" ")
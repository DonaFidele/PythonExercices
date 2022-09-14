#coding:utf-8
"""
 Write a Python program to find the elements in a given set that are not in another set."""
set_word1={1, 2, 3, 'foo', 'bar'}
set_word2={1, 8, 3, 'pipi', '20'}
print(set_word2-set_word1)
print(set_word1-set_word2)
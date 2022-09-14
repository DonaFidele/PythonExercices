#coding:utf-8
"""
Write a Python program to check if a given set is superset of itself and superset of another given set. """ 
set_word1={1, 2, 3, 'foo', 'bar'}
set_word2={1, 8, 3, 'pipi', '20'}

print(set_word1.issuperset(set_word2))
print(set_word1>set_word2)
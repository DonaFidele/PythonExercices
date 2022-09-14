#coding:utf-8
"""
 Write a Python program to use of frozensets. Go to the editor
Note: Frozensets behave just like sets except they are immutable."""
set_word1={1, 2, 3, 'foo', 'bar'}
set_word2={1, 8, 3, 'pipi', '20'}
print(set_word2.isdisjoint(set_word1))
print(set_word2.difference(set_word1))
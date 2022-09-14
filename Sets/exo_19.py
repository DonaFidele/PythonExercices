#coding:utf-8
"""
 Write a Python program to remove the intersection of a 2nd set from the 1st set.
 """
set_word1={1, 2, 3, 'foo', 'bar'}
set_word2={1, 8, 3, 'pipi', '20'}
set_word1-=set_word2
print(set_word1)
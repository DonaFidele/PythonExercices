#coding:utf-8
"""
 Write a Python program to check if two given sets have no elements in common.
""" 
set_word1={1, 2, 3, 'foo', 'bar'}
set_word2={1, 8, 3, 'pipi', '20'}

print(set_word1.isdisjoint(set_word2))

#coding:utf-8
"""
Write a Python program to create a shallow copy of sets. Go to the editor

Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.
"""
set_word1={1, 2, 3, 'foo', 'bar'}
set_word2={1, 8, 3, 'pipi', '20'}
setr = set_word1.copy()
print(setr)
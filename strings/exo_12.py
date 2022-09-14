#coding:utf-8
"""
  Write a Python program to count the occurrences of each word in a given sentence.
"""
def word_count(str):
    return {i:str.count(i) for i in str.split()}
print( word_count('the quick brown fox jumps over the lazy dog.'))
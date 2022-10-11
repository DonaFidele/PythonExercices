#coding:utf-8
# Write a Python program to remove words from a string of length between 1 and a given number.
import re
def remove_words(str):
    return re.sub(r'\W*\b\w{1,3}\b','',str)
print(remove_words("The quick brown fox jumps over the lazy dog."))
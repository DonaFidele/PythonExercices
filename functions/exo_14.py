#coding:utf-8
""" Write a Python function to check whether a string is a pangram or not. Go to the editor
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"""
import string
def test(str):
    al=set(''.join(list(set(string.ascii_lowercase))))
    str=set(str.lower())
    return al <= str

print(test("xcvbn,"))
print(test("The quick brown fox jumps over the lazy dog"))
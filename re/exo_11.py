#coding:utf-8
#Write a Python program that matches a word at the end of string, with optional punctuation.
import re
def test(str):
    regex=re.compile(r"\w+\S*$")
    if regex.search(str):
        return "found"
    return "not found"

print(test("The quick brown fox jumps over the lazy dog."))
print(test("The quick brown fox jumps over the lazy dog.  "))

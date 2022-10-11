#coding:utf-8
#Write a Python program that matches a word containing 'z', not at the start or end of the word.
import re
def test(str):
    regex=re.compile(r"\Bz\B")
    if regex.search(str):
        return "found"
    return "not found"

print(test("The quick brown fox jumps over the lazy dog."))
print(test("qdfg"))
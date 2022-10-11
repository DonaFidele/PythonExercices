#coding:utf-8
#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
def test(str):
    regex=re.compile(r"^[a-z]+_[a-z]+$")
    if regex.search(str):
        return "found"
    return "not found"

print(test("aab_cbbbc"))
print(test("abAc"))

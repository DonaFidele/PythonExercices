#coding:utf-8
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
def test(str):
    regex=re.compile(r"^a.*b$")
    if regex.search(str):
        return "found"
    return "not found"

print(test("aabbbbd"))
print(test("aabAbbbc"))
print(test("accddbbjjjb"))

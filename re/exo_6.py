#coding:utf-8
# Write a Python program that matches a string that has an a followed by two to three 'b'.
import re
def test(str):
    regex=re.compile(r"a(b){2,3}")
    if regex.search(str):
        return "found"
    return "not found"

print(test("ac"))
print(test("abc"))
print(test("aabbbbbc"))
print(test("abbb"))
print(test("abb"))
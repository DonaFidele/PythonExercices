#coding:utf-8
#Write a Python program that matches a string that has an a followed by zero or one 'b'.
import re
def test(str):
    regex=re.compile(r"^a(b?)$")
    if regex.search(str):
        return "found"
    return "not found"

print(test("ac"))
print(test("abc"))
print(test("a"))
print(test("ab"))
print(test("abb"))
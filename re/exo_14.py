#coding:utf-8
#Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
import re
def test(str):
    regex=re.compile(r"^\w*$")
    if regex.search(str):
        return "found"
    return "not found"

print(test("The quick brown fox jumps over the lazy dog."))
print(test("Python_Exercises_1"))
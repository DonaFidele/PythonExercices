#coding:utf-8
#Write a Python program to check for a number at the end of a string. 
import re
def test(str):
    regex=re.compile(r".*[0-9]$")
    if regex.search(str):
        return "found"
    return "not found"

print(test("aaaazrtrez505"))
print(test("qdfgA"))
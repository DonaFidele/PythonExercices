#coding:utf-8
#Write a Python program that matches a word containing 'z'. 
import re
def test(str):
    regex=re.compile(r"[z]")
    if regex.search(str):
        return "found"
    return "not found"

print(test("aaaazrtrez"))
print(test("qdfg"))
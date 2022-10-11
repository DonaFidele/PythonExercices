#coding:utf-8
#Write a Python program where a string will start with a specific number. 
import re
def test(str):
    regex=re.compile(r"^4")
    if regex.search(str):
        return "found"
    return "not found"

print(test("41275"))
print(test("852"))
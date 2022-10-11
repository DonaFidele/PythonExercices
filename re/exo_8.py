#coding:utf-8
# Write a Python program to find the sequences of one upper case letter followed by lower case letters. 
import re
def test(str):
    regex=re.compile(r"[A-Z]+[a-z]+$")
    if regex.search(str):
        return "found"
    return "not found"

print(test("aab_cbbbc"))
print(test("AaBbGg"))

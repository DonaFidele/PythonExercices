#coding:utf-8
#  Write a Python program that matches a word at the beginning of a string. 
import re
def test(str):
    regex=re.compile(r"lol")
    if regex.match(str):
        return "found"
    return "not found"

print(test("lolsdfb"))
print(test("aabAlolbbbc"))


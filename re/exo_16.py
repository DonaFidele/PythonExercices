#coding:utf-8
#Write a Python program to remove leading zeros from an IP address. 
import re
def test(str):
    str= re.sub('\.[0]*','.',str)
    return str
print(test("216.08.094.196"))
print(test("852"))
#coding:utf-8
# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
import re
regex=re.compile(r"^[A-Za-z0-9]")
print(regex.search("ABCDEFabcdef123450"))
print(regex.search("*&%@#!}{"))
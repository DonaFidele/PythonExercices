#coding:utf-8
"""Write a Python program that checks whether a word stars and ends with a vowel in a given string. Return true if a word matches the condition; otherwise, return false.
Sample Data:
("Red Orange White") -> True
("Red White Black") -> False
("abcd dkise eosksu") -> True"""
import re
def start_with_vowel(str):
    regex=re.compile(r"[/^[aeiou]$|^([aeiou]).*\1$/")
    result=regex.search(str)
    return bool(result)


print(start_with_vowel("Red Orange White"))
print(start_with_vowel("Red White Black"))
print(start_with_vowel("abcd dkise eosksu"))
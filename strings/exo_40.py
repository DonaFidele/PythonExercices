#coding:utf-8
#Write a Python program to reverse words in a string.
def test(str):    
    return " ".join(str.split()[::-1])
print(test("Python Exercises"))

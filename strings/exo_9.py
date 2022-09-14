#coding:utf-8
"""
 Write a Python program to remove the nth index character from a nonempty string. 
"""
def test(string,n):
    return string[:n]+string[n+1:]
print(test("Python",3))
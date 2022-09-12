#coding:utf-8
"""
 Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.
Input:
922
Output:
True
Input:
914
Output:
False
Input:
854
Output:
True
Input:
854
Output:
True
"""
def verify_number(n):
    return n>4**4 and n%34==4

print(verify_number(922))
print(verify_number(914))
print(verify_number(854))

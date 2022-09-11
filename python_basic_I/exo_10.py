#coding:utf-8
"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
Sample value of n is 5
Expected Result : 615
"""
n=input("Enter an integer : ")
print(f"Result: {int(n)+int(n*2)+int(n*3)}")
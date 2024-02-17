#coding:utf-8
#Write a Python program to get the factorial of a non-negative integer. 

def factorial(n):
    if n<0:
        return "n should be positive"
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
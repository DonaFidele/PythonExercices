#coding:utf-8
#Write a Python program to solve the Fibonacci sequence using recursion

def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))

print(fibonacci(7))
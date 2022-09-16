#coding:utf-8
# Write a Python program to compute the square of first N Fibonacci numbers, using map function and generate a list of the numbers. 
import itertools
n = 10
def fibonacci_nums(x=0, y=1):
    yield x
    while True:
        yield y
        x, y = y, x + y
print("First 10 Fibonacci numbers:")
result = list(itertools.islice(fibonacci_nums(), n))
print(result)
square = lambda x: x * x 
print("\nAfter squaring said numbers of the list:")
print(list(map(square, result)))
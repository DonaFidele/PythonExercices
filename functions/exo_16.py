#coding:utf-8
""" Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included). """
def square_num():
    return [i**2 for i in range(1,31)]

print(square_num())
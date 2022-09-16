#coding:utf-8
#  Write a Python program to check if a given function is a generator or not. Use types.GeneratorType()
import types
def a(x):
    yield x
        
def b(x):
    return x

def add(x, y):
    return x + y
print(isinstance(a(555),types.GeneratorType))
print(isinstance(b(823), types.GeneratorType))
print(isinstance(add(8,2), types.GeneratorType))
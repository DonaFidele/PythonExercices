#coding:utf-8
# Write a Python program to check if a function is a user-defined function or not. Use types.FunctionType, types.LambdaType()
import types
def func(): 
    return 1

print(isinstance(func, types.FunctionType))
print(isinstance(func, types.LambdaType))
print(isinstance(lambda x: x, types.FunctionType))
print(isinstance(lambda x: x, types.LambdaType))
print(isinstance(max, types.FunctionType))
print(isinstance(max, types.LambdaType))
print(isinstance(abs, types.FunctionType))
print(isinstance(abs, types.LambdaType))
#coding:utf-8
""" Write a Python program that invoke a given function after specific milliseconds. Go to the editor
Sample Output:
Square root after specific miliseconds:
4.0
10.0
158.42979517754858"""
from time import sleep
import math
def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
print("Square root after specific miliseconds:") 
print(delay(lambda x: math.sqrt(x), 100, 16))
print(delay(lambda x: math.sqrt(x), 1000, 100))
print(delay(lambda x: math.sqrt(x), 2000, 25100))
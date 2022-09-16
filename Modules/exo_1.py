#coding:utf-8
"""
Write a Python program to generate a random color hex, a random alphabetical string, random value between two integers (inclusive) and a random multiple of 7 between 0 and 70. Use random.randint()"""
import random
import random
import string
print("Generate a random color hex:")
print("#{:06x}".format(random.randint(0, 0xFFFFFF)))
print(f"random alphabetical string :{random.choice(string.ascii_letters)}")
print(f"random value between two integers:{random.randint(1,10)}")
print(f"random multiple of 7 between 0 and 70:{random.randint(0,10)*7}")
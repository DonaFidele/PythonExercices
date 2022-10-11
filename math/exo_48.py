#coding:utf-8
"""
Write a Python program to generate random float numbers in a specific numerical range. Go to the editor

Expected Output :

 16.329 17.326 54.024 13.229 68.952 87.039
 """
import random
for x in range(6):
    print(f"{random.uniform(x,100):04.3f}",end=' ')
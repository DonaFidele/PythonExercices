#coding:utf-8
# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
from math import sqrt
def compute_distance(x1,y1,x2,y2):
    X=(x1-x2)**2
    Y=(y1-y2)**2
    return sqrt(X+Y) 

print(compute_distance(2,2,1,3)
#coding:utf-8
""" Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes. Go to the editor
Sample Output:
1
3
5
7
9
Access first three items individually
1
3
5"""
from array import *
a=array('i',[1,2,3,4,5])
print(a)
for i in a:
    print(i)
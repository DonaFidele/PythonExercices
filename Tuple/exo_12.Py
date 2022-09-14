#coding:utf-8
#Write a Python program to remove an item from a tuple. 
tuple_a=1,1,2,3,2
tuple_a=list(tuple_a)
tuple_a.remove(3)
print(tuple(tuple_a))
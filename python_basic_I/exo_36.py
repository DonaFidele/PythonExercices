#coding:utf-8
#Write a Python program to add two objects if both objects are an integer type.

def type_object(x,y):
    if type(x)==int and type (y)==int:
        return x+y
    return ('ValueError')

print(type_object(5,3))
print(type_object('4',3))

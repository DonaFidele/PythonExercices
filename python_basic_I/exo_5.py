#coding:utf-8
"""
 Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""
name=input(" Your first and last name : ")
name=name.split(" ")
print(f"Hello  {name[1]} {name[0]}")
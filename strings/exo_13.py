#coding:utf-8
"""
Write a Python script that takes input from the user and displays that input back in upper and lower cases. """
def word_count(str):
    return f"{str.upper()}\n{str.lower()}"
user_input=input("string : ")
print( word_count(user_input))
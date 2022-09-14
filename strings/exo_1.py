#coding:utf-8
#Write a Python program to calculate the length of a string. 
def calculate_length(string):
    count = 0
    for char in string:
        count += 1
    return count
print(calculate_length('w3resource.com'))
#coding:utf-8
#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. 

def copy(word,n):
    return (word[:2])*n

print(copy('baké',3))
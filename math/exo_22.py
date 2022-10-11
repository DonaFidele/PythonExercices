#coding:utf-8
# Write a python program to find the next smallest palindrome of a specified number. 
import sys
def next_smallest_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i

print(next_smallest_palindrome(99))

#coding:utf-8
# Write a python program to find the next previous palindrome of a specified number.
def next_previous_palindrome(num):
    return max([i for i in range(1,num) if str(i)==str(i)[::-1]])
print(next_previous_palindrome(1221))
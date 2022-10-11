#coding:utf-8
# Write a Python program to count the frequency of words in a file


with open('test.txt', 'r') as f:
    w=f.read().split()
print({i:w.count(i) for i in w})
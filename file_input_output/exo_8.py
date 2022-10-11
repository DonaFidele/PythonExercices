#coding:utf-8
#Write a python program to find the longest words

with open('test.txt', 'r') as f:
    w=f.read().split()
    

print([words for words in w if len(words)==len(max(w,key=len))])
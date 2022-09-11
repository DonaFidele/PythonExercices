#coding:utf-8
# Write a Python program to split a list based on first character of word. 

def split_list(word):
    return word.split(word[0])

print(split_list("abracadabra"))

#coding:utf-8
""" Write a Python function that checks whether a passed string is palindrome or not. Go to the editor
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run."""
def palindrome(str):
    if len(str)%2!=0:
        return str[:len(str)//2]==str[len(str)//2+1:][::-1]
    return str[:len(str)//2]==str[len(str)//2:][::-1] 
print(palindrome('elle'))
print(palindrome('madam'))
print(palindrome('function'))

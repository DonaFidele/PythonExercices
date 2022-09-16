#coding:utf-8
"""Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. Go to the editor
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow"""
def sorted_word(hyphen_separated):
    hyphen_separated=sorted(hyphen_separated.split('-'))
    return '-'.join(hyphen_separated)
print(sorted_word("green-red-yellow-black-white"))

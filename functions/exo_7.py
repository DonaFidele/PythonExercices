#coding:utf-8
"""Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12"""
def upper_lower(str):
    up,low=0,0   
    for letters in str:
        if letters.isupper():
            up+=1
        elif letters.islower():
            low+=1
        else:
            pass
    return f"uppers:{up}\nlowers:{low}"

print(upper_lower('The quick Brow Fox'))
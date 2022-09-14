#coding:utf-8
"""
Write a Python program to print the index of the character in a string. Go to the editor
Sample string: w3resource
Expected output:
Current character w position at 0
Current character 3 position at 1
Current character r position at 2
- - - - - - - - - - - - - - - - - - - - - - - - -
Current character c position at 8
Current character e position at 9
"""
str1 = "w3resource"
for index, char in enumerate(str1):
    print("Current character", char, "position at", index )
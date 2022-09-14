#coding:utf-8
"""
Write a Python program to add two given lists using map and lambda. Go to the editor
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]"""
liste1=[1, 2, 3]
liste2=[4, 5, 6]
result=list(map(lambda x,y:x+y, liste1 , liste2 ))
print(result)
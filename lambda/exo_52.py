#coding:utf-8
"""
Write a Python program to remove None value from a given list using lambda function. Go to the editor
Original list:
[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
Remove None value from the said list:
[12, 0, 23, -55, 234, 89, 0, 6, -12]"""
liste=[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
result=list(filter(lambda x:x!=None,liste))
print(result)
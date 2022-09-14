#coding:utf-8
"""Write a Python program to remove specific words from a given list using lambda. Go to the editor
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']
Remove words:
['orange', 'black']
After removing the specified words from the said list:
['red', 'green', 'blue', 'white']"""
liste=['orange', 'red', 'green', 'blue', 'white', 'black']
l1=['orange', 'black']
result=list(filter(lambda x:x not in l1,liste))
print(result)
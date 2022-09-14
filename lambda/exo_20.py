#coding:utf-8
"""
 Write a Python program that multiply each number of given list with a given number using lambda function. Print the result. Go to the editor
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22"""
liste=[2, 4, 6, 9, 11]
n=2
result=list(map(lambda x:x*n,liste))
print(result)
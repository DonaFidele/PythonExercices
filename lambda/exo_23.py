#coding:utf-8
"""Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function. Go to the editor
Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
Sum of the positive numbers: -32
Sum of the negative numbers: 48"""

liste=[2, 4, -6, -9, 11, -12, 14, -5, 17]
positive_rslt=sum(list(filter(lambda x:x>0 , liste)))
negative_rslt=sum(list(filter(lambda x:x<0 , liste)))
print(f"Sum of the positive numbers:{positive_rslt}")
print(f"Sum of the negative numbers:{negative_rslt}")
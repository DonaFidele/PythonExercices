#coding:utf-8
# Write a Python program to listify the list of given strings individually using Python map.
color = ['Red', 'Blue', 'Black', 'White', 'Pink'] 
print(list(map(lambda x:list(x),color)))
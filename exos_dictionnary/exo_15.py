#coding:utf-8
# Write a Python program to get the maximum and minimum value in a dictionary. 

def max_dic(dic):
    return max(dic.values())

def min_dic(dic):
    return min(dic.values())

print( "Max:",max_dic({'x':500, 'y':5874, 'z': 560}))
print("Min:",min_dic({'x':500, 'y':5874, 'z': 560}))

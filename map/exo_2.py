#coding:utf-8
# Write a Python program to add three given lists using Python map and lambda.
a_liste=[1, 2, 3]
b_liste=[2,5,6]
c_liste=[7,8,9]
print(list(map(lambda x,y,z:x+y+z ,a_liste,b_liste,c_liste)))
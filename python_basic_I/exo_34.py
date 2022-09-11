#coding:utf-8
#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 

def sum(x,y):
    if 15<=x+y and x+y<=20:
        return 20
    else :
        return x+y
        
print(sum(15,3))
print(sum(15,-4))

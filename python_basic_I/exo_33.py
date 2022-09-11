#coding:utf-8
#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

def sum(x,y,z):
    liste=[x,y,z]
    if len(set(liste)) <=2:
        return 0
    else :
        return x+y+z

print(sum(1,1,3))
print(sum(2,3,5))
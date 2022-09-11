#coding:utf-8
#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def specified_value(x,y):
    liste=[x,y]
    if x==y or x-y==5:
        return True
    else :
        return False

print(specified_value(5,5))
print(specified_value(10,5))
print(specified_value(3,2))
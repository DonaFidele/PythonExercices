#coding:utf-8
#Write a Python program to print the following floating numbers upto 2 decimal places with a sign.

def test(flt):
    if flt>0:
        return '+'+str(flt).split('.')[0]+'.'+str(flt).split('.')[1][:2]
    return '-'+str(flt).split('.')[0]+'.'+str(flt).split('.')[1][:2]
print(test(3.12345))
print(test(-3.12345))
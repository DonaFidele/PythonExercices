#coding:utf-8
#Write a Python function to find the Max of three numbers.
def max(x,y):
    if x>y:
        return x
    return y
    
print(max(1,max(2,3)))

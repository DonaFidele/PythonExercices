#coding:utf-8
#Write a Python program to multiply all the items in a dictionary. 
def mul_item(dic):
    result=1
    for key in dic:    
        result=result * dic[key]
    return(result)
print(mul_item({1:5,2:5}))


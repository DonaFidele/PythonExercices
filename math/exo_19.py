#coding:utf-8
# Write a Python program to multiply two integers without using the * operator in python.
def multiply(num1,num2):
    if num2==0:
        return 0
    elif num2==1:
        return num1
    else:
        count=0
        result=0
        while count!=num2:
            result+=num1
            count+=1
        return result
    
print(multiply(5,5))
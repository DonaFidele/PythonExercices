#coding:utf-8
#Write a Python program to create a new list taking specific elements from a tuple and convert a string value to integer. 
student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]

print(list(map(lambda x:int(x[2][:-2]),student_data)))

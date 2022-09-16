#coding:utf-8
#Write a Python program to execute a string containing Python code.
code="""
def sum(a_liste):
    the_sum=0
    for i in a_liste:
        the_sum+=i
    return the_sum
    
print(sum([8, 2, 3, 0, 7]))
"""
exec(code)
#coding:utf-8
# Write a Python program to print the following integers with '*' on the right of specified width.

def test(i_nt):
    return str(i_nt)+"*"*len(str(i_nt))
print(test(123))
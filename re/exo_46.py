# Write a Python program to check a decimal with a precision of 2. 
#coding:utf-8
import re
def is_decimal(num):
    regex=re.compile(r'^\d+\.\d{1,2}$')
    result=regex.search(num)
    return bool(result)
print(is_decimal("45.72"))
print(is_decimal(".742"))
print(is_decimal("45.2"))


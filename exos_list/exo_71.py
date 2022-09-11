#coding:utf-8
"""
Write a Python program to check whether all dictionaries in a list are empty or not. 
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
"""
"""def check_dictionaries(liste):
    for dict in liste:
        if len(dict)!=0 :
            return False
    return True

print(check_dictionaries([{},{},{}]))
print(check_dictionaries([{1,2},{},{}]))"""

my_list = [{},{},{}]
my_list1 = [{1:2},{},{}]
print(all(not d for d in my_list))
print(all( not d for d in my_list1))
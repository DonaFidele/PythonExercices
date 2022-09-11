#coding:utf-8
#Write a Python function that takes two lists and returns True if they have at least one common member.

def cmp_list(list1,list2):
    for i in list1:
        if i in list2:
            return True
    return False
print(cmp_list( ['Green', 'White', 'Black'], ['yellow', 'White', 'Black']))
print(cmp_list( ['Green', 'White', 'Black'], ['yellow', 'red', 'blue']))

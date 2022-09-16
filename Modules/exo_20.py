#coding:utf-8
# Write a Python program to create a deep copy of a given dictionary. Use copy.copy
import copy
a_dict={"a":1, "b":2, 'cc':{"c":3}}
dict_copy=copy.deepcopy(a_dict)
a_dict["e"]=5
print(a_dict,dict_copy)
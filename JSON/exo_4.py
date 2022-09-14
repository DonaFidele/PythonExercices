#coding:utf-8
#Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.
import json
JSON_data =  {'4': 5, '6': 7, '1': 3, '2': 4}
Python_object=json.dumps(JSON_data,sort_keys=True,indent=4)
print(Python_object)
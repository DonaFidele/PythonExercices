#coding:utf-8
#Write a Python program to convert JSON data to Python object. 
import json
JSON_data =  '{ "Name":"David", "Class":"I", "Age":6 }'
Python_object=json.loads(JSON_data)
print(Python_object)
print(Python_object["Name"])
#coding:utf-8
# Write a Python program to convert JSON encoded data into Python objects.
import json
JSON_data =   '{"name": "David", "age": 6, "class": "I"}'
Python_object=json.loads(JSON_data)
print(Python_object)
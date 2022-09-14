#coding:utf-8
#Write a Python program to convert Python object to JSON data. 
import json
JSON_data =  {'Name': 'David', 'Class': 'I', 'Age': 6}
Python_object=json.dumps(JSON_data)
print(Python_object)

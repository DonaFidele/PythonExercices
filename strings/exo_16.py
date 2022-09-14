#coding:utf-8
"""
 Write a Python function to insert a string in the middle of a string. Go to the editor
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}"""
def add_tags(str1, str2):
	return str1[:(len(str1)//2)]+str2+str1[(len(str1)//2):]
print(add_tags('[[]]', 'Python'))
print(add_tags('{{}}', 'Python Tutorial'))
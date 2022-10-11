#coding:utf-8
#Write a Python program to split a string at uppercase letters.
import re
text = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', text))
#coding:utf-8
#Write a Python program to insert spaces between words starting with capital letters.
import re
str="PythonExercisesPracticeSolution"
print(re.sub(r"(\w)([A-Z])", r"\1 \2", str))
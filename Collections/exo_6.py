#coding:utf-8
"""Write a Python program that accepts number of subjects, subject names and marks. Input number of subjects and then subject name, marks separated by a space in next line. Print subject name and marks in order of its first occurrence. Go to the editor
Sample Output:
Powered by
Number of subjects: 3
Input Subject name and marks: Bengali 58
Input Subject name and marks: English 62
Input Subject name and marks: Math 68
Bengali 58
English 62
Math 68"""
import collections, re
n = int(input("Number of subjects: "))
item_order = collections.OrderedDict()
for i in range(n):
   sub_marks_list = re.split(r'(\d+)$',input("Input Subject name and marks: ").strip())
   subject_name = sub_marks_list[0]
   item_price = int(sub_marks_list[1])
   if subject_name not in item_order:
       item_order[subject_name]=item_price
   else:
       item_order[subject_name]=item_order[subject_name]+item_price
           
for i in item_order:
   print(i+str(item_order[i]))
#coding:utf-8
""" Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and their values of the said class. Now remove the student_name attribute and display the entire attribute with values. """

class Student:
    student_name='Dona'
    student_id='4125'

Student.student_class='CM1'
for name,value in Student.__dict__.items():
    if not name.startswith("_"):
        print(name ,":",value)
print("\n")
del Student.student_name
for name,value in Student.__dict__.items():
    if not name.startswith("_"):
        print(name ,":",value)

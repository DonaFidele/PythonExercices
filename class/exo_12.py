#coding:utf-8
#Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class. Create a function to display the entire attribute and their values in Student class.

class Student:
    student_name='Dona'
    student_id='4125'

Student.student_class='CM1'

def display():
    for name,value in Student.__dict__.items():
        if not name.startswith("_"):
            print(name ,":",value) 
display()
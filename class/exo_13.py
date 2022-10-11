#coding:utf-8
# Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes. Print all the attributes of student1, student2 instances with their values in the given format.

class Student:
    student_class='CE2'
    student_matiere='7'


student1=Student()
student2=Student()

student1.student_id='456'
student2.student_id='741'

student1.student_name="Dona"
student2.student_name="Fidele"

students = [student1, student2]
def display():
    for student in students:
        print('\n')
        for attr in student.__dict__:
            print(f'{attr} -> {getattr(student, attr)}')

display()

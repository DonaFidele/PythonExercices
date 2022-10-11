#coding:utf-8
"""Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class. """
class Student:
    pass

print(Student.__dict__.keys)
print(Student.__module__)
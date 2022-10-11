#coding:utf-8
#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle. 

class Rectangle:
    def __init__(self):
        self.length=int(input('length :'))
        self.width=int(input('width :'))

    def area(self):
        return self.length*self.width

r1=Rectangle()
print(r1.area())

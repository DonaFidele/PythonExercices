#coding:utf-8
#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. 

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.radius**2*3.14

    def perimeter(self):
        return 2*self.radius*3.14
    
c1 = Circle(5)
print(c1.area())
print(c1.perimeter())

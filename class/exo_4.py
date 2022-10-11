#coding:utf-8
# Write a Python program to create an instance of a specified class and display the namespace of the said instance. 
class Citron:
    def __init__(self,masse,couleur="vert"):
        self.mass=masse
        self.couleur=couleur
    
if __name__=="__main__":
    citron1=Citron(10,"jaune")
    citron2=Citron(5)
    print("citron1:",citron1.__dict__)
    print("citron2:",citron2.__dict__)


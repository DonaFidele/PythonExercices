#coding:utf-8
#Write a Python program to find the size of a singly linked list. 

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,val):
        self.data = val
    def setNext(self,val):
        self.next=val
    
class LinkedList:
    def __init__(self):
        self.head = None
    def IsEmpty(self):
        return self.head is None
    def add(self,item):
        new_node=Node(item)
        new_node.setNext(self.head)
        self.head=new_node
    def FindSize(self):
        self.count=0
        level=self.head
        while level!=None:
            self.count+=1
            level=level.getNext()
        return self.count
    

List=LinkedList()
List.add('f')
List.add('i')
List.add('d')
print(List.FindSize())

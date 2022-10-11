#coding:utf-8
#Write a Python program to set a new value of an item in a singly linked list using index value
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, val):
        self.data = val
    def setNext(self, val):
        self.next = val

class LinkedList:
    def __init__(self):
        self.head = None

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

    def insertValue(self,value,ValueIndex):

        if ValueIndex>self.FindSize()-1:
            raise IndexError
        level=self.head
        preced=None
        index=0
        if ValueIndex==0:
            self.add(ValueIndex)
        else:
            new_node=Node(value)
            while index < ValueIndex:
                index+=1
                preced=level
                level=level.getNext()
            preced.setNext(new_node)
            new_node.setNext(level)

            
    def printList(self):
        """Print the list"""
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()

List=LinkedList()
List.add('print')
List.add("python")
List.add("input")

List.printList()
print('\n')
List.insertValue("return",1)
List.printList()
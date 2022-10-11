#coding:utf-8
#Write a Python program to access a specific item in a singly linked list using index value.

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
        self.head=None

    def add(self,item):
        new_node=Node(item)
        new_node.setNext(self.head)
        self.head=new_node

    def isEmpty(self):
        """Check if the list is empty"""
        return self.head is None

    def searchItem(self,item):
        level=self.head
        while level!=None:
            if level.getData()==item:
                return True
            level=level.getNext()
        return False

    def getIndex(self,item):
        
        if self.isEmpty() == True:
            index="List Empty"
        else:
            index=-1
        level=self.head
        while level!=None:
            index+=1
            if self.searchItem(item)==False:
                return "not found"
            elif level.getData()==item:
                return index
            level=level.getNext()
        return index

List=LinkedList()
List.add('print')
List.add("python")
List.add("input")

print(List.getIndex("print"))
print(List.getIndex('python'))
print(List.getIndex("input"))
print(List.getIndex("return"))

#coding:utf-8
#Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false.

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,val):
        self.data=val
    def setNext(self,val):
        self.next=val

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,item):
        new_node=Node(item)
        new_node.setNext(self.head)
        self.head=new_node

    def searchItem(self,item):
        level=self.head
        while level!=None:
            if level.getData()==item:
                return True
            level=level.getNext()
        return False
            


List=LinkedList()
List.add('print')
List.add("python")

print(List.searchItem("python"))
print(List.searchItem('gow'))
            
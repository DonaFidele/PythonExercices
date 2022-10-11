#coding:utf-8
#Write a Python program to delete the first item from a singly linked list. 

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
    def isEmpty(self):
        """Check if the list is empty"""
        return self.head is None
    def add(self, item):
        """Add the item to the list"""
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node

    def pop(self):
        level=self.head
        new_head=level.getNext()
        new_next=new_head.getNext()
        level=level.setData(new_head)
        del level
        
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
List.add("While")

List.printList()
print('\n')

List.pop()
List.printList()
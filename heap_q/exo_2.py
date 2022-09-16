#coding:utf-8
#Write a Python program to find the three smallest integers from a given list of numbers using Heap queue algorithm. 
import heapq
a_liste=[100,5,48,-9,45,27,19,-7521,35]
print(heapq.nsmallest(3,a_liste))
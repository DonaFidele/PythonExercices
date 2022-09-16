#coding:utf-8
# Write a Python function which accepts an arbitrary list and converts it to a heap using Heap queue algorithm. 
import heapq
def test(a_liste):
    heapq.heapify(a_liste)
    return a_liste
print(test([50,-5,1,2,3,4,56]))
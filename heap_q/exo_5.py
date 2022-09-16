#coding:utf-8
#Write a Python program to delete the smallest element from the given Heap and then inserts a new item. 
import heapq
def test(a_liste):
    heapq.heapify(a_liste)
    heapq.heappop(a_liste)
    return a_liste
print(test([50,-5,1,2,3,4,56]))
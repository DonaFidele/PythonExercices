#coding:utf-8
#Write a Python program to sort a given list of elements in ascending order using Heap queue algorithm. 

import heapq
def test(a_liste):
    return heapq.nsmallest(len(a_liste),a_liste)
print(test([50,-5,1,2,3,4,56]))
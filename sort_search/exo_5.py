#coding:utf-8
"""Write a Python program to sort a list of elements using the selection sort algorithm. Go to the editor
Note : The selection sort improves on the bubble sort by making only one exchange for every pass through the list. 
Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]"""
def selectionSort(nlist):
   for fillslot in range(len(nlist)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if nlist[location]>nlist[maxpos]:
               maxpos = location

       temp = nlist[fillslot]
       nlist[fillslot] = nlist[maxpos]
       nlist[maxpos] = temp

nlist = [14,46,43,27,57,41,45,21,70]
selectionSort(nlist)
print(nlist)

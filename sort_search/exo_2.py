#coding:utf-8
"""Write a Python program for sequential search. Go to the editor
Sequential Search : In computer science, linear search or sequential search is a method for finding a particular value in a list that checks each element in sequence until the desired element is found or the list is exhausted. The list need not be ordered.
Test Data :
Sequential_Search([11,23,58,31,56,77,43,12,65,19],31) -> (True, 3)"""
def research_item(a_list,item):
    found=False
    count=-1
    for i in a_list:
        count+=1
        if i==item:
            found=True
            return found,count
    return found
print(research_item([11,23,58,31,56,77,43,12,65,19],31))
print(research_item([11,23,58,31,56,77,43,12,65,19],-31))
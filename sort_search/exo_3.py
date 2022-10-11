#coding:utf-8
"""Write a Python program for binary search for an ordered list. Go to the editor
Test Data :
Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3) -> True
Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17) -> False"""
def research_item(a_list,item):
    found=False
    for i in a_list:
        if i==item:
            found=True
    return found
print(research_item([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
print(research_item([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))
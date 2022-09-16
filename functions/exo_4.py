#coding:utf-8
"""Write a Python program to reverse a string. Go to the editor
Sample String : "1234abcd"
Expected Output : "dcba4321"""
def reverse(str):
    l=[]
    for i in str:
        l.append(i)
    return ''.join(l)[::-1]
    
print(reverse("1234abcd"))
#coding:utf-8
"""Write a Python program to detect the number of local variables declared in a function. Go to the editor
Sample Output:
3"""
def sum(a_liste):
    the_sum=0
    for i in a_liste:
        the_sum+=i
    return the_sum
    
print(sum.__code__.co_nlocals)

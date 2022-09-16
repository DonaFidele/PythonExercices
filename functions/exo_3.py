#coding:utf-8
"""Write a Python function to multiply all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336"""
def mul(a_liste):
    the_mul=1
    for i in a_liste:
        the_mul*=i
    return the_mul
    
print(mul([8, 2, 3, -1, 7]))
#coding:utf-8
"""Write a Python function to sum all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20"""
def sum(a_liste):
    the_sum=0
    for i in a_liste:
        the_sum+=i
    return the_sum
    
print(sum([8, 2, 3, 0, 7]))

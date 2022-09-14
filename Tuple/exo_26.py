#coding:utf-8
"""Write a Python program calculate the product, multiplying all the numbers of a given tuple. Go to the editor
Original Tuple:
(4, 3, 2, 2, -1, 18)
Product - multiplying all the numbers of the said tuple: -864
Original Tuple:
(2, 4, 8, 8, 3, 2, 9)
Product - multiplying all the numbers of the said tuple: 27648
"""

def mutiple_tuple(nums):
    temp = list(nums)
    product = 1 
    for x in temp:
        product *= x
    return product

nums = (4, 3, 2, 2, -1, 18)
print ("Original Tuple: ")
print(nums)
print("Product - multiplying all the numbers of the said tuple:",mutiple_tuple(nums))

nums = (2, 4, 8, 8, 3, 2, 9)
print ("\nOriginal Tuple: ")
print(nums)
print("Product - multiplying all the numbers of the said tuple:",mutiple_tuple(nums))
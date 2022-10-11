#coding:utf-8
"""Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
Note: There will be one solution for each input and do not use the same element twice. Go to the editor
Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4

"""
class Pair:
    def findPair(self,target,numbers):
        dict={}
        for k,v in enumerate(numbers):
            if target-v in dict:
                return (dict[target-v],k)
            dict[v]=k 

print(Pair().findPair(50,(10,20,10,40,50,60,70)))
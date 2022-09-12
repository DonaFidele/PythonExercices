#coding:utf-8
"""
Write a Python program to find the list of strings that has fewer total characters (including repetitions). Go to the editor
Input:
[['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
Output:
['this', 'list', 'is', 'narrow']
Input:
[['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
Output:
['Red', 'Black', 'Pink']
"""

def test(strs):
    return min(strs, key=lambda x: sum(len(i) for i in x))

print(test([['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]))
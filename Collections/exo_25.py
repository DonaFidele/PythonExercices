#coding:utf-8
"""Write a Python program to find the characters in a list of strings which occur more than and less than a given number. Go to the editor
Sample Output:
Original list:
['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
Characters of the said list of strings which occur more than: 3
['a', 'd', 'f']
Characters of the said list of strings which occur less than: 3
['c', 'b', 'h', 'e', 'i', 's', 'l', 'k', 'j', 'g']"""
from collections import Counter
from itertools import chain 
N=3
a_liste=['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
temp=[set(i) for i in a_liste]
counts = Counter(chain.from_iterable(temp)) 
gt_N =  [chr for chr, count in counts.items() if count > N]
lt_N =  [chr for chr, count in counts.items() if count < N]
print(gt_N, lt_N)
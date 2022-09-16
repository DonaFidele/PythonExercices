#coding:utf-8
"""Write a Python program to get the frequency of the elements in a given list of lists. Use collections module. Go to the editor
Sample Output:
Original list of lists:
[[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
Frequency of the elements in the said list of lists:
Counter({2: 3, 1: 2, 5: 2, 3: 1, 4: 1, 6: 1, 7: 1, 9: 1})"""

from collections import Counter,defaultdict
from itertools import chain 
a_liste=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
counts=Counter(chain.from_iterable(a_liste))
print(counts)

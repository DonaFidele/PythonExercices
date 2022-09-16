#coding:utf-8
"""Write a Python program to get the frequency of the tuples in a given list. Go to the editor
Sample Output:
Original list of tuples:
[(['1', '4'], ['4', '1'], ['3', '4'], ['2', '7'], ['6', '8'], ['5', '8'], ['6', '8'], ['5', '7'], ['2', '7'])]
Tuples frequency
('1', '4') 2
('3', '4') 1
('2', '7') 2
('6', '8') 2
('5', '8') 1
('5', '7') 1"""
from collections import Counter
Original_list=[(['1', '4'], ['4', '1'], ['3', '4'], ['2', '7'], ['6', '8'], ['5', '8'], ['6', '8'], ['5', '7'], ['2', '7'])]
a=Counter(tuple(sorted(i)) for i in Original_list[0])
for key,val in a.items():
    print(key," ", val)
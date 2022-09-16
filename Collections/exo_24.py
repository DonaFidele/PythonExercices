#coding:utf-8
"""Write a Python program to calculate the maximum aggregate from the list of tuples (pairs). Go to the editor
Sample Output:
Original list:
[('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]
Maximum aggregate value of the said list of tuple pair:
('Juan Whelan', 212)"""
from collections import defaultdict
a_liste=[('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]
dict_words=defaultdict(int)
for x,y in a_liste:
    dict_words[x]+=y
print(max(dict_words.items(),key=lambda x:x[1]))
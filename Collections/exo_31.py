#coding:utf-8
"""Write a Python program to count the most common words in a dictionary. Go to the editor
Sample Output:
[('pink', 6), ('black', 5), ('white', 5), ('red', 4)]"""
from collections import Counter
def count_occurrence(liste):
    return Counter(liste).most_common(4)

print(count_occurrence([
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red']))

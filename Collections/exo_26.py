#coding:utf-8
"""Write a Python program to find the difference between two list including duplicate elements. Use collections module. Go to the editor
Sample Output:
Original lists:
[3, 3, 4, 7]"""
from collections import Counter
l1 = [1,1,2,3,3,4,4,5,6,7]
l2 = [1,1,2,4,5,6]
print("Original lists:")
c1 = Counter(l1)
c2 = Counter(l2)
diff = c1-c2
print(list(diff.elements()))
#coding:utf-8
"""Write a Python program to copy of a deque object and verify the shallow copying process. Go to the editor
Sample Output:
Content of dq1:
deque([1, 3, 5, 7, 9])
dq2 id:
140706429557152
Content of dq2:
deque([1, 3, 5, 7, 9])
dq2 id:
140706406914152
Checking the first element of dq1 and dq2 are shallow copies:
11065888
11065888"""

import collections
tup1 = (1,3,5,7,9)
dq1 = collections.deque(tup1)
dq2 = dq1.copy()
print("Content of dq1:")
print(dq1)
print("dq2 id:")
print(id(dq1))
print("\nContent of dq2:")
print(dq2)
print("dq2 id:")
print(id(dq2))
print("\nChecking the first element of dq1 and dq2 are shallow copies:")
print(id(dq1[0]))
print(id(dq2[0]))
#coding:utf-8
"""
Write a Python program to print the first n Lucky Numbers. Go to the editor
Lucky numbers are defined via a sieve as follows.
Begin with a list of integers starting with 1 :
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, . . . .
Now eliminate every second number :
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, ...
The second remaining number is 3, so remove every 3rd number:
1, 3, 7, 9, 13, 15, 19, 21, 25, ...
The next remaining number is 7, so remove every 7th number:
1, 3, 7, 9, 13, 15, 21, 25, ...
Next, remove every 9th number and so on.
Finally, the resulting sequence is the lucky numbers.
"""
n=int(input("Input a Number: "))
List=range(-1,n*n+9,2)
i=2
while List[i:]:List=sorted(set(List)-set(List[List[i]::List[i]]));i+=1
print(List[1:n+1])
#coding:utf-8
"""
Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
"""
def sum(nbre1,nbre2,nbre3):
    if nbre1==nbre2==nbre3:
        return (nbre3+nbre2+nbre1)*3
    else:
        return nbre3+nbre2+nbre1

print(sum(2,5,3))
print(sum(2,2,2))
#coding:utf-8
# Write a Python class to implement pow(x, n).

class Pow:
    def pow(self,x,n):
        p=1
        for i in range(n):
            p*=x
        return p

print(Pow().pow(2,3))
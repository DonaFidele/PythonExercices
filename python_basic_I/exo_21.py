#coding:utf-8
# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user. 

def parity(nbre):
    if nbre%2==0:
        return True

nbre=int(input("Enter the number: "))
if parity(nbre):
    print("Ce nombre est paire")
else:
    print("Ce nombre est impaire")
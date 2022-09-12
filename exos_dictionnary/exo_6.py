#coding:utf-8
"""
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
def generate_dic(n):
    dic={}
    for k in range(1,n+1):
        dic[k]=k*k
    return dic

print(generate_dic(5))
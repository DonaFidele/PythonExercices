#coding:utf-8
"""
 Write a Python program for nth Catalan Number. Go to the editor
In combinatorial mathematics, the Catalan numbers form a sequence of natural numbers that occur in various counting problems, often involving recursively-defined objects. They are named after the Belgian mathematician Eugène Charles Catalan (1814 –1894).
"""

def catalan_number(num):
    if num <=1:
         return 1
   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num
 
for n in range(10):
    print(catalan_number(n))
	
#coding:utf-8
"""
Write a Python program to round a specified decimal by setting precision (between 1 and 4). Go to the editor

Sample Number : 0.26598
Original Number : 0.26598
Precision- 1 : 0.3
Precision- 2 : 0.27
Precision- 3 : 0.266
Precision- 4 : 0.2660

Expected Output :

Original Number :  0.26598                                                       
Precision- 1 : 0.3                                                               
Precision- 2 : 0.27                                                              
Precision- 3 : 0.266                                                             
Precision- 4 : 0.2660
"""
import decimal
d = decimal.Decimal('00.26598')
print("Original Number : ",d)
for i in range(1, 5):
    decimal.getcontext().prec = i
    print("Precision-",i, ':', d * 1)
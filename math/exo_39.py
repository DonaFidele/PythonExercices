#coding:utf-8
"""
Write a Python program to retrieve the current global context (public properties) for all decimal. Go to the editor

Expected Output :

Emax     = 999999                                                                
Emin     = -999999                                                               
capitals = 1                                                                  
prec     = 28                                                                  
rounding = ROUND_HALF_EVEN                                                       
flags    = <class 'decimal.InvalidOperation'>: False  
........
"""

import decimal
context = decimal.getcontext()
print('Emax     =', context.Emax)
print('Emin     =', context.Emin)
print('capitals =', context.capitals)
print('prec     =', context.prec)
print('rounding =', context.rounding)
print('flags    =')
for x, y in context.flags.items():
    print('  {}: {}'.format(x, y))
print('traps    =')
for x, y in context.traps.items():
    print('  {}: {}'.format(x, y))

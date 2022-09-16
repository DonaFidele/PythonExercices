#coding:utf-8
#Write a Python program to configure the rounding to round up and round down a given decimal value. Use decimal.Decimal
import decimal
print(decimal.Decimal('8.325').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_UP))
print(decimal.Decimal('8.325').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN))
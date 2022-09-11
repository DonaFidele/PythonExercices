#coding:utf-8
"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
from datetime import datetime
date1=datetime (2014, 5, 1)
date2=datetime (2014, 7, 11)
nbre_jours=date2-date1
print(nbre_jours.days)
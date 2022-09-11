#coding:utf-8
"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""
import calendar
month=int(input("Month:"))
year=int(input("Year: "))

print(calendar.month(year,month))


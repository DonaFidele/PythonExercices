#coding:utf-8
#Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
import re
def date_format(date):
    return re.sub(r'([0-9]{4})-(\d{1,2})-(\d{1,2})','\\3-\\2-\\1',date)
print(date_format("2022-10-19"))

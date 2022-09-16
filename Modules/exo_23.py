#coding:utf-8
#Write a Python program to parse a given CSV string and get the list of lists of string values. Use csv.reader
import csv
csv_string = """1,2,3
4,5,6
7,8,9
"""
print(csv_string)
lines = csv_string.splitlines()
print(lines)
reader = csv.reader(lines)
parsed_csv = list(reader)
print(parsed_csv)
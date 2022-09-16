#coding:utf-8
#Write a Python program to count the number of lines in a given CSV file. Use csv.reader
import csv
reader = csv.reader(open("exo_1.py"))
no_lines= len(list(reader))
print(no_lines)

#coding:utf-8
#Write a Python program to read the current line from a given CSV file. Use csv.reader
import csv
f = open("exo_1.py", newline='')
csv_reader = csv.reader(f)
print(next(csv_reader))
print(next(csv_reader))
print(next(csv_reader))


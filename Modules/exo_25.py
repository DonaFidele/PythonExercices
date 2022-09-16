#coding:utf-8
#Write a Python program to skip the headers of a given CSV file. Use csv.reader
import csv
f = open("exo_1.py", "r")
reader = csv.reader(f)
next(reader)

for row in reader:
    print(row)
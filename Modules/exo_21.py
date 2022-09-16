#coding:utf-8
#Write a Python program to read and display the content of a given CSV file. Use csv.reader
import csv
import csv
csv_string = """1,2,3
4,5,6
7,8,9
"""
print("Original string:")
print(csv_string)
lines = csv_string.splitlines()
print("List of CSV formatted strings:")
print(lines)
reader = csv.reader(lines)
parsed_csv = list(reader)
print("\nList representation of the CSV file:")
print(parsed_csv)
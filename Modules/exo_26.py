#coding:utf-8
#Write a Python program to write (without writing separate lines between rows) and read a CSV file with specified delimiter. Use csv.reader
import csv     
fw = open("test.csv", "w", newline='')
writer = csv.writer(fw, delimiter = ",")
writer.writerow(["a","b","c"])
writer.writerow(["d","e","f"])
writer.writerow(["g","h","i"])
fw.close()
 
fr = open("test.csv", "r")
csv = csv.reader(fr, delimiter = ",")
for row in csv:
  print(row) 
fr.close()
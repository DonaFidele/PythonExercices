#coding:utf-8
#Write a Python program to combine each line from first file with the corresponding line in second file.
with open("file",'r') as f:
    w=f.readlines()

with open("fileCopy",'r') as f1:
    w1=f1.readlines()

with open("file2",'w') as f2:
    [f2.write(l1+l2) for l1 in w for l2 in w1 ]
#coding:utf-8
"""
Write a Python script to concatenate following dictionaries to create a new one. 

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
new_dic={}
for dics in (dic1,dic2,dic3):
    new_dic.update(dics)
print(new_dic)
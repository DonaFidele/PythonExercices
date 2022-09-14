#coding:utf-8
""" Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. Go to the editor
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]"""
def test(str1, sub_str):
    result = list(filter(lambda x: sub_str in x, str1))
    return result

print(test(['red', 'black', 'white', 'green', 'orange'],"ack"))
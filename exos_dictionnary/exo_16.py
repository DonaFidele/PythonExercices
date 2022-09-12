#coding:utf-8
#Write a Python program to get a dictionary from an object's fields.

class dic_object(object):
    def __init__(self):
        self.k1 = 'val1'
        self.k2 = 'val2'
        self.k3 = 'val3'
     
get_dic = dic_object()
print(get_dic.__dict__)
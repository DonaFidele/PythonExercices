#coding:utf-8
#Write a Python program to map two lists into a dictionary. 

def map_lists(k_list,v_list):
    return dict(zip(k_list,v_list))

print(map_lists(['red', 'green', 'blue'],['#FF0000','#008000', '#0000FF']))
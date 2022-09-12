#codinf:utf-8
"""
 Write a Python script to add a key to a dictionary. 

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""
dict={0: 10, 1: 20}
dict.update({max(dict.keys())+1:sum(x for x in dict.values())})
print(dict)
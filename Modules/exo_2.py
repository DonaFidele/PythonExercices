#coding:utf-8
"""
Write a Python program to select a random element from a list, set, dictionary (value) and a file from a directory. Use random.choice()
"""
import random
a_liste=[1, 2, 3, 4, 5]
a_set={1,2,3,4,5,6,}
a_dict={"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(random.choice(a_liste))
print(random.choice(list(a_set)))
print(random.choice(tuple(a_set)))
print(a_dict[random.choice(list(a_dict))])


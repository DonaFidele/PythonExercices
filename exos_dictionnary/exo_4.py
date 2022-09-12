#ccoding:utf-8
# Write a Python script to check whether a given key already exists in a dictionary. 

def check_key(dic,key):
    return key in dic.keys()

print(check_key({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},2))
print(check_key({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},20))
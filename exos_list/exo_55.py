#coding:utf-8
#Write a Python program to remove key values pairs from a list of dictionaries.

def remove_key(liste):
    new_liste=[{k:v for k,v in dict.items() if k!='key1'}for dict in liste]
    return new_liste

print(remove_key([{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]))



#autre modifdff






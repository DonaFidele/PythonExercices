#coding:utf-8
#Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function. 
chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print(set(list(map(lambda x:(x.upper(),x.lower()),chrars))))

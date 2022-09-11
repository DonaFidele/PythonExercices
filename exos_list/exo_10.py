#coding:utf-8
# Write a Python program to find the list of words that are longer than n from a given list of words.

def len_word(liste,n):
    words_list=[]
    for i in liste:
        if len(i)>n:
            words_list.append(i)
    return words_list

print(len_word( ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],4))
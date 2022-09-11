#coding:utf-8
#Write a Python program to get the frequency of the elements in a list

def frequency_of_elements(liste):
    for element in set(liste):
        print( f"{element}: {liste.count(element)}")

frequency_of_elements(['Green', 'White', 'Black','Black'])
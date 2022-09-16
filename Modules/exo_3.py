#coding:utf-8
#Write a Python program to generate a random alphabetical character, alphabetical string and alphabetical string of a fixed length. Use random.choice()
import random,string
print(f"random alphabetical character : {random.choice(string.ascii_letters)}")
print(f"alphabetical string :{''.join([random.choice(string.ascii_letters) for i in range(random.randint(1,50))])}")
print(f"alphabetical string :{''.join([random.choice(string.ascii_letters) for i in range(5)])}")
#coding:utf-8
"""
Write a Python program to generate a random integer between 0 and 6 - excluding 6, random integer between 5 and 10 - excluding 10, random integer between 0 and 10, with a step of 3 and random date between two dates. Use random.randrange()"""
import random,datetime
print(random.randrange(5))
print(random.randrange(5,10))
print(random.randrange(0,10,3))
start_dt=datetime.date(2002,5,29)
end_dt=datetime.date(2022,11,15)
time_between_dates = end_dt - start_dt
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_dt + datetime.timedelta(days=random_number_of_days)
print(random_date)
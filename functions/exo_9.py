#coding:utf-8
"""Write a Python function that takes a number as a parameter and check the number is prime or not. Go to the editor
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself."""
def prime_or_not(num):
    for i in range(2,num):
        if num%i==0:
            return " prime"
        return "not prime"
print(prime_or_not(100))
print(prime_or_not(13))
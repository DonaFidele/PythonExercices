#coding:utf-8
"""
Write a Python program to print all primes (Sieve_of_Eratosthenes) smaller than or equal to a specified number. Go to the editor
In mathematics, the sieve of Eratosthenes, one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit. It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the multiples of 2.
"""
def sieve_of_Eratosthenes(num):
    limitn = num+1
    not_prime_num = set()
    prime_nums = []

    for i in range(2, limitn):
        if i in not_prime_num:
            continue

        for f in range(i*2, limitn, i):
            not_prime_num.add(f)

        prime_nums.append(i)

    return prime_nums

print(sieve_of_Eratosthenes(100));

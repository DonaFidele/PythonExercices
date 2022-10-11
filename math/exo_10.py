#coding:utf-8
"""
Write a Python program to find the smallest multiple of the first n numbers. Also, display the factors. Go to the editor
Test Data:
If n = (13)
Expected Output :
[13, 12, 11, 10, 9, 8, 7]
360360"""
def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    print(factors)

    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i
                
print(smallest_multiple(13))
print(smallest_multiple(11))
print(smallest_multiple(2))
print(smallest_multiple(1))
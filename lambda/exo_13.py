#coding:utf-8
"""
Write a Python program to count the even, odd numbers in a given array of integers using Lambda. Go to the editor
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5
"""
def test(liste):
    return f"Even numbers from the said list: {len(list(filter(lambda x: x%2==0,liste )))}\nOdd numbers from the said list: {len(list(filter(lambda x: x%2!=0,liste )))}"

print(test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
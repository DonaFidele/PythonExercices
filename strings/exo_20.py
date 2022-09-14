#coding:utf-8
# Write a Python function to reverses a string if it's length is a multiple of 4.

def test(str):
    if len(str)%4==0:
        return str[::-1]

print(test('blue'))
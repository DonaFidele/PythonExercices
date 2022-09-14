#coding:utf-8
""" Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. """
def test(str):
    count=0
    for i in str[:4]:
        if i.isupper():
            count+=1
    if count>=2:
        return str.upper()


print(test('BLue'))
print(test('blue'))
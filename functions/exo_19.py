#coding:utf-8
#Write a Python program to access a function inside a function. 
def test(the_sum):
    def sum(a_liste):
        nonlocal the_sum
        for i in a_liste:
            the_sum+=i
        return the_sum
    return sum

func=test(0)
print(func([8, 2, 3, 0, 7]))
#coding:utf-8
#Write a Python program to compute the greatest common divisor (GCD) of two positive integers

def pgcd(nbre1,nbre2):
    rest=nbre1%nbre2
    if rest==0:
        rest_copy=rest
        return rest
    else:
        rest=nbre2%rest

print(pgcd(126,90))i_i__çç,:m!ùµ

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 20:52:07 2023

@author: HP
"""
def factorial(n):
    if n==0:
        return 1
    else:
        fact=n*factorial(n-1)
        return fact
num=int(input('Enter Number:'))
ans=factorial(num)
print('Factorial=',ans)
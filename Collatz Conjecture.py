# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:00:03 2023
@author: HP
"""
#Collatz Conjecture
def checkNum(num):
    iterations=1
    while num!=1:
        if num%2==0:
            num=num//2
        else:
            num=3*num+1
        iterations+=1
        print(num,iterations)

checkNum(22)

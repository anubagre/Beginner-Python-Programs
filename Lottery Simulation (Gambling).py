# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:12:40 2023

@author: HP
"""

#Lottery Simulation (Gambling)
import random as r
amt=0
while True:
    num=int(input('Enter Number of Your Choice(1-10):'))
    l_no=r.randint(1,10)
    print('Card picked:',l_no)
    if l_no==num:
        amt+=1000
    else:
        amt+=(-100)
    print('Amount=',amt)
    ch=input('Wanna Continue(Y/N):')
    if ch.upper()=='N':
        break
    else:
        continue
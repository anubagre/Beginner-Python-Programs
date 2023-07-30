# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 09:08:22 2023

@author: HP
"""
#Monte Hall Game
import random as r
while True:
    doors=[0,0,0]
    pos1=r.randint(0,2)
    doors[pos1]='Treasure'
    inp1=int(input("Enter the number of door with treasure(1/2/3):"))
    while True:
        pos2=r.randint(0,2)
        if pos2!=inp1 and doors[pos2]==0:
            print("Opened door",pos2+1,"and found it empty")
        ch=input("Wanna swap(Y/N)?")
        if ch.upper()=="Y":
            for i in range(3):
                if i!=inp1 and i!=pos2:
                    inp2=i
            if doors[inp2-1]=='Treasure':
                print('You found the Treasure.')
                break
            else:
                print("Treasure was in door",pos1+1)
                break
        else:
            if doors[inp1-1]=='Treasure':
                print('You found the Treasure in box',pos1+1)
                break
            else:
                print("Treasure was in door",pos1+1)
                break
    choice=input("Wanna Continue(Y/N)?")
    if choice.upper()!='Y':
        break
    
    
    
    
    
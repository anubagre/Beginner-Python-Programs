# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 13:48:24 2023

@author: HP
"""

#Bubble Sort
def bubble_sort(nlist):
    n=len(nlist)
    for x in range(n):
        for y in range(0,n-x-1):
            if nlist[y]>nlist[y+1]:
                nlist[y],nlist[y+1]=nlist[y+1],nlist[y]
    print(nlist)
list1=[88,3,56,1,7]
bubble_sort(list1)
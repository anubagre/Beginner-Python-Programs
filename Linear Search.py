# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 14:52:30 2023

@author: HP
"""

#Linear Search
def lsearch(nlist,x):
    flag=0
    for elem in nlist:
        if elem==x:
            print('Found at', nlist.index(elem))
            flag=1
    if flag==0:
        print('Not in List')
list1=[2,34,56,78,23,12]
lsearch(list1,34)
    
            
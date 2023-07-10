# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:02:36 2023
@author: HP
"""
#Generating 50 random Birthday Dates
import datetime
import random
for i in range(51):
    year=random.randint(1900,2022) #122 is maximum age
    month=random.randint(1,12)
    if (((year%4==0 and year%100!=0) or year%400==0) and month==2):
        day=random.randint(1,29)
    elif month in [1,3,5,7,8,10,12]:
        day=random.randint(1,31)
    elif month in [4,6,9,11]:
        day=random.randint(1,30)
    else:
        day=random.randint(1,28)
    dd=datetime.date(year,month,day)
    print(dd)        
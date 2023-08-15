 # -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 22:11:04 2023
@author: HP
"""
#FLAMES

#taking input
n1=list(input('Enter name 1:'))
n2=list(input('Enter name 2:'))

#removing common letters
for i in range(len(n1)):
    for x in n1:
        for y in n2:
            if x.lower()==y.lower():
                print(x,y)
                n1.remove(x)
                n2.remove(y)
                break

#determining count of remaing letters
num=len(n1)+len(n2)
print(num)

#creating list out of flames
l=list('FLAMES')
print(l)
result={'F':'Friendship','L':'Love','A':'Affection','M':'Marriage','E':'Enemy','S':'Siblings'}

#determining relationship
while len(l)>1:
    split_index=(num%len(l))-1
    if split_index>=0:
        right=l[split_index+1:] 
        left=l[:split_index]
        l=right+left
    else:
        l=l[:len(l)-1]

#printing result
print('Your Relation will end in',result[(l[0])])

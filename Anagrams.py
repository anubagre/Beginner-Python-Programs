# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:18:43 2023
@author: HP
"""

#Anagrams
s1=input('Enter String 1:')
s2=input('Enter String 2:')
print(sorted(s1),'\n',sorted(s2))
if sorted(s1)==sorted(s2):
    print('These are anagrams')
else:
    print('These are not anagrams')
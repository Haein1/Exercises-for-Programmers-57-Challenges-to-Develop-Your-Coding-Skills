# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:41:59 2021

@author: Administrator
"""

names = ['A', 'B', 'C', 'D']
heros = ['a', 'b', 'c', 'd']

# my_dict = {}
# for names, heros in zip(names, heros):
#     my_dict[names] = heros
    
# print(my_dict)

#using dict comprehension
my_dict = {name:hero for name,hero in zip(names, heros) if name != 'D' }
print(my_dict)
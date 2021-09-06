# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:42:25 2021

@author: Administrator
"""


'''
List comprehension: []
Dict comprehension:{}
Set comprehension: {}
generator comprehension:()


'''
nums = [1, 1, 2, 3, 5, 5]

# my_set = set()

# for n in nums:
#     my_set.add(n)
    
# print(my_set)

my_set = {n for n in nums}
print(my_set)
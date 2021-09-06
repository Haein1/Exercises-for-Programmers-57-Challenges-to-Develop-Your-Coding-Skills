# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 13:18:17 2021

@author: Administrator
"""

'''
List: [1, 2, "a", 3.14]

List comprehension:
    [expr for val in collection]
    
    [expr for val in collection if <test1>]
    
    [expr for val in collection if <test1> and <test2>]
    
    [expr for val1 in collection1 for val2 in collection2 ]
    
    


'''

#1.
print("using the normal list")
squares = []
for i in range(0, 101):
    squares.append(i ** 2)
    
print(squares)

print("using list comprehenison to achieve the same function")
squares1 = [i ** 2 for i in range(0, 101) if i % 2 ==0]
print(squares1)

#2.
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)




# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 11:36:26 2021

@author: Administrator
"""

'''
keyword: yield
its function is similar to return
but the difference between them is 
    that "yield" stores the first value, then stop execution
    
    when it meets the command next time, 
    "yield" stores the next value, then pause
    
the biggest advantage is that generator saves much more memory than normal function
'''
#1.
def odds(start, stop):
    for odd in range(start, stop+1, 2):
        yield odd
        #this keyword yield indicates that this is a generator rather than a function
        
g = odds(3, 15)
print(g)

#2. change the following list into generator by raplacing square bracket with paratheses
squares1 = []
print(squares1)

#3. generator comprehension
squars2 = (i ** 2 for i in range(0, 101))
print(squars2)
print(next(squars2))


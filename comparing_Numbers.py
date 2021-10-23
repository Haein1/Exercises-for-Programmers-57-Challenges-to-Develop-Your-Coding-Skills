# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:03:23 2021

@author: Administrator
"""

'''Comparing one input to a known value is common enough,
but you’ll often need to process a collection of inputs.


Write a program that asks for three numbers. Check first to
see that all numbers are different. If they’re not different,
then exit the program. Otherwise, display the largest number
of the three


Example Output
    Enter the first number: 1
    Enter the second number: 51
    Enter the third number: 2
    The largest number is 51.
'''

# find the largest number and print it
def max(num1, num2, num3):
    
    max = num1
    
    if (num1 != num2) and (num1 != num3) and (num2 != num3):
        if num2 > max:
            max = num2
        elif num3 > max:
            max = num3
    
    else:
    #google how to make python program exit
        exit()
    #if these three numbers are not different, then force the program to stop execute
    
    print('The largest number is {}.'.format(max))


num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')
num3 = input('Enter the third number: ')
max(num1, num2, num3)
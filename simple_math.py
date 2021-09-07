# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:28:36 2021

@author: Administrator
"""

'''
(STEP ONE: a clear problem statement):
Write a program that prompts for two numbers. Print the
sum, difference, product, and quotient of those numbers as
shown in the example output:
    Example Output:
    What is the first number? 10
    What is the second number? 5
    10 + 5 = 15
    10 - 5 = 5
    10 * 5 = 50
    10 / 5 = 2
    
(STEP TWO: input, output, process):
    input: two numbers
    
    process: 
        1. prompt for num1 with "What is the first number? "
        2. prompt for num2 with "What is the second number? "
        3. display: 
            10 + 5 = 15
            10 - 5 = 5
            10 * 5 = 50
            10 / 5 = 2
    
            
        
    Example Output:
        What is the first number? 10
        What is the second number? 5
        10 + 5 = 15
        10 - 5 = 5
        10 * 5 = 50
        10 / 5 = 2
 
(STEP THREE: DESIGN AT LEAST FOUR TEST):
    test 1: for testing the normal occasion
        input:  
            1. for num1 : 10
            2. for num2: 5
            
(STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE
    

'''

#1. initialize num1 to an input function
# prompt for num1 with "What is the first number? "
# convert it to numbers
num1 = int(input("What is the first number? "))

#2. initialize num2 to an input function
# prompt for num2 with "What is the second number? "
# convert it to numbers
num2 = int(input("What is the second number? "))
#display:
    # "{num1} + {num2} = {num1+num2}".format(num1 = num1, num2 = num2)\n"{num1} - {num2} = {num1+num2}.format(num1, num2)
print("{num1} + {num2} = {add}\n{num1} - {num2} = {minus}\n{num1} * {num2} = {multiply}\n{num1} / {num2} = {division}".format(num1 = num1, num2 = num2, add = num1+num2, minus = num1-num2, multiply = num1*num2, division = num1/num2))








# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 21:11:53 2021

@author: Administrator
"""

'''(STEP ONE: a clear problem statement):
    Write a program that converts currency. Specifically, convert
euros to U.S. dollars. Prompt for the amount of money in
euros you have, and prompt for the current exchange rate
of the euro. Print out the new amount in U.S. dollars.




(STEP TWO: input, output, process):
    input:
        (1) your_euros: 81
        (2) exchange_rate : 137.51
        
    process:
        
        
        
        
    example output:
        How many euros are you exchanging? 81
        What is the exchange rate? 137.51
        81 euros at an exchange rate of 137.51 is
        111.38 U.S. dollars.
        
(STEP THREE: DESIGN TESTS)
        test1:
            input: 
                (1) your_euros: 81
                (2) exchange_rate : 137.51
                
            example output:
                How many euros are you exchanging? 81
                What is the exchange rate? 137.51
                81 euros at an exchange rate of 137.51 is
                111.38 U.S. dollars.
                
            
 (STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE

(STEP FIVE: TRUE CODE)               

'''
your_euros = int(input("How many euros are you exchanging? "))
exchange_rate = float(input("What is the exchange rate? "))
dollars = your_euros * exchange_rate /100

print('{} euros at an exchange rate of {} is {:.2f} U.S. dollars.'.format(your_euros,exchange_rate,dollars  ))


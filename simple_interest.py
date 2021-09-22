# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:38:32 2021

@author: Administrator
"""

'''(STEP ONE: a clear problem statement):
    Create a program that computes simple interest. Prompt for
the principal amount, the rate as a percentage, and the time,
and display the amount accrued (principal + interest).


(STEP TWO: input, output, process):
    input:
        (1)principal: 1500
        (2)interest_rate: 4.3
        (3)years: 4
    
    process:
        (1)prompt for principle with "Enter the principal: "
        (2)prompt for interest_rate with "Enter the rate of interest: "
            divede the input by 100
        (3)prompt for year with "Enter the number of years: "
        (4) initialize all_money to princle*(1+(interest_rate*years))
        (5)display:
            "After {years} years at {interest_rate}%, the investment will\nbe worth ${all_money}.".format(years = years, interest_rate = interest_rate , all_money = all_money )
    
    Example Output:
        Enter the principal: 1500
        Enter the rate of interest: 4.3
        Enter the number of years: 4
        
        After 4 years at 4.3%, the investment will
        be worth $1758.
        
(STEP THREE: DESIGN TESTS)
    test1:
        input:
            (1)principal: 1500
            (2)interest_rate: 4.3
            (3)years: 4
            
        expected Output:
            Enter the principal: 1500
            Enter the rate of interest: 4.3
            Enter the number of years: 4
            
            After 4 years at 4.3%, the investment will
            be worth $1758.
            
        actual output:

(STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE            
        
       
        

'''

#1.initialize principal to a input function 
#prompt for principle with "Enter the principal: "
#convert it to int
principal = int(input("Enter the principal: "))

#2.initialize interest_rate to a input function 
#prompt for interest_rate with "Enter the rate of interest: "
#divede the input by 100
#convert it to float
interest_rate =  (float(input("Enter the rate of interest: ")) / 100)

#3.initialize years to a input function 
#prompt for year with "Enter the number of years: "
#convert it to int
years = int(input("Enter the number of years: "))

#4.initialize all_money to princle*(1+(interest_rate*years))
all_money = int(principal*(1+(interest_rate*years)))


#display:
            #"After {years} years at {interest_rate}%, the investment will\nbe worth ${all_money}.".format(years = years, interest_rate = interest_rate , all_money = all_money )
print("After {years} years at {interest_rate}%, the investment will\nbe worth ${all_money}.".format(years = years, interest_rate = interest_rate*100 , all_money = all_money))
            
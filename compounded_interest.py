# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 20:34:50 2021

@author: Administrator
"""

'''(STEP ONE: a clear problem statement):
    Write a program to compute the value of an investment
compounded over time. The program should ask for the
starting amount, the number of years to invest, the interest
rate, and the number of periods per year to compound.



(STEP TWO: input, output, process):
    input:
        (1)principal: 1500
        (2)interest_rate: 4.3
        (3)years: 6
        (4)times_compounded: 4
        
    
    process:
        (1)prompt for principle with "What is the principal amount? "
        (2)prompt for interest_rate with "What is the rate? "
            divede the input by 100
        (3)prompt for years with "What is the number of years? "
        (4)prompt for times_compounded with "What is the number of times the interest\nis compounded per year? "
        (5)initialize final_amount to principal*((1+(interest_rate/times_compounded))**(times_compounded*years))
        (6)display:
            "${} invested at {}% for {} years\ncompounded {} times per year is $1938.84.".format(principal, interest_rate, years,times_compounded)
            
    
    output:
        What is the principal amount? 1500
        What is the rate? 4.3
        What is the number of years? 6
        What is the number of times the interest
        is compounded per year? 4
        $1500 invested at 4.3% for 6 years
        compounded 4 times per year is $1938.84.


(STEP THREE: DESIGN TESTS)
    test1:
        input:
            (1)principal: 1500
            (2)interest_rate: 4.3
            (3)years: 6
            (4)times_compounded: 4
            
        expected output:
            What is the principal amount? 1500
            What is the rate? 4.3
            What is the number of years? 6
            What is the number of times the interest
            is compounded per year? 4
            $1500 invested at 4.3% for 6 years
            compounded 4 times per year is $1938.84.
            
        actual result:

(STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE                
            

'''

#1.initialize principal to a input function 
#prompt for principle with "What is the principal amount? "
#convert it to int
principal = int(input("What is the principal amount? "))

#2.initialize interest_rate to a input function 
#prompt for interest_rate with "What is the rate? "
#divede the input by 100
#convert it to float
interest_rate = float(input("What is the rate? ")) / 100

#3.initialize years to a input function 
#prompt for year with "What is the number of years? " 
#convert it to int
years = int(input("What is the number of years? "))

#4.initialize times_compounded to a input function 
#prompt for year with "What is the number of times the interest\nis compounded per year?"
#convert it to int
times_compounded = int(input("What is the number of times the interest\nis compounded per year? "))

#5.initialize final_amount to principal*((1+(interest_rate/times_compounded))**(times_compounded*years))
final_amount = principal*((1+(interest_rate/times_compounded))**(times_compounded*years))

#6.display:
#            "${} invested at {}% for {} years\ncompounded {} times per year is ${}.".format(principal, interest_rate, years,times_compounded)
print("${} invested at {}% for {} years\ncompounded {} times per year is ${:.2f}.".format(principal, interest_rate*100, years, times_compounded, final_amount))



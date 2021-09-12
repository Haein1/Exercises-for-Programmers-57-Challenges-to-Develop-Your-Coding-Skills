# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 11:11:55 2021

@author: Administrator
"""

import math

'''(STEP ONE: a clear problem statement):
    Calculate gallons of paint needed to paint the ceiling of a
room. Prompt for the length and width, and assume one
gallon covers 350 square feet. Display the number of gallons
needed to paint the ceiling as a whole number.
    
    Remember, you can’t buy a partial gallon of paint. You must
round up to the next whole gallon.


(STEP TWO: input, output, process):
    input:
        length_feet: 30
        width_feet: 12
            
    process: 
        1. prompt for length_feet with "What is the length of your ceiling? "
        2. prompt for width_feet with "What is the width of your ceiling? "
        3.initialize area_feet to (length_feet * width_feet)
        4. initialize sq_to_gallon  to 350
        5. initialize num_gallon to (area_feet/sq_to_gallon)
        6. round up num_gallon
        7.display:
            "You will need to purchase {num_gallon} gallons of\npaint to cover {area_feet} square feet.".format(num_gallon = num_gallon, area_feet = area_feet)
        
        
    Example Output:
        You will need to purchase 2 gallons of
        paint to cover 360 square feet.
        
(STEP THREE: DESIGN AT LEAST FOUR TEST):
    test 1: for testing the normal occasion,
    input: 
        length_feet: 30
        width_feet: 12
        
    expected output:
                You will need to purchase 2 gallons of
        paint to cover 360 square feet.
        
    actual output:
        
(STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE
     
 (STEP FIVE: WRITE CODE)
    

'''
#1. INITIALIZE length_feet to input function
#prompt for length_feet with "What is the length of your ceiling? "
#covert it to int
length_feet = int(input("What is the length of your ceiling? "))

#2.initialize width_feet to input function
#prompt for width_feet with "What is the width of your ceiling? "
#covert it to int
width_feet = int(input("What is the width of your ceiling? "))

#3.initialize area_feet to (length_feet * width_feet)
area_feet = length_feet * width_feet

#4. initialize sq_to_gallon  to 350
sq_to_gallon = 350


#5. initialize num_gallon to (area_feet/sq_to_gallon)
# 6. round up num_gallon

num_gallon =  math.ceil(area_feet/sq_to_gallon)




# 7.display:
 #           "You will need to purchase {num_gallon} gallons of\npaint to cover {area_feet} square feet.".format(num_gallon = num_gallon, area_feet = area_feet)

print("You will need to purchase {num_gallon} gallons of\npaint to cover {area_feet} square feet.".format(num_gallon = num_gallon, area_feet = area_feet))


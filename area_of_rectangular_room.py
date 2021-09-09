# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:37:48 2021

@author: Administrator
"""

'''
(STEP ONE: a clear problem statement):
        Create a program that calculates the area of a room. Prompt
    the user for the length and width of the room in feet. Then
    display the area in both square feet and square meters.
    
        Constraints:
            • Keep the calculations separate from the output.
            • Use a constant to hold the conversion factor
            The formula for this conversion is:
                m^2 = f^2 × 0.09290304
    
(STEP TWO: input, output, process):
    input:
        1.f_length: 15
        2.f_width: 20
        
    process:
        1. prompt for f_length with " What is the length of the room in feet? "
        2. prompt for f_width with "What is the width of the room in feet? "
        3. display the area in both square feet and square meters as the example output does.
        
    
    example output:
        What is the length of the room in feet? 15
        What is the width of the room in feet? 20
        You entered dimensions of 15 feet by 20 feet.
        The area is
        300 square feet
        27.871 square meters
        
(STEP THREE: DESIGN AT LEAST FOUR TEST):
    input:
        1.f_length: 15
        2.f_width: 20
        
    example output:
        What is the length of the room in feet? 15
        What is the width of the room in feet? 20
        You entered dimensions of 15 feet by 20 feet.
        The area is
        300 square feet
        27.871 square meters
    
(STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE

'''

#1.initialize f_length to input function
#prompt for f_length with " What is the length of the room in feet? "
#convert it to int
f_length = int(input("What is the length of the room in feet? "))


#2.initialize f_width to input function
#prompt for f_width with "What is the width of the room in feet? "
#convert it to int
f_width = int(input("What is the width of the room in feet? "))


#3.initialize conversion_factor to 0.09290304  
conversion_factor = 0.09290304 

'''my error in the journey for solving this problem
# #4.initialize m_length to math.isqrt((f_length^2) *conversion_factor )
# #m_length^2 = (f_length^2) *conversion_factor 
# #m_length = (math.isqrt((f_width^2) *conversion_factor))
# m_length = math.isqrt((f_width^2) *int(conversion_factor))

# #5,initialize m_width to math.isqrt((f_width^2) *conversion_factor)
# m_width = math.isqrt((f_width^2) *int(conversion_factor))
'''



#6. initialize f_area  to (f_length*f_width)

f_area = f_length*f_width

#7.initialize m_area  to round((float(f_area) * conversion_factor),3)
m_area = round((float(f_area) * conversion_factor),3)
'''try to solve the conversion problem
f_area = 300
conversion_factor = 0.09290304
m_area = round(float(f_area) * conversion_factor)
print(m_area)
#print(round(m_area,3))

'''

#8.display:
    # "You entered dimensions of {f_length} feet by {f_width} feet.".format(f_length = f_length, f_width = f_width)
    #"The area is\n{f_area} square feet\n{m_area} square meters".format(f_area = f_area, m_area = m_area)
print("You entered dimensions of {f_length} feet by {f_width} feet.".format(f_length = f_length, f_width = f_width))
print("The area is\n{f_area} square feet\n{m_area} square meters".format(f_area = f_area, m_area = m_area))